# VCS-Agnostic Principles for BMAD

## Core Philosophy

**"Optimized for the majority, open to all"**

BMAD adapts to teams' existing version control practices rather than imposing new ones. We recognize that ~85-90% use Git, but remain fully functional for those who don't.

## The 10 Principles

### 1. Discovery Before Assumption

- Always ask about VCS approach first
- Never assume Git or any specific system
- Respect "no VCS" as a valid choice

### 2. Optimize for the Common Case

- Provide quick picks for Git workflows (~85-90% of users)
- Make popular choices easy to select
- Keep edge cases possible but not prominent

### 3. Adapt Language to Context

- Git users: "commit", "branch", "merge"
- SVN users: "revision", "trunk", "update"
- No VCS: "package", "version", "deliverable"
- Generic: "save changes", "workspace", "integrate"

### 4. Structure Follows Function

- GitHub Flow: Small, PR-sized artifacts
- GitFlow: Version-oriented documentation
- Trunk-Based: Flag-gated increments
- No VCS: Monolithic, dated packages

### 5. Respect Existing Workflows

- Document their process, don't change it
- Work within their constraints
- Enhance, don't replace

### 6. Practical Over Theoretical

- Suggest only when asked
- Provide what works, not what's "best"
- Focus on delivery, not process

### 7. Progressive Disclosure

- Simple choices for majority upfront
- Complex options available but hidden
- Custom escape hatch always present

### 8. Context-Aware Generation

- Architecture adapts to VCS choice
- Stories sized for their workflow
- Documentation matches their practices

### 9. Terminology Consistency

- Once VCS is identified, use their terms throughout
- Don't mix Git and SVN terminology
- Be consistent within a project

### 10. Zero Friction Adoption

- Work with what they have
- No required process changes
- Value delivery over methodology

## Implementation Guidelines

### For Agent Developers

#### DO:

- Check for VCS configuration early
- Load appropriate adaptation templates
- Use conditional logic based on VCS type
- Provide examples for different systems
- Test with non-Git users

#### DON'T:

- Hardcode Git commands
- Assume branches exist
- Force commit message formats
- Require specific tools
- Judge non-standard approaches

### For BMAD Users

#### What to Expect:

- Initial question about your VCS
- Adapted terminology and workflows
- Artifacts that fit your process
- Respect for your existing practices
- No forced "improvements"

#### How to Get Best Results:

- Be clear about your VCS setup
- Describe custom workflows if needed
- Ask for clarification if unsure
- Request changes if something doesn't fit

## Configuration Storage

VCS configuration is stored in `.bmad-core/vcs-config.yaml`:

```yaml
vcs_config:
  type: git|svn|perforce|none|custom
  workflow: github-flow|gitflow|trunk-based|custom|none
  details: 'Custom description if provided'

  adaptations:
    artifact_format: branches|monolithic|platform-specific
    terminology: git|svn|generic|custom
    commit_style: conventional|team-specific|none
```

## Testing Checklist

Verify BMAD works correctly with:

- [ ] Git + GitHub Flow
- [ ] Git + GitFlow
- [ ] Git + Trunk-Based
- [ ] Git + Custom workflow
- [ ] SVN
- [ ] Perforce
- [ ] No VCS
- [ ] Mixed/Complex setup

## Success Metrics

- 80% of users select from predefined options
- 20% custom cases handled gracefully
- Zero Git assumptions for non-Git users
- No friction from VCS differences
- Positive feedback from diverse teams

## Evolution Path

As version control evolves:

1. Add new templates for emerging patterns
2. Update terminology mappings
3. Maintain backward compatibility
4. Never remove support for "legacy" systems
5. Keep "no VCS" option always available

## Conclusion

VCS-agnosticism makes BMAD truly universal. By respecting teams' existing practices and adapting to their workflows, BMAD becomes a tool that enhances productivity without forcing change.

The goal is simple: **Make BMAD work with whatever the team has, not force the team to work with what BMAD expects.**
