# BMVCS Examples

Practical examples demonstrating VCS-agnostic adaptation in BMAD.

## Files in This Directory

### [vcs-adaptation-examples.md](./vcs-adaptation-examples.md)

**Real-world scenarios** showing how BMAD adapts to different VCS workflows:

- **Startup with GitHub Flow**: Fast-paced web development
- **Enterprise with GitFlow**: Structured releases with versions
- **No Version Control**: One-time scripts and prototypes
- **Custom SVN Workflow**: Legacy system adaptation
- **Trunk-Based with Feature Flags**: Continuous deployment
- **Complex Multi-VCS Setup**: Mixed systems in one organization

Each example shows discovery dialogue, BMAD adaptations, and generated artifacts.

### [vcs-detection-implementation.py](./vcs-detection-implementation.py)

**Reference implementation** of Git workflow auto-detection:

- Analyzes repository history to detect workflow patterns
- Calculates confidence scores for GitFlow, GitHub Flow, and Trunk-Based
- Follows "Detection as a HINT, not a DECISION" principle
- Interactive confirmation with evidence presentation
- Handles edge cases (migration, unclear patterns, fresh repos)

**Note**: This is an example implementation in Python. The actual BMAD implementation may use JavaScript/TypeScript. This demonstrates the detection logic that can be adapted to any language.

## Usage

### Running the Detector Example

```bash
cd /path/to/your/git/repo
python /path/to/vcs-detection-implementation.py
```

The script will:

1. Analyze your Git history
2. Score workflow indicators
3. Present detection results with evidence
4. Ask for confirmation (never auto-decides)
5. Save configuration to `.bmad/vcs_config.json`

### Understanding the Examples

The adaptation examples show specific output for each workflow type. Use them as:

- **Reference**: See how BMAD should adapt terminology and structure
- **Templates**: Copy patterns for custom integrations
- **Documentation**: Explain VCS-agnostic behavior to users

## Key Principles Demonstrated

1. **Discovery First**: Always ask, never assume
2. **Evidence-Based**: Show detection reasoning transparently
3. **User Confirmation**: Detection is advisory, not prescriptive
4. **Graceful Fallback**: Handle unclear cases with questions
5. **Respect Existing**: Adapt to their workflow, don't change it

## Integration with BMAD Agents

These examples inform how all BMAD agents should adapt:

- **Architect**: Generate VCS-appropriate architecture docs
- **PM**: Create requirements matching workflow style
- **SM**: Size stories for the team's release cadence
- **Dev**: Suggest VCS-appropriate code delivery
- **QA**: Align test plans with workflow gates

## Further Reading

- [VCS Agnostic Principles](../docs/VCS_AGNOSTIC_PRINCIPLES.md)
- [Detection Confidence Scoring](../docs/VCS_DETECTION_CONFIDENCE.md)
- [Discovery Task Implementation](../tasks/discover-vcs.md)
