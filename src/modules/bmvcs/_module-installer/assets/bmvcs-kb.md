# BMVCS Knowledge Base Content

## Optional Modules

BMAD-METHOD™ includes optional modules that extend core functionality for specific use cases. These modules are available during installation or can be added later as needed.

### BMVCS: Version Control Suite

#### What is BMVCS?

BMVCS (BMad Version Control Suite) makes BMAD universal by adapting to **any version control system**. Instead of assuming Git or forcing workflow changes, BMVCS discovers your existing practices and adjusts BMAD's output accordingly.

**Core Philosophy**: "Optimize for the majority, open to all"

- 85-90% of teams use Git → Quick picks for common workflows (GitHub Flow, GitFlow, Trunk-Based)
- 10-15% use other VCS or no VCS → Fully supported with specialized adaptations
- Respects existing workflows - enhances, doesn't replace

#### When to Use BMVCS

**Use BMVCS when:**

- Working with **non-Git VCS** systems (SVN, Perforce, Mercurial, TFS)
- Using **no version control** (freelancers, consultants, isolated projects)
- Managing **custom or proprietary** VCS workflows
- Supporting **multi-VCS teams** across different projects

**Skip BMVCS when:**

- Standard Git with GitHub Flow (BMAD already optimized for this)
- Single VCS across all projects with standard practices

#### Quick Start

```bash
# 1. Install module
npx bmad-method install
# Select "BMVCS: Version Control Suite" from module list

# 2. Run VCS discovery
# Activate VCS Adapter agent and run discovery command
*discover

# 3. Adapt documents to your workflow
*adapt-doc docs/architecture.md
```

**Discovery creates** `.bmad/vcs-config.yaml` with your workflow adaptations.

#### VCS-Aware Agents

When BMVCS is installed, these agents gain VCS-aware capabilities:

| Agent         | VCS Enhancement                                  |
| ------------- | ------------------------------------------------ |
| `vcs-adapter` | Discovery, adaptation, validation (BMVCS agent)  |
| `architect`   | VCS-adapted architecture docs, branch strategies |
| `pm`          | Workflow-aware planning, release sizing          |
| `dev`         | VCS-specific commit messages, naming conventions |

**Integration**: BMVCS is **optional** - BMM works without BMVCS, BMVCS works standalone.

#### Supported VCS Systems

| VCS Type      | Workflows                                 | Status       |
| ------------- | ----------------------------------------- | ------------ |
| **Git**       | GitHub Flow, GitFlow, Trunk-Based, Custom | ✅ Supported |
| **SVN**       | Trunk/Branches                            | ✅ Supported |
| **Perforce**  | Streams, Classic                          | ✅ Supported |
| **Mercurial** | Generic                                   | ✅ Supported |
| **TFS/TFVC**  | Generic                                   | ✅ Supported |
| **No VCS**    | Date-based deliverables                   | ✅ Supported |
| **Custom**    | User-defined                              | ✅ Supported |

#### Workflow Adaptations

BMVCS automatically adapts BMAD output to match your VCS workflow:

- **Terminology**: Git users get "commit/branch", SVN users get "revision/trunk"
- **Artifact Size**: GitHub Flow = small PRs, No VCS = monolithic packages
- **Documentation**: Branch strategy, CI/CD considerations, commit conventions
- **Templates**: Workflow-specific examples and best practices

**Example**: GitHub Flow generates feature-branch architecture with PR workflow. GitFlow generates release-branch strategy with hotfix process. No VCS generates self-contained delivery packages with date versioning.

#### Learn More

- **Full Documentation**: `src/modules/bmvcs/README.md`
- **VCS Principles**: `src/modules/bmvcs/docs/VCS_AGNOSTIC_PRINCIPLES.md`
- **Examples**: `src/modules/bmvcs/examples/vcs-adaptation-examples.md`
- **Templates**: `src/modules/bmvcs/templates/vcs-adaptations/`
