# Validate VCS Configuration Task

## Purpose

Validate that the VCS configuration file exists and contains valid settings.

## Task Instructions

### Step 1: Check Configuration Exists

```yaml
check_file: .bmad/vcs-config.yaml
if_missing: |
  VCS configuration not found. Please run VCS discovery first:
  - Activate VCS Adapter agent
  - Run: *discover
```

### Step 2: Validate Structure

```yaml
validate_yaml:
  required_fields:
    - vcs_config.type
    - vcs_config.workflow
    - vcs_config.adaptations.artifact_format
    - vcs_config.adaptations.terminology
    - vcs_config.adaptations.commit_style
```

### Step 3: Validate Values

```yaml
validate_values:
  vcs_config.type:
    allowed: [git, svn, perforce, mercurial, tfs, none, custom]

  vcs_config.workflow:
    allowed: [github-flow, gitflow, trunk-based, custom, none]

  vcs_config.adaptations.artifact_format:
    allowed: [branches, monolithic, platform-specific]

  vcs_config.adaptations.terminology:
    allowed: [git, svn, generic, platform-specific, custom]

  vcs_config.adaptations.commit_style:
    allowed: [conventional, team-specific, none]
```

### Step 4: Report Results

```yaml
output: |
  ✅ VCS Configuration Valid

  System: {type}
  Workflow: {workflow}
  Artifact Format: {artifact_format}
  Terminology: {terminology}
  Commit Style: {commit_style}
```

## Error Handling

If validation fails:

- Report specific field with error
- Suggest correction
- Offer to re-run discovery

## Success Criteria

- Configuration file exists
- All required fields present
- All values within allowed ranges
- YAML syntax valid
