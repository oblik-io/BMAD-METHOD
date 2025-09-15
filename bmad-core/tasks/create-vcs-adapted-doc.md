# Create VCS-Adapted Document Task

## Purpose

Adapt architecture and other documents based on the team's version control system configuration.

## Prerequisites

- VCS configuration must exist in `.bmad-core/vcs-config.yaml`
- If not, run `discover-vcs.md` task first

## Task Instructions

### Step 1: Load VCS Configuration

```yaml
load_config:
  file: .bmad-core/vcs-config.yaml
  fallback:
    if_missing: 'Execute discover-vcs.md task first'
```

### Step 2: Load Appropriate VCS Template

Based on `vcs_config.workflow`:

- `github-flow` → Load `vcs-adaptations/git-github-flow.yaml`
- `gitflow` → Load `vcs-adaptations/git-gitflow.yaml`
- `trunk-based` → Load `vcs-adaptations/git-trunk-based.yaml`
- `none` → Load `vcs-adaptations/no-vcs.yaml`
- `custom` or other → Load `vcs-adaptations/custom-generic.yaml`

### Step 3: Apply Adaptations to Document

#### For Architecture Documents:

**If Git-based (GitHub Flow/GitFlow/Trunk):**

```yaml
adaptations:
  structure:
    - Include branch strategy section
    - Add CI/CD pipeline considerations
    - Reference commit conventions

  terminology:
    - Use Git terminology (branch, commit, merge)
    - Include PR/MR workflow details
```

**If No VCS:**

```yaml
adaptations:
  structure:
    - Single comprehensive document
    - Date-based versioning
    - All diagrams embedded

  terminology:
    - Avoid version control terms
    - Focus on deliverables
```

**If Custom VCS:**

```yaml
adaptations:
  structure:
    - Ask user for preferred format
    - Mirror their documentation style

  terminology:
    - Use their VCS terminology
    - Avoid Git-specific references
```

### Step 4: Document Sections Based on VCS

#### GitHub Flow Additions:

```markdown
## Development Workflow

- Feature branches from main
- Pull requests for review
- Continuous deployment after merge

## Architecture Decisions per Feature

- Lightweight ADRs in feature branches
- Architecture evolves with each PR
```

#### GitFlow Additions:

```markdown
## Release Architecture

- Version-specific considerations
- Migration paths between versions
- Hotfix procedures

## Branch-Specific Components

- Features in development
- Release candidates
- Production hotfixes
```

#### Trunk-Based Additions:

```markdown
## Feature Flag Architecture

- Flag-gated components
- Progressive rollout strategy
- Flag retirement plan

## Continuous Architecture

- Small, incremental changes
- Always-deployable state
```

#### No VCS Additions:

```markdown
## Complete Package Contents

- All source code included
- Setup instructions
- No external dependencies

## Delivery Structure

- Single ZIP/folder
- Date-stamped versions
```

### Step 5: Adapt Language and Recommendations

Based on VCS type, adjust:

- Deployment strategies
- Testing approaches
- Documentation structure
- Team collaboration patterns

## Output Format

The adapted document should:

1. Respect the team's existing VCS practices
2. Use appropriate terminology
3. Structure content for their workflow
4. Include VCS-specific best practices
5. Avoid imposing foreign concepts

## Success Criteria

- Document aligns with team's VCS workflow
- No Git assumptions for non-Git users
- Practical, actionable guidance
- Respects existing team processes
