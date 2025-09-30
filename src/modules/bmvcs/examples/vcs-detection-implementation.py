#!/usr/bin/env python3
"""
Example implementation of VCS workflow auto-detection for BMAD agents.
This can be adapted for different languages and Git libraries.
"""

import subprocess
import json
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Optional


class GitWorkflowDetector:
    """
    Auto-detect Git workflow from repository history.
    Follows the principle: "Detection as a HINT, not a DECISION"
    """

    def __init__(self, repo_path: str = '.'):
        self.repo_path = repo_path
        self.confidence_threshold = 0.7

    def run_git_command(self, cmd: str) -> Optional[str]:
        """Execute git command and return output"""
        try:
            result = subprocess.run(
                cmd.split(),
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError:
            return None

    def detect_workflow(self) -> Dict:
        """
        Main detection method that returns workflow suggestion with confidence.
        """
        if not self.is_git_repo():
            return {
                'detected': False,
                'reason': 'Not a Git repository'
            }

        # Calculate scores for each workflow
        gitflow_score = self._score_gitflow()
        github_flow_score = self._score_github_flow()
        trunk_based_score = self._score_trunk_based()

        # Check for migration
        migration_info = self._detect_migration()

        # Determine best match
        scores = {
            'gitflow': gitflow_score,
            'github_flow': github_flow_score,
            'trunk_based': trunk_based_score
        }

        best_workflow = max(scores.items(), key=lambda x: x[1]['score'])
        workflow_name = best_workflow[0]
        confidence = best_workflow[1]['score']
        evidence = best_workflow[1]['evidence']

        # Check if confidence meets threshold
        if confidence < self.confidence_threshold:
            return {
                'detected': True,
                'workflow': 'unclear',
                'confidence': confidence,
                'evidence': evidence,
                'needs_clarification': True,
                'migration_detected': migration_info['detected']
            }

        return {
            'detected': True,
            'workflow': workflow_name,
            'confidence': confidence,
            'evidence': evidence,
            'migration_detected': migration_info['detected'],
            'migration_info': migration_info if migration_info['detected'] else None
        }

    def is_git_repo(self) -> bool:
        """Check if current directory is a Git repository"""
        return self.run_git_command('git rev-parse --git-dir') is not None

    def _score_gitflow(self) -> Dict:
        """Score GitFlow indicators"""
        score = 0.0
        evidence = []

        # Check for develop branch
        branches = self.run_git_command('git branch -a')
        if branches and ('develop' in branches or 'development' in branches):
            score += 0.3
            evidence.append("Found develop branch")

        # Check for release branches
        if branches and 'release/' in branches:
            release_count = branches.count('release/')
            score += 0.3
            evidence.append(f"Found {release_count} release branches")

        # Check for hotfix branches
        if branches and 'hotfix/' in branches:
            score += 0.2
            evidence.append("Found hotfix branches")

        # Check for version tags
        tags = self.run_git_command('git tag -l v*')
        if tags:
            tag_count = len(tags.split('\n'))
            score += 0.2
            evidence.append(f"Found {tag_count} version tags")

        return {'score': score, 'evidence': evidence}

    def _score_github_flow(self) -> Dict:
        """Score GitHub Flow indicators"""
        score = 0.0
        evidence = []

        # Check for PR merge patterns in recent commits
        recent_commits = self.run_git_command(
            'git log --oneline --since="90 days ago" --grep="Merge pull request"'
        )
        if recent_commits:
            pr_count = len(recent_commits.split('\n'))
            score += 0.3
            evidence.append(f"Found {pr_count} PR merges in last 90 days")

        # Check for squash merge patterns
        squash_commits = self.run_git_command(
            'git log --oneline --since="90 days ago" --grep="(#"'
        )
        if squash_commits:
            score += 0.2
            evidence.append("Found squash-merge patterns")

        # Check average branch lifespan (simplified)
        branches = self.run_git_command('git branch -a')
        if branches and 'feature/' in branches:
            score += 0.3
            evidence.append("Using feature branch naming")

        # No develop branch is positive for GitHub Flow
        if branches and 'develop' not in branches:
            score += 0.2
            evidence.append("No develop branch (GitHub Flow indicator)")

        return {'score': score, 'evidence': evidence}

    def _score_trunk_based(self) -> Dict:
        """Score Trunk-Based Development indicators"""
        score = 0.0
        evidence = []

        # Check ratio of direct commits to main
        main_commits = self.run_git_command(
            'git log --oneline --since="90 days ago" --first-parent main'
        )
        all_commits = self.run_git_command(
            'git log --oneline --since="90 days ago"'
        )

        if main_commits and all_commits:
            main_count = len(main_commits.split('\n'))
            total_count = len(all_commits.split('\n'))
            ratio = main_count / total_count

            if ratio > 0.5:
                score += 0.4
                evidence.append(f"{int(ratio * 100)}% commits directly to main")

        # Check for feature flags in commit messages
        feature_flag_commits = self.run_git_command(
            'git log --oneline --since="90 days ago" --grep="feature flag" -i'
        )
        if feature_flag_commits:
            score += 0.3
            evidence.append("Found feature flag usage in commits")

        # Check for very short-lived branches (would need more complex analysis)
        # Simplified: check if most branches are deleted quickly
        deleted_branches = self.run_git_command('git reflog show --all | grep "branch:"')
        if deleted_branches:
            score += 0.3
            evidence.append("Pattern suggests short-lived branches")

        return {'score': score, 'evidence': evidence}

    def _detect_migration(self) -> Dict:
        """Detect if workflow has changed recently"""
        # Compare recent vs historical commit patterns
        recent = self.run_git_command(
            'git log --oneline --since="30 days ago" --pretty=format:"%d"'
        )
        historical = self.run_git_command(
            'git log --oneline --since="90 days ago" --until="30 days ago" --pretty=format:"%d"'
        )

        if not recent or not historical:
            return {'detected': False}

        # Simple heuristic: check if branch naming patterns changed
        recent_has_develop = 'develop' in recent
        historical_has_develop = 'develop' in historical

        if recent_has_develop != historical_has_develop:
            return {
                'detected': True,
                'recent_pattern': 'GitFlow-like' if recent_has_develop else 'GitHub Flow-like',
                'historical_pattern': 'GitFlow-like' if historical_has_develop else 'GitHub Flow-like'
            }

        return {'detected': False}

    def interactive_confirmation(self, detection_result: Dict) -> str:
        """
        Present detection results to user and get confirmation.
        This demonstrates the "hint not decision" principle.
        """
        if not detection_result['detected']:
            print(f"❌ {detection_result['reason']}")
            return self.manual_selection()

        if detection_result['workflow'] == 'unclear':
            print("🤔 Could not confidently detect your workflow.")
            print(f"   Confidence: {detection_result['confidence']:.1%}")
            return self.clarifying_questions()

        # Present detection with evidence
        print(f"🔍 Analyzed your Git history...")
        print(f"\nDetected workflow: **{detection_result['workflow']}**")
        print(f"Confidence: {detection_result['confidence']:.1%}\n")
        print("Evidence:")
        for item in detection_result['evidence']:
            print(f"  ✓ {item}")

        if detection_result['migration_detected']:
            print("\n📊 Note: Detected a possible workflow change recently")
            print(f"   Recent: {detection_result['migration_info']['recent_pattern']}")
            print(f"   Historical: {detection_result['migration_info']['historical_pattern']}")

        # Get confirmation
        print("\nIs this correct?")
        print("1. Yes, that's right")
        print("2. No, we actually use something else")
        print("3. We recently changed our approach")
        print("4. It's more complex than that")

        choice = input("\nSelect (1-4): ")

        if choice == '1':
            return detection_result['workflow']
        elif choice == '3':
            return self.handle_migration()
        else:
            return self.manual_selection()

    def clarifying_questions(self) -> str:
        """Ask progressive questions when detection is unclear"""
        print("\nLet me ask a few questions to understand your workflow better:\n")

        # Progressive questions to increase confidence
        score_adjustments = {
            'gitflow': 0,
            'github_flow': 0,
            'trunk_based': 0
        }

        # Question 1: Team size
        print("1. How many developers actively commit code?")
        print("   a) Just me")
        print("   b) 2-5 developers")
        print("   c) 6+ developers")
        team_size = input("Select (a-c): ")

        if team_size == 'a':
            score_adjustments['trunk_based'] += 0.3
        elif team_size == 'b':
            score_adjustments['github_flow'] += 0.2
        elif team_size == 'c':
            score_adjustments['gitflow'] += 0.2

        # Question 2: Release frequency
        print("\n2. How often do you release to production?")
        print("   a) Multiple times daily")
        print("   b) Weekly")
        print("   c) Monthly or less frequently")
        release_freq = input("Select (a-c): ")

        if release_freq == 'a':
            score_adjustments['trunk_based'] += 0.3
        elif release_freq == 'b':
            score_adjustments['github_flow'] += 0.3
        elif release_freq == 'c':
            score_adjustments['gitflow'] += 0.3

        # Determine recommendation
        best_workflow = max(score_adjustments.items(), key=lambda x: x[1])
        return best_workflow[0]

    def manual_selection(self) -> str:
        """Fallback to manual workflow selection"""
        print("\nWhich Git workflow best describes your team's approach?\n")
        print("1. GitHub Flow - Simple feature branches with pull requests")
        print("   → Best for: Web apps, continuous deployment\n")
        print("2. GitFlow - Structured branches (develop, release, hotfix)")
        print("   → Best for: Versioned software, scheduled releases\n")
        print("3. Trunk-Based - Direct commits or very short branches")
        print("   → Best for: Mature CI/CD, experienced teams\n")
        print("4. Custom Git workflow")

        choice = input("Select (1-4): ")

        workflow_map = {
            '1': 'github_flow',
            '2': 'gitflow',
            '3': 'trunk_based',
            '4': 'custom'
        }

        return workflow_map.get(choice, 'github_flow')

    def handle_migration(self) -> str:
        """Handle workflow migration scenario"""
        print("\nWhich workflow should BMAD optimize for?")
        print("1. The new approach (we've completed migration)")
        print("2. The old approach (recent activity was exceptional)")
        print("3. Both (we're still transitioning)")

        choice = input("Select (1-3): ")

        if choice == '3':
            print("\nWhich workflow is your target state?")

        return self.manual_selection()


def main():
    """Example usage of the detector"""
    detector = GitWorkflowDetector()

    # Run detection
    result = detector.detect_workflow()

    # Get user confirmation (following "hint not decision" principle)
    confirmed_workflow = detector.interactive_confirmation(result)

    # Save configuration
    config = {
        'vcs_config': {
            'type': 'git',
            'workflow': confirmed_workflow,
            'detection_method': 'auto-detected' if result['detected'] else 'user-selected',
            'confidence_score': result.get('confidence', 0),
            'detection_evidence': result.get('evidence', []),
            'cache': {
                'detected_at': datetime.now().isoformat(),
                'valid_until': (datetime.now() + timedelta(days=7)).isoformat()
            }
        }
    }

    print(f"\n✅ Configuration saved!")
    print(f"   Workflow: {confirmed_workflow}")
    print(f"   All BMAD agents will adapt to your {confirmed_workflow} workflow.")

    # Save to file (in real implementation)
    with open('.bmad/vcs_config.json', 'w') as f:
        json.dump(config, f, indent=2)


if __name__ == '__main__':
    main()
