# VCS Discovery Task

## Purpose

Intelligently identify and adapt to the team's version control system using a hybrid detection + confirmation approach.

## Philosophy

- **Detection as a HINT, not a DECISION**
- Optimize for the 85-90% who use Git
- Auto-detect for brownfield, ask for greenfield
- Confirm with user when confidence < 100%
- Progressive disclosure: simple cases fast, complex cases handled

## Task Instructions

### Step 0: Auto-Detection (Brownfield Projects)

For existing Git repositories, attempt automatic workflow detection:

```yaml
auto_detection:
  enabled: true
  confidence_threshold: 0.7

  indicators:
    gitflow:
      - pattern: 'branch:develop exists'
        weight: 0.3
      - pattern: 'branches matching release/* or hotfix/*'
        weight: 0.3
      - pattern: 'long-lived feature branches (>14 days)'
        weight: 0.2
      - pattern: 'version tags (v1.0.0, etc.)'
        weight: 0.2

    github_flow:
      - pattern: 'PR/MR merges to main/master'
        weight: 0.3
      - pattern: 'feature/* branches < 7 days lifespan'
        weight: 0.3
      - pattern: 'squash-and-merge commit patterns'
        weight: 0.2
      - pattern: 'no develop branch'
        weight: 0.2

    trunk_based:
      - pattern: 'direct commits to main > 50%'
        weight: 0.4
      - pattern: 'branches live < 1 day'
        weight: 0.3
      - pattern: 'feature flags in codebase'
        weight: 0.3

  migration_detection:
    check_periods:
      recent: 'last 30 days'
      historical: '30-90 days ago'
    alert_if_different: true
```

#### Detection Results Presentation

If detection confidence ≥ 70%:

```yaml
prompt: |
  🔍 Analyzed your Git history...

  Detected workflow: **{detected_workflow}** (confidence: {score}%)

  Evidence:
  {foreach evidence}
    ✓ {evidence_item}
  {/foreach}

  Is this correct?
  1. Yes, that's right
  2. No, we actually use something else
  3. We recently changed our approach
  4. It's more complex than that
```

If detection confidence < 70% or no Git repo found, proceed to Step 1.

### Step 1: Initial Discovery

```yaml
elicit: true
prompt: |
  How does your team manage code versions?

  1. Git with GitHub/GitLab/Bitbucket [MOST COMMON]
  2. Git with corporate server
  3. Other version control system
  4. No version control needed
  5. Custom/Complex setup

  Select a number (1-5):
```

### Step 2A: Git-Based Workflows (Options 1-2)

If user selects Git-based (or auto-detection had low confidence):

```yaml
elicit: true
prompt: |
  Which Git workflow best describes your team's approach?

  1. GitHub Flow - Simple feature branches with pull requests
     → Best for: Web apps, continuous deployment

  2. GitFlow - Structured branches (develop, release, hotfix)
     → Best for: Versioned software, scheduled releases

  3. Trunk-Based - Direct commits or very short branches
     → Best for: Mature CI/CD, experienced teams

  4. Not sure - I'd like a recommendation
     → We'll ask a few questions to suggest the best fit

  5. Custom Git workflow
     → Describe your approach

  Select a number (1-5):
```

#### If "Not sure" (Option 4) or Low Auto-Detection Confidence:

```yaml
elicit: true
questions:
  - 'How many developers on your team? (1, 2-5, 6+)'
  - 'How often do you release? (Daily, Weekly, Monthly, Quarterly)'
  - 'Do you have automated testing? (Yes/No)'
  - 'Do you need to maintain multiple versions? (Yes/No)'

recommendation_logic: |
  - Solo or Daily releases + Automated tests → Trunk-Based
  - Small team + Weekly/Monthly → GitHub Flow
  - Large team or Multiple versions → GitFlow
  - Default → GitHub Flow (safest choice)
```

#### If "Custom" (Option 5):

```yaml
elicit: true
prompt: |
  Please briefly describe your Git workflow:
  (e.g., "We use feature branches but merge to staging first, then production")

  [Free text input]
```

### Step 2B: Other VCS (Option 3)

```yaml
elicit: true
prompt: |
  Which version control system do you use?

  1. Subversion (SVN)
  2. Perforce
  3. Mercurial
  4. Team Foundation Server (TFS)
  5. Other (please specify)

  Select a number or describe:
```

### Step 2C: No VCS (Option 4)

```yaml
confirm: |
  Understood. BMAD will generate:
  - Self-contained deliverables
  - Date-versioned packages
  - No commit messages or branch references

  Is this a prototype/one-time project? (Yes/No)
```

### Step 2D: Complex Setup (Option 5)

```yaml
elicit: true
prompt: |
  Please describe your version control setup:
  (e.g., "Monorepo with custom tooling", "Multiple systems for different components")

  [Free text input]
```

### Step 2E: Handle Workflow Migration

If auto-detection found different patterns in recent vs historical periods:

```yaml
prompt: |
  📊 Noticed a change in your workflow patterns:

  **Previously (30-90 days ago):**
  - {old_workflow_patterns}

  **Recently (last 30 days):**
  - {new_workflow_patterns}

  Which should BMAD optimize for?
  1. The new approach (we've migrated)
  2. The old approach (recent was exceptional)
  3. Both (we're in transition)
  4. Neither (let me explain)
```

### Step 3: Store Configuration with Metadata

Save the enhanced VCS configuration for all agents to access:

```yaml
vcs_config:
  type: [git|svn|perforce|none|custom]
  workflow: [github-flow|gitflow|trunk-based|custom|none]
  details: [user's custom description if provided]

  # New metadata for auto-detection
  detection_method: [auto-detected|user-selected|hybrid]
  confidence_score: 0.85 # If auto-detected
  detection_evidence:
    - 'Found develop branch'
    - 'Release branches present'
    - 'Average branch lifespan: 12 days'

  adaptations:
    artifact_format: [branches|monolithic|platform-specific]
    terminology: [git|generic|platform-specific]
    commit_style: [conventional|team-specific|none]

  # Cache for subsequent runs
  cache:
    detected_at: '2024-01-15T10:30:00Z'
    valid_until: '2024-01-22T10:30:00Z' # 7 days
```

### Step 4: Cached Detection on Subsequent Runs

```yaml
if cache_exists and not expired:
  prompt: |
    📌 Last time you were using **{cached_workflow}**.
    Still accurate? (Y/n):

  if no:
    options: 1. "We switched workflows" → Re-run detection
      2. "It was incorrectly detected" → Manual selection
      3. "Let me choose again" → Show full menu
```

### Step 5: Confirm Understanding

```yaml
output: |
  VCS Configuration Confirmed:
  - System: {type}
  - Workflow: {workflow}
  {if auto_detected}
  - Detection confidence: {confidence}%
  {/if}
  - BMAD will adapt by: {key_adaptations}

  All agents will generate artifacts compatible with your setup.
```

## Escape Hatches

For advanced users who want to bypass auto-detection:

```yaml
cli_options:
  --skip-detection: 'Jump straight to manual selection'
  --force-workflow=[gitflow|github|trunk]: 'Specify workflow directly'
  --no-cache: "Don't cache detection results"

example_usage: |
  bmad init --skip-detection
  bmad init --force-workflow=gitflow
```

## Success Criteria

- **Auto-detection accuracy > 80%** for standard workflows
- **User correction rate < 20%** for auto-detected cases
- **Time to configuration < 30 seconds** for detected cases
- 80% of users can select from predefined options (when not auto-detected)
- 20% custom cases are handled gracefully
- Configuration is stored and accessible to all agents
- No Git assumptions for non-Git users
- Clear recommendations when requested
- **Detection treated as hint, not decision** - always confirmed with user

## Agent Adaptations Based on VCS

### For Architect Agent

- Git + GitHub Flow: Suggest feature-based architecture docs
- Git + GitFlow: Support release-oriented planning
- No VCS: Generate comprehensive, dated documents
- Custom: Ask for preferred format

### For Dev Agent

- Git workflows: Generate appropriate commit messages
- No VCS: Package complete code solutions
- Custom: Follow described conventions

### For SM Agent

- Git + Trunk: Create small, atomic stories
- Git + GitFlow: Support epic-based stories
- No VCS: Create comprehensive story documents

## Notes

- This discovery happens ONCE at project start
- All agents read this configuration
- Can be updated if team process changes
- Default to GitHub Flow if uncertain (most common, safest)
