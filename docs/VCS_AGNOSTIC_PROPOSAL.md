# VCS-Agnostic Approach for BMAD-METHOD

## Core Philosophy: "BMAD Suggests, User Decides"

### Executive Summary

BMAD should adapt to existing team practices rather than impose specific version control strategies. This proposal outlines a flexible, discovery-based approach to VCS integration.

## The Problem with Current Assumptions

Current BMAD and the Gemini analysis document assume:

- All projects use Git
- Teams need "best practice" workflows
- Version control strategy is primarily technical

Reality:

- Many teams have unique, working systems
- Some projects don't need VCS at all
- VCS choice is often organizational/political, not technical

## Proposed Solution: VCS Discovery Protocol

### 1. Initial Discovery Question

```yaml
vcs_discovery:
  initial_question: 'How does your team manage code versions?'

  response_paths:
    established_system:
      - 'We have our own system that works'
      - BMAD: 'Great! Tell me about it so I can adapt'

    no_vcs:
      - "We don't use version control"
      - BMAD: "Understood. I'll generate self-contained packages"

    need_guidance:
      - 'We need recommendations'
      - BMAD: 'Let me understand your context first...'
```

### 2. Adaptation Matrix

| User Response               | BMAD Adaptation                                       |
| --------------------------- | ----------------------------------------------------- |
| "Custom Git workflow"       | Agents use generic Git terms, no strategy assumptions |
| "No VCS (prototype)"        | Single deliverable packages with date versioning      |
| "Platform VCS (Salesforce)" | Platform-specific artifacts and terminology           |
| "Legacy system (SVN)"       | VCS-agnostic artifacts, no Git-specific features      |
| "It's complicated..."       | Free-form description, custom adaptation              |

### 3. Agent Behavioral Adaptations

#### Architect Agent

```yaml
vcs_adaptations:
  no_vcs:
    - Generate monolithic architecture document
    - Include all specs in single package
    - Version via: PROJECTNAME_ARCH_YYYYMMDD.md

  custom_vcs:
    - Ask: 'What format works with your system?'
    - Avoid Git-specific terminology
    - Focus on deliverables, not process
```

#### Developer Agent

```yaml
vcs_adaptations:
  no_vcs:
    - Generate complete code blocks
    - No commit message suggestions
    - Package as: FEATURE_COMPLETE_YYYYMMDD.zip

  custom_vcs:
    - Ask: 'How should I structure code changes?'
    - Follow team's existing patterns
```

#### SM Agent

```yaml
vcs_adaptations:
  no_vcs:
    - Create comprehensive story documents
    - Include all context in each story

  git_based:
    - Option to create branch-scoped stories
    - But only if team requests it
```

## Implementation Steps

### Phase 1: Discovery Mechanism

Create `bmad-core/tasks/discover-vcs.md`:

- Non-assumptive questions
- Multiple response paths
- Custom description option

### Phase 2: Adaptation Templates

Create `bmad-core/templates/vcs-adaptations/`:

- `no-vcs.yaml`
- `git-agnostic.yaml`
- `platform-specific.yaml`
- `custom-adapter.yaml`

### Phase 3: Agent Updates

Modify each agent to:

1. Check VCS context before generating artifacts
2. Adapt output format based on VCS choice
3. Never assume Git unless confirmed

## Key Principles

1. **No Assumptions**: Never assume Git or any specific VCS
2. **Respect Existing**: Honor teams' current working systems
3. **Adapt, Don't Educate**: We adapt to them, not vice versa
4. **Suggest When Asked**: Only provide recommendations when requested
5. **Custom is Valid**: "Our own way" is a perfectly valid answer

## Example Interactions

### Scenario 1: Team with Custom Process

```
BMAD: "How does your team manage code versions?"
User: "We use Git but with our own branching model based on features and environments"
BMAD: "Perfect! I'll adapt to your model. Could you briefly describe when code moves between environments?"
User: [describes their process]
BMAD: "Got it. I'll structure artifacts to align with your feature→environment flow"
```

### Scenario 2: No VCS Needed

```
BMAD: "How does your team manage code versions?"
User: "This is a one-time data migration script, no versioning needed"
BMAD: "Understood. I'll generate a single, complete package with clear documentation"
```

### Scenario 3: Guidance Requested

```
BMAD: "How does your team manage code versions?"
User: "We're not sure, what do you recommend?"
BMAD: "Let me understand your context first:
- How many developers?
- How often do you release?
- Is this a new project or existing codebase?"
[After answers]
BMAD: "Based on your context, here are 2 options that could work..."
```

## Success Metrics

- Zero assumptions about Git in initial interactions
- Successful adaptation to 10+ different VCS approaches
- No forced "best practices" unless requested
- Positive feedback from teams with non-standard processes

## Anti-Patterns to Avoid

❌ "You should use Trunk-Based Development"
❌ "Git is the industry standard"
❌ "Your process could be improved by..."
❌ Generating Git-specific artifacts without confirmation
❌ Assuming branches exist

## Conclusion

BMAD's strength lies in adaptation, not prescription. By adopting a truly VCS-agnostic approach, BMAD becomes useful to ALL teams, regardless of their version control choices or lack thereof.

The goal: Make BMAD work with whatever the team has, not force the team to work with what BMAD expects.
