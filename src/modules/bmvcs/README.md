# BMVCS: BMad Version Control Suite

**Status:** 🚧 In Development (v6-alpha)

> Make BMAD adapt to your version control workflow, not the other way around.

---

## 🎯 What is BMVCS?

**BMVCS** (BMad Version Control Suite) is an optional module that makes BMAD truly universal by adapting to any version control system. Instead of assuming Git or forcing workflow changes, BMVCS discovers your existing practices and adjusts BMAD's output accordingly.

### Core Philosophy

**"Optimize for the majority, open to all"**

- ~85-90% of teams use Git → Quick picks for common Git workflows
- ~10-15% use other VCS or no VCS → Fully supported, never forced to change
- **Respect existing workflows** - Enhance, don't replace

---

## ✨ Features

### 🔍 VCS Discovery

Interactive detection of your version control system:

- **Git workflows:** GitHub Flow, GitFlow, Trunk-Based Development
- **Other VCS:** SVN, Perforce, Mercurial, TFS
- **No VCS:** Self-contained deliverables with date versioning
- **Custom:** Team-specific workflows

### 📝 Workflow Adaptation

Automatically adapts BMAD output to your workflow:

- **Terminology:** Git users get "commit/branch", SVN users get "revision/trunk"
- **Artifact size:** GitHub Flow = small PRs, No VCS = monolithic packages
- **Documentation:** Branch strategy, CI/CD considerations, commit conventions

### 🔧 VCS Adapter Agent

Specialized agent for version control integration:

- Commands: `*discover`, `*adapt-doc`, `*show-config`, `*validate`
- Works standalone or integrates with BMM agents
- Optional dependency - BMM works without BMVCS

---

## 📦 Installation

### via BMad Method Installer

```bash
npx bmad-method install
# Select "BMVCS: Version Control Suite" from the module list
```

### Manual Installation

```bash
# Copy module to your project
cp -r src/modules/bmvcs {project-root}/bmad/bmvcs

# Run VCS discovery
# (activate VCS Adapter agent and run *discover command)
```

---

## 🚀 Quick Start

### 1. Run VCS Discovery

```bash
# Activate VCS Adapter agent
# Run: *discover

# Interactive prompts will guide you through:
# - What VCS you use (Git/SVN/Perforce/None/Custom)
# - Your Git workflow (if applicable)
# - Team preferences and constraints
```

### 2. VCS Configuration Created

Discovery saves configuration to `.bmad/vcs-config.yaml`:

```yaml
vcs_config:
  type: git
  workflow: github-flow

  adaptations:
    artifact_format: branches
    terminology: git
    commit_style: conventional
```

### 3. Adapt Documents

```bash
# Activate VCS Adapter agent
# Run: *adapt-doc architecture.md

# Document will be adapted to your VCS workflow:
# - GitHub Flow: Feature branch strategy, PR workflow
# - GitFlow: Release branches, hotfix process
# - No VCS: Monolithic delivery, date versioning
```

---

## 🔗 Integration with BMM

BMVCS integrates optionally with BMM (BMad Method) agents:

### Architect Agent

- VCS-adapted architecture documents
- Branch strategy recommendations
- CI/CD pipeline considerations

### PM Agent

- VCS-aware project planning
- Release planning adapted to workflow
- Story sizing for workflow

### Dev Agent

- VCS-adapted commit messages
- Workflow-specific conventions
- Branch naming patterns

**Note:** Integration is **optional** - BMM works without BMVCS, BMVCS works without BMM.

---

## 📚 Documentation

- **[VCS Agnostic Principles](./docs/VCS_AGNOSTIC_PRINCIPLES.md)** - Philosophy and approach
- **[VCS Agnostic Proposal](./docs/VCS_AGNOSTIC_PROPOSAL.md)** - Detailed implementation design
- **[VCS Detection Confidence](./docs/VCS_DETECTION_CONFIDENCE.md)** - How discovery scoring works
- **[Usage Examples](./examples/vcs-adaptation-examples.md)** - Practical examples

---

## 🎯 Supported VCS Systems

| VCS Type      | Workflows                                 | Status       |
| ------------- | ----------------------------------------- | ------------ |
| **Git**       | GitHub Flow, GitFlow, Trunk-Based, Custom | ✅ Supported |
| **SVN**       | Trunk/Branches                            | ✅ Supported |
| **Perforce**  | Streams, Classic                          | ✅ Supported |
| **Mercurial** | Generic                                   | ✅ Supported |
| **TFS/TFVC**  | Generic                                   | ✅ Supported |
| **No VCS**    | Date-based deliverables                   | ✅ Supported |
| **Custom**    | User-defined                              | ✅ Supported |

---

## 🧪 Module Structure

```
src/modules/bmvcs/
├── agents/
│   └── vcs-adapter.md           # VCS Adapter agent
├── tasks/
│   ├── discover-vcs.md          # Interactive VCS discovery
│   ├── create-vcs-adapted-doc.md # Document adaptation
│   └── validate-vcs-config.md   # Config validation
├── templates/
│   └── vcs-adaptations/
│       ├── git-github-flow.yaml
│       ├── git-gitflow.yaml
│       ├── git-trunk-based.yaml
│       ├── no-vcs.yaml
│       └── custom-generic.yaml
├── workflows/
│   └── setup-vcs/               # Initial VCS setup workflow
├── docs/                        # Documentation
└── README.md                    # This file
```

---

## 📚 Documentation

- **[VCS Agnostic Principles](./docs/VCS_AGNOSTIC_PRINCIPLES.md)** - Philosophy and approach
- **[VCS Agnostic Proposal](./docs/VCS_AGNOSTIC_PROPOSAL.md)** - Detailed implementation design
- **[VCS Detection Confidence](./docs/VCS_DETECTION_CONFIDENCE.md)** - How discovery scoring works
- **[Usage Examples](./examples/vcs-adaptation-examples.md)** - Practical examples

---

## 🤝 Contributing

BMVCS is part of the BMAD Method project. See [CONTRIBUTING.md](../../../CONTRIBUTING.md) for guidelines.

### Adding New VCS Support

1. Add template in `templates/vcs-adaptations/`
2. Update `discover-vcs.md` task with new prompts
3. Test with real projects using that VCS
4. Submit PR with examples

---

## 📝 License

Same license as BMAD Method project.

---

## 🔗 Links

- **BMAD Method:** <https://github.com/bmad-code-org/BMAD-METHOD>
- **Issue Tracker:** <https://github.com/bmad-code-org/BMAD-METHOD/issues>
- **Discord:** <https://discord.gg/gk8jAdXWmj>

---

**Version:** 6.0.0-alpha
**Status:** In Development
**Module Code:** `bmvcs`
