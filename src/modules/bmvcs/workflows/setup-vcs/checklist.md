# VCS Setup Workflow Checklist

## Pre-Setup Checklist

Run through these items **before** starting VCS configuration:

### Environment Check

- [ ] `.bmad-core/` directory exists or can be created
- [ ] User has write permissions to project directory
- [ ] If Git repo: Can run `git` commands

### Information Gathering

- [ ] Understand project type (prototype, production, migration, etc.)
- [ ] Know team size (solo, small team, large team)
- [ ] Know release frequency (daily, weekly, monthly, quarterly)
- [ ] Know if multiple versions need maintenance

### Existing Configuration

- [ ] Check if `.bmad-core/vcs-config.yaml` exists
- [ ] If exists: Check if valid (< 7 days old)
- [ ] If exists: Ask user if still accurate

## During Setup Checklist

Follow these during the VCS discovery workflow:

### Detection Phase (Git only)

- [ ] Attempt auto-detection if Git repository
- [ ] Calculate confidence score
- [ ] Present evidence if confidence >= 70%
- [ ] Skip to manual selection if confidence < 70%

### Discovery Phase

- [ ] Ask initial VCS question
- [ ] Branch based on response (Git, Other VCS, No VCS, Custom)
- [ ] If Git: Ask workflow question
- [ ] If "Not sure": Ask clarifying questions
- [ ] If Custom: Request detailed description

### Confirmation Phase

- [ ] Present detected or selected workflow
- [ ] Show adaptations that will be applied
- [ ] Get explicit user confirmation
- [ ] Handle edge cases (migration, unclear, fresh repo)

### Configuration Phase

- [ ] Create `.bmad-core/` directory if needed
- [ ] Write `vcs-config.yaml` with correct format
- [ ] Set cache validity (7 days from now)
- [ ] Record detection method and confidence

## Post-Setup Checklist

Verify setup completion:

### Configuration Verification

- [ ] `.bmad-core/vcs-config.yaml` exists
- [ ] File contains valid YAML
- [ ] `type` field is set correctly
- [ ] `workflow` field is set correctly
- [ ] `cache_valid_until` is set to future date

### User Confirmation

- [ ] Show success message to user
- [ ] Display configured workflow
- [ ] Explain agent adaptations
- [ ] Provide instructions for updating config later

### Agent Integration

- [ ] Architect agent can read VCS config
- [ ] PM agent can read VCS config
- [ ] SM agent can read VCS config
- [ ] Dev agent can read VCS config
- [ ] QA agent can read VCS config

### Documentation

- [ ] User knows how to view configuration
- [ ] User knows how to update configuration
- [ ] User knows when cache expires (7 days)
- [ ] User knows how to trigger re-detection

## Validation Checklist

Ensure configuration quality:

### Content Validation

- [ ] VCS type is one of: `git`, `svn`, `perforce`, `mercurial`, `tfs`, `none`, `custom`
- [ ] Workflow (if Git) is one of: `github-flow`, `gitflow`, `trunk-based`, `custom`, `none`
- [ ] Details field populated if custom/complex setup
- [ ] Adaptations section includes: `artifact_format`, `terminology`, `commit_style`

### Logic Validation

- [ ] If type=`none`, workflow should be `none`
- [ ] If type=`git`, workflow should not be `none`
- [ ] If workflow=`custom`, details field should be populated
- [ ] If auto-detected, confidence_score should exist

### Timestamp Validation

- [ ] `configured_at` is valid ISO 8601 timestamp
- [ ] `cache_valid_until` is 7 days after `configured_at`
- [ ] Both timestamps are in UTC

## Troubleshooting Checklist

If issues occur:

### Detection Issues

- [ ] **Low confidence**: Fall back to manual selection
- [ ] **Fresh repo**: Skip detection, use manual selection
- [ ] **Migration detected**: Ask user which workflow to use
- [ ] **Non-Git repo**: Skip detection, ask for VCS type

### Configuration Issues

- [ ] **Write fails**: Use in-memory config, warn user
- [ ] **Invalid YAML**: Re-create with default values
- [ ] **Missing directory**: Create `.bmad-core/` automatically
- [ ] **Permission denied**: Instruct user to fix permissions

### User Confusion

- [ ] **Unclear options**: Provide more detailed descriptions
- [ ] **Not sure**: Trigger clarifying questions
- [ ] **Complex setup**: Allow free-text description
- [ ] **Multiple VCS**: Ask component-specific questions

## Re-Configuration Checklist

When updating existing configuration:

### Trigger Scenarios

- [ ] User explicitly requests change
- [ ] Cache expired (>7 days old)
- [ ] Detected workflow change (migration)
- [ ] Configuration file corrupted/invalid

### Update Process

- [ ] Show current configuration
- [ ] Ask reason for update
- [ ] Run through discovery again (faster path)
- [ ] Preserve user's custom details if applicable
- [ ] Update timestamps

### Verification

- [ ] New configuration saved
- [ ] Old configuration backed up (optional)
- [ ] All agents recognize new configuration
- [ ] User confirmed update

## Success Criteria

Setup is complete when:

- ✅ Configuration file exists and valid
- ✅ User confirmed workflow selection
- ✅ All agents can read configuration
- ✅ User understands adaptations
- ✅ Cache expiry set correctly
- ✅ No errors or warnings

## Related Files

- [Instructions](./instructions.md) - Detailed workflow steps
- [Workflow Definition](./workflow.yaml) - Machine-readable workflow
- [Discovery Task](../../tasks/discover-vcs.md) - Implementation details
