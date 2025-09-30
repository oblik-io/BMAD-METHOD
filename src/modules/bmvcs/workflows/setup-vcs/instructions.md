# VCS Setup Workflow Instructions

## Purpose

Guide users through VCS discovery and configuration at project initialization, ensuring BMAD adapts to their version control practices.

## When to Use

- New project initialization with BMAD
- First-time BMAD user in existing project
- Team changing VCS workflows
- VCS configuration missing or outdated

## Workflow Overview

```
1. Detect existing VCS → 2. Discovery questions → 3. Confirm workflow → 4. Save configuration
```

## Step-by-Step Instructions

### Step 1: Check Existing Configuration

**Action:** Look for `.bmad-core/vcs-config.yaml`

**If exists and valid (<7 days old):**

```yaml
action: confirm_existing
prompt: |
  Found existing VCS configuration:
  - System: {type}
  - Workflow: {workflow}

  Is this still accurate? (Yes/No)
```

**If No or missing:** Proceed to Step 2

### Step 2: Auto-Detection (Optional)

**For Git repositories only:**

```yaml
action: attempt_detection
method: analyze_history
confidence_threshold: 0.7

if_high_confidence:
  present:
    - Detected workflow with evidence
    - Ask for confirmation

if_low_confidence:
  skip_to: manual_discovery
```

**Detection analyzes:**

- Branch patterns (develop, release/\*, hotfix/\*)
- Commit messages (PR merges, squash patterns)
- Tag patterns (version tags)
- Commit frequency to main branch
- Feature flag mentions

**Present results:**

```
🔍 Analyzed your Git history...

Detected workflow: GitHub Flow
Confidence: 85%

Evidence:
✓ Found 23 PR merges in last 90 days
✓ Using feature branch naming
✓ No develop branch (GitHub Flow indicator)

Is this correct?
1. Yes, that's right
2. No, we actually use something else
3. We recently changed our approach
```

### Step 3: Discovery Questions

**Initial Question:**

```yaml
question: 'How does your team manage code versions?'
options:
  1: 'Git with GitHub/GitLab/Bitbucket [MOST COMMON]'
  2: 'Git with corporate server'
  3: 'Other version control system'
  4: 'No version control needed'
  5: 'Custom/Complex setup'
```

#### Path 3A: Git-Based Workflows (Options 1-2)

```yaml
question: 'Which Git workflow best describes your approach?'
options:
  1:
    name: 'GitHub Flow'
    description: 'Simple feature branches with pull requests'
    best_for: 'Web apps, continuous deployment'

  2:
    name: 'GitFlow'
    description: 'Structured branches (develop, release, hotfix)'
    best_for: 'Versioned software, scheduled releases'

  3:
    name: 'Trunk-Based'
    description: 'Direct commits or very short branches'
    best_for: 'Mature CI/CD, experienced teams'

  4:
    name: 'Not sure'
    action: 'trigger_clarifying_questions'

  5:
    name: 'Custom Git workflow'
    action: 'request_description'
```

**If "Not sure":**

```yaml
clarifying_questions:
  q1:
    question: 'How many developers on your team?'
    options: ['1', '2-5', '6+']
    scoring:
      '1': { trunk_based: +0.3 }
      '2-5': { github_flow: +0.2 }
      '6+': { gitflow: +0.2 }

  q2:
    question: 'How often do you release?'
    options: ['Daily', 'Weekly', 'Monthly', 'Quarterly']
    scoring:
      'Daily': { trunk_based: +0.3 }
      'Weekly': { github_flow: +0.3 }
      'Monthly': { gitflow: +0.3 }
      'Quarterly': { gitflow: +0.3 }

  q3:
    question: 'Do you have automated testing?'
    options: ['Yes', 'No']
    scoring:
      'Yes': { trunk_based: +0.2 }

  q4:
    question: 'Do you maintain multiple versions?'
    options: ['Yes', 'No']
    scoring:
      'Yes': { gitflow: +0.4 }

recommendation: 'Based on your answers, we suggest: {highest_score}'
```

#### Path 3B: Other VCS (Option 3)

```yaml
question: 'Which version control system do you use?'
options:
  1: 'Subversion (SVN)'
  2: 'Perforce'
  3: 'Mercurial'
  4: 'Team Foundation Server (TFS)'
  5: 'Other (please specify)'
```

#### Path 3C: No VCS (Option 4)

```yaml
confirm: |
  Understood. BMAD will generate:
  - Self-contained deliverables
  - Date-versioned packages
  - No commit messages or branch references

question: 'Is this a prototype or one-time project?'
action: 'Save configuration with type=none'
```

#### Path 3D: Custom/Complex (Option 5)

```yaml
prompt: |
  Please describe your version control setup:
  (e.g., "Monorepo with custom tooling", "Multiple systems for different components")

action: 'free_text_input'
follow_up: 'Ask component-specific questions if multi-VCS'
```

### Step 4: Save Configuration

**Create `.bmad-core/vcs-config.yaml`:**

```yaml
vcs_config:
  type: git|svn|perforce|none|custom
  workflow: github-flow|gitflow|trunk-based|custom|none
  details: "User's custom description if provided"

  adaptations:
    artifact_format: branches|monolithic|platform-specific
    terminology: git|svn|generic|custom
    commit_style: conventional|team-specific|none

  metadata:
    configured_at: '2024-09-30T12:00:00Z'
    method: auto-detected|user-selected|recommended
    confidence_score: 0.85 # if auto-detected
    cache_valid_until: '2024-10-07T12:00:00Z'
```

**Confirm to user:**

```
✅ VCS Configuration Saved!

System: Git
Workflow: GitHub Flow
Adaptations: Small PRs, feature branches, conventional commits

All BMAD agents will now adapt to your workflow:
- Architect: Lightweight, PR-sized architecture docs
- PM: Feature-scoped requirements
- SM: Small stories mapping to single PRs
- Dev: Feature branch suggestions, atomic commits
- QA: PR-focused test plans
```

## Edge Cases

### Migration Detected

```yaml
if: recent_pattern != historical_pattern
action: |
  📊 Note: Detected a possible workflow change
  Recent: GitHub Flow-like
  Historical: GitFlow-like

  Which should BMAD optimize for?
  1. New approach (migration complete)
  2. Old approach (recent was exceptional)
  3. Both (still transitioning)
```

### Fresh Repository (<10 commits)

```yaml
if: commit_count < 10
action: skip_detection
message: 'Repository too new for reliable detection'
default_to: manual_selection
```

### Non-Git Repository

```yaml
if: not is_git_repo()
action: skip_detection
prompt: 'What version control system do you use?'
options: [SVN, Perforce, Mercurial, TFS, None, Other]
```

## Success Criteria

- ✅ Configuration saved in `.bmad-core/vcs-config.yaml`
- ✅ User confirmed workflow selection
- ✅ No Git assumptions for non-Git users
- ✅ Graceful handling of unclear cases
- ✅ Cache validity set (7 days)

## Error Handling

### Detection Fails

```yaml
fallback: manual_selection
message: "Could not analyze repository. Let's select manually."
```

### Invalid Selection

```yaml
action: re-prompt
validation: 'Please select a valid option (1-5)'
```

### Configuration Write Fails

```yaml
fallback: in_memory_config
warning: 'Could not save configuration. Will use for this session only.'
action: suggest_manual_save
```

## Related Files

- [Checklist](./checklist.md) - Pre/post setup checklist
- [Workflow Definition](./workflow.yaml) - Machine-readable workflow
- [Discovery Task](../../tasks/discover-vcs.md) - Discovery implementation
- [Detection Confidence](../../docs/VCS_DETECTION_CONFIDENCE.md) - Detection algorithms
