"""
Tests for VCS workflow auto-detection logic
"""

import unittest
from datetime import datetime, timedelta
from typing import Dict, List, Tuple


class MockGitRepo:
    """Mock Git repository for testing detection logic"""

    def __init__(self):
        self.branches = []
        self.commits = []
        self.tags = []

    def add_branch(self, name: str, created_days_ago: int, deleted_days_ago: int = None):
        self.branches.append({
            'name': name,
            'created': datetime.now() - timedelta(days=created_days_ago),
            'deleted': datetime.now() - timedelta(days=deleted_days_ago) if deleted_days_ago else None
        })

    def add_commit(self, branch: str, message: str, days_ago: int):
        self.commits.append({
            'branch': branch,
            'message': message,
            'date': datetime.now() - timedelta(days=days_ago)
        })

    def add_tag(self, name: str, days_ago: int):
        self.tags.append({
            'name': name,
            'date': datetime.now() - timedelta(days=days_ago)
        })


class WorkflowDetector:
    """VCS workflow detection implementation"""

    def __init__(self, repo: MockGitRepo):
        self.repo = repo
        self.confidence_threshold = 0.7

    def detect(self) -> Tuple[str, float, List[str]]:
        """
        Detect workflow type with confidence score
        Returns: (workflow_type, confidence, evidence_list)
        """
        scores = {
            'gitflow': self._detect_gitflow(),
            'github_flow': self._detect_github_flow(),
            'trunk_based': self._detect_trunk_based()
        }

        # Find workflow with highest score
        best_workflow = max(scores.items(), key=lambda x: x[1][0])
        workflow_type = best_workflow[0]
        confidence = best_workflow[1][0]
        evidence = best_workflow[1][1]

        if confidence < self.confidence_threshold:
            workflow_type = 'unclear'

        return workflow_type, confidence, evidence

    def _detect_gitflow(self) -> Tuple[float, List[str]]:
        """Detect GitFlow indicators"""
        score = 0.0
        evidence = []

        # Check for develop branch
        develop_branches = [b for b in self.repo.branches
                          if b['name'] in ['develop', 'development']]
        if develop_branches:
            score += 0.3
            evidence.append("Found develop branch")

        # Check for release branches
        release_branches = [b for b in self.repo.branches
                          if b['name'].startswith('release/')]
        if release_branches:
            score += 0.3
            evidence.append(f"Found {len(release_branches)} release branches")

        # Check for hotfix branches
        hotfix_branches = [b for b in self.repo.branches
                         if b['name'].startswith('hotfix/')]
        if hotfix_branches:
            score += 0.2
            evidence.append("Found hotfix branches")

        # Check for version tags
        version_tags = [t for t in self.repo.tags
                       if t['name'].startswith('v')]
        if version_tags:
            score += 0.2
            evidence.append(f"Found {len(version_tags)} version tags")

        return score, evidence

    def _detect_github_flow(self) -> Tuple[float, List[str]]:
        """Detect GitHub Flow indicators"""
        score = 0.0
        evidence = []

        # Check for PR merge patterns
        pr_merges = [c for c in self.repo.commits
                    if 'Merge pull request' in c['message'] or 'Merge PR' in c['message']]
        if pr_merges:
            score += 0.3
            evidence.append(f"Found {len(pr_merges)} PR merges")

        # Check for short-lived feature branches
        feature_branches = [b for b in self.repo.branches
                          if b['name'].startswith('feature/')]
        if feature_branches:
            short_lived = [b for b in feature_branches
                          if b['deleted'] and (b['deleted'] - b['created']).days < 7]
            if short_lived:
                score += 0.3
                evidence.append(f"{len(short_lived)} feature branches < 7 days")

        # Check for squash-merge patterns
        squash_merges = [c for c in self.repo.commits
                        if '(#' in c['message']]  # Common squash merge pattern
        if squash_merges:
            score += 0.2
            evidence.append("Found squash-merge patterns")

        # No develop branch is a positive signal
        if not any(b['name'] in ['develop', 'development'] for b in self.repo.branches):
            score += 0.2
            evidence.append("No develop branch")

        return score, evidence

    def _detect_trunk_based(self) -> Tuple[float, List[str]]:
        """Detect Trunk-Based Development indicators"""
        score = 0.0
        evidence = []

        # Check for direct commits to main
        main_commits = [c for c in self.repo.commits
                       if c['branch'] in ['main', 'master']]
        total_commits = len(self.repo.commits)

        if total_commits > 0:
            main_ratio = len(main_commits) / total_commits
            if main_ratio > 0.5:
                score += 0.4
                evidence.append(f"{int(main_ratio * 100)}% commits directly to main")

        # Check for very short-lived branches
        all_branches = [b for b in self.repo.branches
                       if b['deleted'] and not b['name'] in ['main', 'master', 'develop']]
        if all_branches:
            very_short = [b for b in all_branches
                         if (b['deleted'] - b['created']).days < 1]
            if len(very_short) > len(all_branches) * 0.5:
                score += 0.3
                evidence.append(f"{len(very_short)} branches lived < 1 day")

        # Check for feature flags (simplified check)
        feature_flag_commits = [c for c in self.repo.commits
                               if 'feature flag' in c['message'].lower() or
                               'feature toggle' in c['message'].lower()]
        if feature_flag_commits:
            score += 0.3
            evidence.append("Found feature flag usage")

        return score, evidence

    def detect_migration(self, days_threshold: int = 30) -> Dict:
        """Detect if workflow has changed recently"""
        recent_date = datetime.now() - timedelta(days=days_threshold)
        historical_date = datetime.now() - timedelta(days=days_threshold * 3)

        # Split commits into periods
        recent_commits = [c for c in self.repo.commits
                         if c['date'] > recent_date]
        historical_commits = [c for c in self.repo.commits
                            if historical_date < c['date'] <= recent_date]

        # Simplified: check if branch patterns changed
        recent_branches = set(c['branch'] for c in recent_commits)
        historical_branches = set(c['branch'] for c in historical_commits)

        if recent_branches != historical_branches:
            return {
                'migration_detected': True,
                'recent_pattern': list(recent_branches),
                'historical_pattern': list(historical_branches)
            }

        return {'migration_detected': False}


class TestVCSDetection(unittest.TestCase):
    """Test cases for VCS workflow detection"""

    def test_detect_gitflow(self):
        """Test GitFlow detection with high confidence"""
        repo = MockGitRepo()
        repo.add_branch('develop', 365)
        repo.add_branch('release/1.0', 30, 10)
        repo.add_branch('release/1.1', 15, 5)
        repo.add_branch('hotfix/urgent-fix', 5, 3)
        repo.add_branch('feature/new-feature', 20, 7)
        repo.add_tag('v1.0.0', 30)
        repo.add_tag('v1.1.0', 15)

        detector = WorkflowDetector(repo)
        workflow, confidence, evidence = detector.detect()

        self.assertEqual(workflow, 'gitflow')
        self.assertGreaterEqual(confidence, 0.7)
        self.assertIn('Found develop branch', evidence)
        self.assertIn('release branches', ' '.join(evidence))

    def test_detect_github_flow(self):
        """Test GitHub Flow detection with high confidence"""
        repo = MockGitRepo()
        repo.add_branch('main', 365)
        repo.add_branch('feature/quick-fix', 5, 3)
        repo.add_branch('feature/new-ui', 10, 6)
        repo.add_commit('main', 'Merge pull request #123', 3)
        repo.add_commit('main', 'Merge pull request #124', 5)
        repo.add_commit('main', 'feat: Add new feature (#125)', 7)

        detector = WorkflowDetector(repo)
        workflow, confidence, evidence = detector.detect()

        self.assertEqual(workflow, 'github_flow')
        self.assertGreaterEqual(confidence, 0.5)
        self.assertIn('PR merges', ' '.join(evidence))

    def test_detect_trunk_based(self):
        """Test Trunk-Based Development detection"""
        repo = MockGitRepo()
        repo.add_branch('main', 365)
        repo.add_branch('fix-123', 2, 1)  # Very short-lived
        repo.add_branch('update-456', 1, 0.5)

        # Many direct commits to main
        for i in range(20):
            repo.add_commit('main', f'feat: Direct commit {i}', i)

        # Few branch commits
        repo.add_commit('fix-123', 'fix: Quick fix', 2)
        repo.add_commit('main', 'chore: Enable feature flag for new UI', 5)

        detector = WorkflowDetector(repo)
        workflow, confidence, evidence = detector.detect()

        self.assertEqual(workflow, 'trunk_based')
        self.assertIn('commits directly to main', ' '.join(evidence))

    def test_detect_unclear_workflow(self):
        """Test detection with low confidence returns 'unclear'"""
        repo = MockGitRepo()
        repo.add_branch('main', 365)
        # Very minimal activity
        repo.add_commit('main', 'Initial commit', 300)

        detector = WorkflowDetector(repo)
        workflow, confidence, evidence = detector.detect()

        self.assertEqual(workflow, 'unclear')
        self.assertLess(confidence, 0.7)

    def test_detect_migration(self):
        """Test workflow migration detection"""
        repo = MockGitRepo()

        # Historical: GitFlow pattern
        repo.add_commit('develop', 'feat: Old feature', 60)
        repo.add_commit('release/1.0', 'chore: Release prep', 50)

        # Recent: GitHub Flow pattern
        repo.add_commit('main', 'Merge pull request #200', 10)
        repo.add_commit('main', 'Merge pull request #201', 5)

        detector = WorkflowDetector(repo)
        migration = detector.detect_migration()

        self.assertTrue(migration['migration_detected'])
        self.assertIn('develop', migration['historical_pattern'])
        self.assertNotIn('develop', migration['recent_pattern'])

    def test_confidence_scoring(self):
        """Test confidence score calculation"""
        repo = MockGitRepo()
        repo.add_branch('develop', 365)  # 0.3 points for GitFlow
        repo.add_branch('release/1.0', 30, 10)  # 0.3 points for GitFlow

        detector = WorkflowDetector(repo)
        workflow, confidence, evidence = detector.detect()

        self.assertAlmostEqual(confidence, 0.6, places=1)
        self.assertEqual(len(evidence), 2)


if __name__ == '__main__':
    unittest.main()