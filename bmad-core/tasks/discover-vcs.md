# VCS Discovery Task

## Purpose

Identify and adapt to the team's version control system at project initialization.

## Philosophy

- Optimize for the 85-90% who use Git
- Remain open for the 10-15% with special needs
- Suggest best practices without forcing them

## Task Instructions

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

If user selects Git-based:

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

#### If "Not sure" (Option 4):

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

### Step 3: Store Configuration

Save the VCS configuration for all agents to access:

```yaml
vcs_config:
  type: [git|svn|perforce|none|custom]
  workflow: [github-flow|gitflow|trunk-based|custom|none]
  details: [user's custom description if provided]

  adaptations:
    artifact_format: [branches|monolithic|platform-specific]
    terminology: [git|generic|platform-specific]
    commit_style: [conventional|team-specific|none]
```

### Step 4: Confirm Understanding

```yaml
output: |
  VCS Configuration Confirmed:
  - System: {type}
  - Workflow: {workflow}
  - BMAD will adapt by: {key_adaptations}

  All agents will generate artifacts compatible with your setup.
```

## Success Criteria

- 80% of users can select from predefined options
- 20% custom cases are handled gracefully
- Configuration is stored and accessible to all agents
- No Git assumptions for non-Git users
- Clear recommendations when requested

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
