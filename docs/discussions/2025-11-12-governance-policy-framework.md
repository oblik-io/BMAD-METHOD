# BMAD-METHOD Governance Policy Framework - Discussion

**Date:** 2025-11-12 19:30:00 EET
**Context:** Planning organizational structure and policies for BMAD-METHOD adoption
**Status:** 🔍 Discussion Phase - Theoretical Planning
**Related:** [Production Process Improvements](./2025-11-12-production-process-improvements.md)

---

## Executive Summary

Планування політики та структури для використання та розвитку BMAD-METHOD через три організації GitHub: @joyshmitz (особистий), felectra (тимчасова), та oblik.io (головна).

**Key Outcome:**

- ✅ Визначено three-tier architecture (Upstream → Organization → Project)
- ✅ Розроблено governance policy для кожної організації
- ✅ Запропоновано automated enforcement через CI/CD
- ⏳ Потрібно обдумати та прийняти рішення перед міграцією

---

## Problem Statement

### Поточна ситуація

**Організації:**

- **@joyshmitz** - особистий GitHub (експерименти, learning)
- **felectra** - тимчасова організація (KRTM проєкт, приватний репо)
- **oblik.io** - головна організація (планується розвертати BMAD-METHOD)

**Проблеми:**

1. ❌ Fork живе в `felectra/BMAD-METHOD` (wrong organization)
2. ❌ Немає чіткої ієрархії та separation of concerns
3. ❌ Відсутня політика для contribution, sync, versioning
4. ❌ Mixing project-specific (KRTM) з general-purpose tooling

### Бажаний стан

```
Upstream (bmad-code-org)
    ↓
oblik.io (org fork + bundles)
    ↓
Projects (krtm, project-x) через submodules
```

---

## Proposed Architecture

### Three-Tier Architecture

```
┌─────────────────────────────────────────────────────────────┐
│ TIER 1: UPSTREAM (bmad-code-org/BMAD-METHOD)               │
│ - Source of truth                                            │
│ - Contribute back improvements via PRs                       │
└─────────────────────────────────────────────────────────────┘
                            ↓ fetch/sync
┌─────────────────────────────────────────────────────────────┐
│ TIER 2: ORGANIZATIONAL FORK (oblik.io)                      │
│ - oblik.io/BMAD-METHOD (main fork)                          │
│ - oblik.io/bmad-bundles (distribution)                      │
│ - Custom agents, methods, workflows                          │
│ - Verification & approval layer                              │
└─────────────────────────────────────────────────────────────┘
                            ↓ consume
┌─────────────────────────────────────────────────────────────┐
│ TIER 3: PROJECT-SPECIFIC (krtm, project-x)                 │
│ - .bmad/ (git submodule → oblik.io/bmad-bundles)           │
│ - Project-specific customizations only                      │
│ - Version locked, controlled updates                         │
└─────────────────────────────────────────────────────────────┘
```

---

## Organization Policies

### 1. @joyshmitz (Personal Account)

**РОЛЬ:** Experimentation & Contribution Playground

**ЩО ТРИМАТИ:**

- ✅ Temporary forks для contribution в upstream
- ✅ Особисті експерименти (POCs, learning)
- ✅ Sandboxes, testing environments

**ЩО НЕ ТРИМАТИ:**

- ❌ Production forks
- ❌ Team/org shared code
- ❌ Long-term maintained forks

**WORKFLOW:**

```bash
# Для contribution в upstream:
gh repo fork bmad-code-org/BMAD-METHOD --clone
cd BMAD-METHOD
git checkout -b feature/my-contribution
# ... робота ...
gh pr create --repo bmad-code-org/BMAD-METHOD

# Після merge PR → видалити fork
gh repo delete joyshmitz/BMAD-METHOD --yes
```

**LIFECYCLE:** Short-lived (дні/тижні), не більше

---

### 2. felectra (Temporary Organization)

**РОЛЬ:** KRTM Project Temporary Home

**ПОТОЧНИЙ СТАН:**

- `felectra/krtm` (приватний проєкт) ✅
- `felectra/BMAD-METHOD` (fork) ❌ WRONG PLACE!

**ЩО ТРИМАТИ:**

- ✅ `felectra/krtm` (тимчасово, поки проєкт активний)
- ✅ KRTM-specific code

**ЩО НЕ ТРИМАТИ:**

- ❌ `felectra/BMAD-METHOD` (перенести в oblik.io)
- ❌ Reusable tooling (має бути в oblik.io)
- ❌ General-purpose infrastructure

**ПІСЛЯ ЗАВЕРШЕННЯ KRTM:**

- Архівувати `felectra/krtm`
- Доступ через oblik.io owners
- Reusable assets → oblik.io

---

### 3. oblik.io (Main Organization)

**РОЛЬ:** Production Fork & Innovation Hub

**СТРУКТУРА РЕПОЗИТОРІЇВ:**

```
oblik-io/
├── BMAD-METHOD (fork)          # Main controlled fork
├── bmad-bundles                # Distribution repo (GitHub Pages)
├── oblik-agents                # Custom oblik.io agents
├── oblik-workflows             # Custom workflows
└── [project repos consume via submodules]
```

#### A. oblik-io/BMAD-METHOD

**Purpose:** Controlled fork з upstream verification

**Branch Strategy:**

```
main                    # Mirror upstream/main (read-only)
├── oblik/stable       # Tested, approved for production
├── oblik/develop      # Integration для custom features
└── feature/*          # Development branches
```

**Sync Policy:**

```yaml
Automated:
  - Daily sync check (6am UTC)
  - Auto-merge: patch versions, non-breaking changes

Manual Approval Required:
  - Minor version bumps
  - Breaking changes
  - Security-sensitive updates
```

**Branch Protection:**

- `main` - read-only, тільки fast-forward від upstream
- `oblik/stable` - requires 1 approval
- `oblik/develop` - requires 2 approvals від core team

#### B. oblik-io/bmad-bundles

**Purpose:** Trusted distribution point з verification

**Structure:**

```
bmad-bundles/
├── upstream/          # Verified upstream bundles
│   ├── bmm/
│   ├── bmb/
│   └── cis/
├── oblik/             # Custom oblik.io bundles
│   ├── agents/
│   └── workflows/
└── versions/          # Tagged, immutable versions
    ├── v1.0.0/
    ├── v1.1.0/
    └── latest/
```

**Distribution URLs:**

```
Stable:   https://oblik-io.github.io/bmad-bundles/stable/
Latest:   https://oblik-io.github.io/bmad-bundles/latest/
Custom:   https://oblik-io.github.io/bmad-bundles/oblik/
```

**Verification Workflow:**

```yaml
Schedule: Weekly (Monday 2am)

Steps: 1. Fetch upstream bundles
  2. Run validation tests
  3. Security scan (npm audit, SAST)
  4. Create verification report
  5. Auto-merge if PASS + no breaking
  6. Create PR if FAIL or breaking changes
  7. Publish to GitHub Pages
```

#### C. oblik-io/oblik-agents (Optional)

**Purpose:** Custom agents не для upstream

**Приклади:**

- oblik-specific business logic
- Internal automation
- Experimental features (not ready for upstream)

---

## Project-Level Integration

### Кожен проєкт (KRTM, project-x)

**Structure:**

```
project-root/
├── .bmad/                     # Git submodule → oblik-io/bmad-bundles
│   ├── config.yaml
│   └── [bundles content]
├── .bmad-local/               # Project-specific (gitignored)
│   ├── custom-agents/
│   └── experiments/
└── .bmad.lock                 # Version lock file
```

**Setup:**

```bash
cd project-root
git submodule add https://github.com/oblik-io/bmad-bundles.git .bmad
echo ".bmad-local/" >> .gitignore

# Lock to specific version
cat > .bmad.lock <<EOF
version: "v1.2.3"
source: "oblik-io/bmad-bundles"
verified: "2025-11-12T15:30:00Z"
checksum: "sha256:abc123..."
EOF
```

**Update Policy:**

```bash
# Check for updates
cd .bmad && git fetch && git tag -l

# Update (requires approval для production)
git checkout v1.3.0
cd .. && git add .bmad .bmad.lock
git commit -m "chore: update bmad-bundles to v1.3.0"

# Production projects - requires review
```

---

## Governance Matrix

### Responsibility Matrix

```
┌─────────────────────────┬──────────┬──────────┬──────────┐
│ Action                  │ Personal │ felectra │ oblik.io │
├─────────────────────────┼──────────┼──────────┼──────────┤
│ Fork upstream           │    ✓     │    ✗     │    ✓     │
│ Contribute to upstream  │    ✓     │    ✗     │    ✓     │
│ Create custom agents    │    ✓     │    ✗     │    ✓     │
│ Host bundles (Pages)    │    ✗     │    ✗     │    ✓     │
│ Sync upstream (auto)    │    ✗     │    ✗     │    ✓     │
│ Version locking         │    ✗     │    ✗     │    ✓     │
│ Security scanning       │    ✗     │    ✗     │    ✓     │
└─────────────────────────┴──────────┴──────────┴──────────┘
```

### Approval Matrix

```
┌─────────────────────────┬──────────┬──────────┬──────────┐
│ Update Type             │ Dev Env  │ KRTM     │ Prod     │
├─────────────────────────┼──────────┼──────────┼──────────┤
│ Patch (v1.0.x)          │   Auto   │  Manual  │  Manual  │
│ Minor (v1.x.0)          │   Auto   │  Manual  │  Review  │
│ Major (vx.0.0)          │  Manual  │  Review  │  Review  │
│ Breaking changes        │  Manual  │  Review  │  Decline │
│ Custom oblik agents     │  Manual  │  Review  │  Review  │
└─────────────────────────┴──────────┴──────────┴──────────┘

Roles:
- Auto: Automated approval
- Manual: Single reviewer approval
- Review: 2+ reviewers + discussion
- Decline: Default deny, exceptional cases only
```

---

## Automated Enforcement

### 1. Repository Configuration

**Via Terraform or GitHub API:**

```hcl
# terraform/oblik-io-github.tf

resource "github_repository" "bmad_fork" {
  name        = "BMAD-METHOD"
  description = "Controlled fork of bmad-code-org/BMAD-METHOD"
  visibility  = "public"

  # Branch protection
  branch_protection_rules {
    pattern = "main"

    required_status_checks {
      strict   = true
      contexts = ["sync-check", "policy-check"]
    }

    required_pull_request_reviews {
      required_approving_review_count = 1
      restrict_push_access            = true
    }

    allows_force_pushes = false
  }
}

resource "github_repository" "bmad_bundles" {
  name        = "bmad-bundles"
  description = "Verified BMAD bundles distribution"

  pages {
    source {
      branch = "main"
      path   = "/"
    }
  }

  environments {
    name      = "production"
    reviewers = ["@joyshmitz"]
  }
}
```

### 2. CI/CD Policy Enforcement

**Sync Check Workflow:**

```yaml
# .github/workflows/upstream-sync-check.yaml
name: Upstream Sync Check

on:
  schedule:
    - cron: '0 6 * * *' # Daily 6am UTC
  workflow_dispatch:

jobs:
  check-sync-status:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Check upstream sync
        run: |
          git fetch upstream main

          # Check if main is behind upstream
          BEHIND=$(git rev-list --count HEAD..upstream/main)

          if [[ $BEHIND -gt 0 ]]; then
            echo "⚠️ Main is $BEHIND commits behind upstream"
            echo "::warning::Upstream sync required"
          fi

          # Check if main has diverged
          AHEAD=$(git rev-list --count upstream/main..HEAD)

          if [[ $AHEAD -gt 0 ]]; then
            echo "❌ Main has $AHEAD commits not in upstream"
            echo "::error::Main has diverged from upstream!"
            exit 1
          fi

      - name: Create sync PR if needed
        if: env.BEHIND > 0
        run: |
          gh pr create \
            --title "chore: sync with upstream $(git rev-parse --short upstream/main)" \
            --body "Automated sync from bmad-code-org/BMAD-METHOD" \
            --base main \
            --head upstream-sync
```

**Policy Check Workflow:**

```yaml
# .github/workflows/policy-check.yaml
name: Policy Enforcement

on: [push, pull_request]

jobs:
  check-branch-policy:
    runs-on: ubuntu-latest
    steps:
      - name: Verify branch naming
        run: |
          BRANCH="${{ github.ref_name }}"

          # main = only from upstream
          if [[ "$BRANCH" == "main" ]] && [[ "${{ github.event_name }}" == "push" ]]; then
            if [[ "${{ github.actor }}" != "github-actions[bot]" ]]; then
              echo "❌ Direct push to main not allowed"
              exit 1
            fi
          fi

          # oblik/* must reference issue
          if [[ "$BRANCH" == oblik/* ]]; then
            if ! git log -1 --pretty=%B | grep -qE '#[0-9]+'; then
              echo "❌ oblik/* branches must reference issue number"
              exit 1
            fi
          fi

  check-commit-convention:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Verify conventional commits
        run: |
          MSG=$(git log -1 --pretty=%B)

          if ! echo "$MSG" | grep -qE '^(feat|fix|docs|chore|refactor|test|ci):'; then
            echo "❌ Commit must follow conventional commits"
            echo "   Current: $MSG"
            echo "   Expected: type: description"
            exit 1
          fi
```

**Bundle Verification Workflow:**

```yaml
# oblik-io/bmad-bundles/.github/workflows/verify-publish.yaml
name: Verify and Publish

on:
  schedule:
    - cron: '0 2 * * 1' # Weekly Monday 2am
  workflow_dispatch:

jobs:
  sync-upstream:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Fetch upstream bundles
        run: |
          curl -L https://bmad-code-org.github.io/bmad-bundles/latest/bmm.zip -o upstream.zip
          unzip upstream.zip -d upstream-new/

      - name: Validate bundles
        run: |
          # Schema validation
          npx ajv validate -s schema.json -d 'upstream-new/**/*.xml'

          # Security scan
          npm audit --audit-level=moderate

          # Custom validation
          ./scripts/validate-agents.sh

      - name: Create verification report
        run: |
          cat > VERIFICATION_REPORT.md <<EOF
          # Verification Report

          **Date:** $(date -u +"%Y-%m-%d %H:%M:%S UTC")
          **Upstream Version:** $(cat upstream-new/VERSION)

          ## Checks
          - [x] Schema validation
          - [x] Security scan
          - [x] Custom validation

          ## Approval
          Status: ✅ PASS
          EOF

      - name: Update bundles
        if: success()
        run: |
          rm -rf upstream/
          mv upstream-new/ upstream/
          git add upstream/ VERIFICATION_REPORT.md
          git commit -m "chore: sync upstream bundles $(date +%Y-%m-%d)"

      - name: Create PR for review
        if: contains(github.event.head_commit.message, 'BREAKING')
        run: |
          gh pr create \
            --title "⚠️ BREAKING: Upstream bundle update" \
            --body-file VERIFICATION_REPORT.md

      - name: Auto-merge if safe
        if: "!contains(github.event.head_commit.message, 'BREAKING')"
        run: |
          git push origin main
```

### 3. Local Git Hooks

```bash
# .git/hooks/pre-commit
#!/bin/bash

BRANCH=$(git symbolic-ref --short HEAD)

# Prevent commit to main
if [[ "$BRANCH" == "main" ]]; then
  echo "❌ Cannot commit directly to main"
  echo "   Use: git checkout -b feature/my-work"
  exit 1
fi

# Check commit message format
MSG_FILE="${1:-.git/COMMIT_EDITMSG}"
MSG=$(cat "$MSG_FILE")

if ! echo "$MSG" | grep -qE '^(feat|fix|docs|chore|refactor|test|ci):'; then
  echo "❌ Commit message must follow conventional commits"
  echo ""
  echo "Format: <type>: <description>"
  echo ""
  echo "Types:"
  echo "  feat:     New feature"
  echo "  fix:      Bug fix"
  echo "  docs:     Documentation"
  echo "  chore:    Maintenance"
  echo "  refactor: Code refactoring"
  echo "  test:     Tests"
  echo "  ci:       CI/CD"
  exit 1
fi

# Check for TODO/FIXME without issue link
if git diff --cached | grep -E '(TODO|FIXME)' | grep -vE '#[0-9]+'; then
  echo "⚠️  Warning: TODO/FIXME found without issue reference"
  echo "   Consider adding issue number: TODO(#123)"
fi
```

---

## Documentation Structure

### oblik-io/BMAD-METHOD

```
docs/
└── oblik/
    ├── GOVERNANCE.md               # Ця політика (повна версія)
    ├── QUICK-START.md              # Швидкий старт для нових членів команди
    ├── CONTRIBUTING.md             # Як контрибутити в oblik fork
    ├── UPSTREAM-SYNC.md            # Процедури sync з upstream
    ├── PROJECT-INTEGRATION.md      # Як інтегрувати в проєкти
    └── FAQ.md                      # Часті питання
```

### oblik-io/bmad-bundles

```
├── README.md                       # How to consume bundles
├── VERIFICATION.md                 # Verification process details
├── CHANGELOG.md                    # Version history
└── docs/
    ├── custom-agents.md            # Creating custom oblik agents
    └── integration-guide.md        # Integration guide
```

### Кожен проєкт

```
project-root/
└── docs/
    └── bmad/
        ├── VERSION.md              # Current version + rationale
        ├── CUSTOMIZATIONS.md       # Project-specific changes
        └── UPDATE-LOG.md           # History of updates
```

---

## Migration Action Plan

**⚠️ ВАЖЛИВО: Це тільки ПЛАН. Виконувати ПІСЛЯ обговорення та прийняття рішень!**

### Phase 1: Infrastructure Setup (oblik.io)

```bash
# 1. Create repositories
gh repo create oblik-io/BMAD-METHOD \
  --public \
  --source bmad-code-org/BMAD-METHOD \
  --description "Controlled fork of BMAD-METHOD for oblik.io"

gh repo create oblik-io/bmad-bundles \
  --public \
  --description "Verified BMAD bundles distribution"

# 2. Clone and setup
git clone git@github.com:oblik-io/BMAD-METHOD.git
cd oblik-io/BMAD-METHOD

# 3. Add upstream
git remote add upstream https://github.com/bmad-code-org/BMAD-METHOD.git
git fetch upstream

# 4. Setup branch protection (via web UI або Terraform)
# 5. Configure secrets (BUNDLES_PAT, etc.)
```

### Phase 2: Documentation

```bash
cd oblik-io/BMAD-METHOD

# Copy governance docs
mkdir -p docs/oblik
cp /path/to/this-discussion.md docs/oblik/GOVERNANCE.md

# Create other docs
# ... (QUICK-START.md, CONTRIBUTING.md, etc.)

git checkout -b docs/initial-governance
git add docs/oblik/
git commit -m "docs: add initial governance framework"
git push origin docs/initial-governance
gh pr create --title "docs: Initial governance framework" --base main
```

### Phase 3: Automation Setup

```bash
# Copy workflows
mkdir -p .github/workflows
# ... copy workflow files з цієї дискусії

# Setup git hooks
# ... copy hook scripts

git checkout -b ci/governance-automation
git add .github/
git commit -m "ci: add governance automation"
gh pr create
```

### Phase 4: Migrate Current Work

```bash
# Migrate local repo
cd /path/to/current/BMAD-METHOD

# Update remote
git remote set-url origin git@github.com:oblik-io/BMAD-METHOD.git

# Push all branches
git push origin --all
git push origin --tags

# Update local tracking
git branch --set-upstream-to=origin/main main
```

### Phase 5: Project Integration (KRTM)

```bash
cd /path/to/krtm

# Add bmad-bundles as submodule
git submodule add https://github.com/oblik-io/bmad-bundles.git .bmad

# Create version lock
cat > .bmad.lock <<EOF
version: "v1.0.0"
source: "oblik-io/bmad-bundles"
verified: "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
checksum: "$(cd .bmad && git rev-parse HEAD)"
EOF

git add .bmad .bmad.lock .gitmodules
git commit -m "chore: integrate oblik.io bmad-bundles"
```

### Phase 6: Cleanup (felectra)

```bash
# ⚠️ ТІЛЬКИ ПІСЛЯ повної міграції та верифікації!

# Archive or delete old fork
gh repo archive felectra/BMAD-METHOD
# OR
gh repo delete felectra/BMAD-METHOD --yes

# Update any remaining references
# Check CI/CD configs, documentation, scripts
```

---

## Open Questions (Потребують обговорення)

### 1. Bundle Distribution Strategy

**Варіант A: oblik.io/bmad-bundles (Recommended)**

- ✅ Full control, verification layer
- ✅ Custom oblik agents alongside upstream
- ✅ Supply chain security
- ❌ Maintenance overhead

**Варіант B: Direct upstream consumption**

- ✅ Zero maintenance
- ✅ Always latest from upstream
- ❌ No verification layer
- ❌ No custom agents distribution

**Рішення потрібне:** A чи B?

### 2. Custom Agents Strategy

**Варіант A: Separate repo (oblik-io/oblik-agents)**

- ✅ Clear separation
- ✅ Independent versioning
- ❌ Multiple submodules

**Варіант B: Integrated в bmad-bundles**

- ✅ Single submodule
- ✅ Unified distribution
- ❌ Mixed upstream + custom content

**Рішення потрібне:** A чи B?

### 3. Approval Process

**Хто має право апрувити:**

- Major version updates?
- Breaking changes?
- Custom agent releases?
- Security patches?

**Процес:**

- Single approver sufficient?
- Required discussion period?
- Automated approvals для patches?

### 4. Versioning Strategy

**Для oblik-io/bmad-bundles:**

- Follow upstream versions?
- Independent versioning (v1.0.0-oblik.1)?
- Calendar versioning (2025.11.1)?

### 5. Communication Channels

**Де обговорювати:**

- GitHub Issues?
- GitHub Discussions?
- Discord?
- Internal Wiki?

---

## Success Criteria

**Коли політика успішна:**

1. ✅ **Clear ownership:** Кожен знає де що живе
2. ✅ **Safe updates:** Automated checks catch problems
3. ✅ **Fast contribution:** Easy to contribute upstream
4. ✅ **Controlled adoption:** Projects use verified versions
5. ✅ **Low friction:** Developers не blocked процесами
6. ✅ **Maintainable:** Sustainable long-term

**Metrics:**

- Time to update project: < 1 hour
- Upstream sync delay: < 24 hours
- PR review time: < 48 hours
- Security scan time: < 30 minutes
- Zero unintended divergence from upstream

---

## Next Steps

### Immediate (Week 1)

- [ ] Обговорити та прийняти рішення по Open Questions
- [ ] Написати GOVERNANCE.md (final version)
- [ ] Створити beads issues для tracking
- [ ] Визначити пріоритети та timeline

### Short-term (Week 2-3)

- [ ] Create oblik-io repositories (if approved)
- [ ] Write detailed documentation
- [ ] Setup CI/CD automation
- [ ] Test workflows на dev environment

### Mid-term (Week 4-6)

- [ ] Migrate current work
- [ ] Integrate KRTM project
- [ ] Train team на новий workflow
- [ ] Monitor and adjust policies

### Long-term (Month 2+)

- [ ] Contribute improvements back to upstream
- [ ] Develop custom oblik agents
- [ ] Establish governance review cadence
- [ ] Document lessons learned

---

## References

**Related Discussions:**

- [Production Process Improvements](./2025-11-12-production-process-improvements.md)

**BMAD Documentation:**

- [Enterprise Agentic Development](.bmad/bmm/docs/enterprise-agentic-development.md)
- [Bundle Distribution Setup](../BUNDLE_DISTRIBUTION_SETUP.md)
- [Contributing Guidelines](../../CONTRIBUTING.md)

**External Resources:**

- [GitHub Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules)
- [Terraform GitHub Provider](https://registry.terraform.io/providers/integrations/github/latest)
- [Conventional Commits](https://www.conventionalcommits.org/)

---

**Status:** 🔍 Discussion Draft - Awaiting decisions and approval

**Author:** @joyshmitz
**Last Updated:** 2025-11-12
**Version:** 0.1.0-draft
