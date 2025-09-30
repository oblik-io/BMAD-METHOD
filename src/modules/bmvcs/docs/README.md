# BMVCS Documentation

Version Control System (VCS) Agnostic Module for BMAD-METHOD

## Overview

BMVCS enables BMAD agents to adapt to any version control system - from Git workflows to SVN, Perforce, or even no VCS at all.

## Core Documents

### [VCS_AGNOSTIC_PRINCIPLES.md](./VCS_AGNOSTIC_PRINCIPLES.md)

The foundational philosophy: "Optimized for the majority, open to all"

- 10 core principles for VCS adaptation
- Implementation guidelines for agent developers
- Configuration storage and testing

### [VCS_AGNOSTIC_PROPOSAL.md](./VCS_AGNOSTIC_PROPOSAL.md)

The practical implementation approach: "BMAD Suggests, User Decides"

- VCS discovery protocol
- Agent behavioral adaptations
- Example interactions and scenarios

### [VCS_DETECTION_CONFIDENCE.md](./VCS_DETECTION_CONFIDENCE.md)

Auto-detection confidence scoring: "Detection as a HINT, not a DECISION"

- Workflow detection algorithms
- Confidence score calculation
- Edge cases and migration handling

## Quick Start

1. **Discovery**: BMAD asks about your VCS at project start
2. **Adaptation**: All agents adapt their output to your workflow
3. **Flexibility**: Change VCS settings anytime via configuration

## Philosophy

BMAD adapts to teams' existing version control practices rather than imposing new ones:

- ~85-90% use Git → Quick-pick Git workflows
- ~10-15% use other systems → Full support with appropriate terminology
- No VCS needed → Self-contained deliverables

## Key Features

- **No Assumptions**: Never assumes Git or any specific VCS
- **Terminology Adaptation**: Uses your VCS language (commit/changelist/revision)
- **Workflow Respect**: Honors existing team processes
- **Progressive Disclosure**: Simple for common cases, flexible for edge cases

## Integration

BMVCS integrates with all BMAD agents:

- **Architect**: VCS-adapted architecture documents
- **PM**: VCS-appropriate requirements
- **SM**: Stories sized for your workflow
- **Dev**: Code delivery matching your VCS
- **QA**: Test plans aligned with your process

## Configuration

VCS settings stored in `.bmad-core/vcs-config.yaml`

See [VCS_AGNOSTIC_PRINCIPLES.md](./VCS_AGNOSTIC_PRINCIPLES.md#configuration-storage) for details.

## Related

- [Module README](../README.md) - BMVCS module overview
- [Discovery Task](../tasks/discover-vcs.md) - VCS discovery implementation
- [VCS Templates](../templates/vcs-adaptations/) - Workflow adaptation templates
