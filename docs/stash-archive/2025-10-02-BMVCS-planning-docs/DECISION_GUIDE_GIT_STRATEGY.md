# Git Strategy Decision Guide - BMVCS Module

**Created:** 2025-10-01 19:30:00 EEST
**Status:** Decision Required
**Context:** First-time contributor preparing BMVCS module for PR
**Related:** Issue #661, PR #668, feat/bmvcs-dev branch

---

## 📚 Table of Contents

1. [Git Basics](#part-1-git-basics)
2. [Current Situation](#part-2-current-situation)
3. [What Changed in v6-alpha](#part-3-what-changed-in-v6-alpha)
4. [Path Fix Problem](#part-4-path-fix-problem)
5. [Three Strategies](#part-5-three-strategies)
6. [Merge vs Rebase](#part-6-merge-vs-rebase)
7. [The Three Questions](#part-7-the-three-questions)
8. [Recommended Plan](#part-8-recommended-plan)
9. [Decision Checklist](#part-9-decision-checklist)

---

## Part 1: Git Basics

### 🌳 What is a Branch?

**Analogy:** Imagine a tree with branches.

- **main** - the main trunk of the tree
- **feat/bmvcs-dev** - a branch that grew from the trunk at a specific point

```
main:        A---B---C---D---E---F (latest code in main project)
                 \
feat/bmvcs-dev:   X---Y---Z (your BMVCS work)
```

**When you created feat/bmvcs-dev:**

- You "branched off" from point B
- Then added your commits X, Y, Z
- But main continued growing (added C, D, E, F)

**Problem:** Your branch doesn't know about C, D, E, F - it's based on an old version!

---

### 🏢 What is origin vs upstream?

**origin** = your personal fork on GitHub

- `https://github.com/oblik-io/BMAD-METHOD.git`
- You can do whatever you want here
- This is YOUR copy of the project

**upstream** = the main project repository

- `https://github.com/bmad-code-org/BMAD-METHOD.git`
- Where all contributors send code
- You DON'T have direct access (only via Pull Request)

**Analogy:**

- upstream = official city library
- origin = your home copy of books from the library

---

## Part 2: Current Situation

### 📊 Branch Visualization

```
BRANCH HISTORY:

30fb0e6 ────┬──────────────────────────────────────────────> main (old)
            │
            ├─> df0c3e4 → e7fcc56 → c42cd48 → 05a3b4f → 56e7a61 → 25c3d50
            │                                                      ↑
            │                                            upstream/v6-alpha
            │                                            (LATEST v6)
            │
            └─> 9571a2f → 2137a77 → 8d342f3 → bccfe9d → 29d4dc0
                → 3f79f1f → fd16dab → 4d06ec7 → 286454e (merge main)
                → bf2ad27 → 84920e1 → e09ec31
                                      ↑
                                 feat/bmvcs-dev (YOUR CODE)
                                 (12 commits with BMVCS)
```

### 🔍 What This Means

**1. Your branch is behind v6-alpha**

When you started work (30fb0e6), upstream/v6-alpha was there too. But THEN:

**upstream/v6-alpha got 6 new commits:**

- df0c3e4: Port TEA commands (#660)
- e7fcc56: v4-v6 upgrade improvement
- c42cd48: Fix installer upgrade issues
- 05a3b4f: hash file change checking
- 56e7a61: v6 flow documented and **subagent organization**
- 25c3d50: **SubAgents in sub folders** + installer improvements

**YOU added 12 commits:**

- 9571a2f...e09ec31: all BMVCS work

**2. There's a merge of main in your branch (286454e)**

- You merged main, but NOT v6-alpha
- main and v6-alpha are DIFFERENT branches!

---

### ✅ GOOD NEWS!

The files `architect.md`, `pm.md`, `dev.md` **DID NOT CHANGE** between your branch point and latest v6-alpha!

**Verified with:**

```bash
git diff 30fb0e6..25c3d50 -- src/modules/bmm/agents/architect.md \
  src/modules/bmm/agents/pm.md src/modules/bmm/agents/dev.md
# Output: (empty - no changes!)
```

**This means:** Low risk of conflicts on the path fix!

---

## Part 3: What Changed in v6-alpha

### 🔍 Changes in upstream/v6-alpha (that you don't have):

**1. TEA Agent (#660 - Port TEA to workflows)**

- TEA rewritten from `exec=` to `run-workflow=`
- New workflows created in `workflows/testarch/`
- Knowledge base reorganized
- **Files changed:**
  - `src/modules/bmm/agents/tea.md`
  - `src/modules/bmm/testarch/*` (many files)
  - `src/modules/bmm/workflows/testarch/*` (new)

**2. SubAgents Organization**

- Sub-agents moved to subfolders:
  - `sub-agents/bmad-analysis/`
  - `sub-agents/bmad-planning/`
  - `sub-agents/bmad-research/`
  - `sub-agents/bmad-review/`
- **Files changed:** 15+ sub-agent files renamed/moved

**3. Installer Improvements**

- Better hash file checking
- Improved v4→v6 upgrade
- BMM Flow documentation

**4. Other files:**

- Communication style changes in game-\* agents
- testarch README updates

**Summary:**

```
68 files changed, 789 insertions(+), 634 deletions(-)
```

**Impact on your work:**

- ✅ No changes to architect.md, pm.md, dev.md
- ✅ No changes to src/modules/bmvcs/ (your new module)
- ⚠️ Changes to TEA and sub-agents (different area)

**Conflict Risk:** 🟢 LOW (different files)

---

## Part 4: Path Fix Problem

### 📁 How {project-root} Works

**In Claude Code / BMAD:**

- `{project-root}` is replaced with actual user's project path
- Example: `/Users/john/my-project/`

**When agent reads instruction:**

```xml
<i>Check if VCS configuration exists in {project-root}/bmad-core/vcs-config.yaml</i>
```

**Claude Code interprets as:**

```
Check file: /Users/john/my-project/bmad-core/vcs-config.yaml
```

### ❌ The Problem

**BMVCS creates config here:**

```
/Users/john/my-project/.bmad/vcs-config.yaml
```

**BMM Agents look here:**

```
/Users/john/my-project/bmad-core/vcs-config.yaml
```

**Result:** Agents DON'T FIND the config! 😱

### ✅ The Solution

Change in 3 files:

```diff
- {project-root}/bmad-core/vcs-config.yaml
+ {project-root}/.bmad/vcs-config.yaml
```

**Files to change:**

1. `src/modules/bmm/agents/architect.md` - line 17
2. `src/modules/bmm/agents/pm.md` - line 17
3. `src/modules/bmm/agents/dev.md` - line 22

### 📝 Exact Changes Needed

**File 1: architect.md (line 17)**

```xml
OLD:
<i>Check if VCS configuration exists in {project-root}/bmad-core/vcs-config.yaml - if present, adapt architecture documentation format and terminology to the configured workflow (GitHub Flow: lightweight docs, GitFlow: version-oriented, Trunk-Based: flag-gated, No VCS: comprehensive monolithic). If missing, architecture decisions remain VCS-neutral.</i>

NEW:
<i>Check if VCS configuration exists in {project-root}/.bmad/vcs-config.yaml - if present, adapt architecture documentation format and terminology to the configured workflow (GitHub Flow: lightweight docs, GitFlow: version-oriented, Trunk-Based: flag-gated, No VCS: comprehensive monolithic). If missing, architecture decisions remain VCS-neutral.</i>
```

**File 2: pm.md (line 17)**

```xml
OLD:
<i>Check if VCS configuration exists in {project-root}/bmad-core/vcs-config.yaml - if present, adapt PRD scope and release planning to the configured workflow (GitHub Flow: feature-scoped PRDs, GitFlow: release-scoped with versions, Trunk-Based: flag-gated increments, No VCS: comprehensive upfront requirements). If missing, requirements remain workflow-neutral.</i>

NEW:
<i>Check if VCS configuration exists in {project-root}/.bmad/vcs-config.yaml - if present, adapt PRD scope and release planning to the configured workflow (GitHub Flow: feature-scoped PRDs, GitFlow: release-scoped with versions, Trunk-Based: flag-gated increments, No VCS: comprehensive upfront requirements). If missing, requirements remain workflow-neutral.</i>
```

**File 3: dev.md (line 22)**

```xml
OLD:
<i>Check if VCS configuration exists in {project-root}/bmad-core/vcs-config.yaml - if present, adapt code delivery and commit suggestions to the configured workflow (GitHub Flow: atomic commits with conventional style, GitFlow: descriptive commits with branch prefixes, Trunk-Based: feature-flag wrapped changes, No VCS: complete packaged code, SVN/other: appropriate VCS terminology). If missing, remain VCS-neutral.</i>

NEW:
<i>Check if VCS configuration exists in {project-root}/.bmad/vcs-config.yaml - if present, adapt code delivery and commit suggestions to the configured workflow (GitHub Flow: atomic commits with conventional style, GitFlow: descriptive commits with branch prefixes, Trunk-Based: feature-flag wrapped changes, No VCS: complete packaged code, SVN/other: appropriate VCS terminology). If missing, remain VCS-neutral.</i>
```

---

## Part 5: Three Strategies

### 🎯 Strategy 1: Path Fix NOW, then Merge

**Order of operations:**

```
1. Make path fix in current branch (feat/bmvcs-dev)
2. Commit path fix
3. git merge upstream/v6-alpha
4. Resolve conflicts (if any)
5. Push and create PR
```

**Pros:**

- ✅ Path fix done as separate commit (easy to find in history)
- ✅ Logical order: "fix problem → sync with upstream"
- ✅ Easier to revert path fix if something goes wrong

**Cons:**

- ⚠️ Conflicts might happen during merge (but unlikely)
- ⚠️ Merge commit will be created (normal for merge strategy)

**Risks:**

- 🟡 LOW - architect/pm/dev unchanged in v6-alpha

**Commands:**

```bash
# 1. Make path fix (Edit tool on 3 files)
# 2. Commit
git add src/modules/bmm/agents/architect.md src/modules/bmm/agents/pm.md src/modules/bmm/agents/dev.md
git commit -m "fix(bmm): correct VCS config path in Architect/PM/Dev agents

- Change: bmad-core/vcs-config.yaml → .bmad/vcs-config.yaml
- Enables BMVCS integration without manual workaround
- Discovered during Alpha Phase 2 testing

Related: #661"

# 3. Merge upstream/v6-alpha
git merge upstream/v6-alpha

# 4. If conflicts, resolve them, then:
git add .
git commit

# 5. Push
git push origin feat/bmvcs-dev
```

---

### 🎯 Strategy 2: Merge FIRST, then Path Fix

**Order of operations:**

```
1. git merge upstream/v6-alpha (WITHOUT path fix)
2. Resolve conflicts
3. Verify everything works
4. THEN make path fix
5. Push and create PR
```

**Pros:**

- ✅ First sync with upstream (latest code)
- ✅ Path fix will be "on top of" latest version
- ✅ Less confusion if conflicts occur

**Cons:**

- ⚠️ Longer process
- ⚠️ Two stages instead of one

**Risks:**

- 🟡 LOW - same conflict risk

**Commands:**

```bash
# 1. Merge first
git merge upstream/v6-alpha

# 2. If conflicts, resolve and commit
git add .
git commit

# 3. Make path fix (Edit tool)
# 4. Commit path fix
git add src/modules/bmm/agents/architect.md src/modules/bmm/agents/pm.md src/modules/bmm/agents/dev.md
git commit -m "fix(bmm): correct VCS config path..."

# 5. Push
git push origin feat/bmvcs-dev
```

---

### 🎯 Strategy 3: Path Fix + Rebase (Advanced)

**Order of operations:**

```
1. Make path fix NOW
2. git rebase upstream/v6-alpha (instead of merge)
3. Resolve conflicts during rebase
4. Force push
```

**Pros:**

- ✅ Clean, linear history
- ✅ No merge commit
- ✅ Professional-looking git log

**Cons:**

- ⚠️ Rewrites history (commits get new SHAs)
- ⚠️ Requires force push
- ⚠️ More complex for beginners
- ⚠️ Risk if others are working on your branch

**Risks:**

- 🟡 MEDIUM - same conflicts + complexity

**Commands:**

```bash
# 1. Make path fix and commit
git add src/modules/bmm/agents/architect.md src/modules/bmm/agents/pm.md src/modules/bmm/agents/dev.md
git commit -m "fix(bmm): correct VCS config path..."

# 2. Rebase
git rebase upstream/v6-alpha

# 3. If conflicts during rebase:
# - Fix conflicts in each commit
# - git add <fixed-files>
# - git rebase --continue
# Repeat until done

# 4. Force push (rewrites history on remote)
git push origin feat/bmvcs-dev --force-with-lease
```

**⚠️ Warning:** Don't use rebase if others are working on feat/bmvcs-dev!

---

## Part 6: Merge vs Rebase

### 📖 Git Merge (Merging)

**Visually:**

```
BEFORE:
main:           A---B---C---D
                     \
feat/bmvcs-dev:       X---Y---Z

AFTER merge:
main:           A---B---C---D
                     \         \
feat/bmvcs-dev:       X---Y---Z---M (merge commit)
```

**What happens:**

- Git creates a special "merge commit" (M)
- M has TWO parent commits: Z and D
- All history is preserved

**Analogy:**
You're walking two roads simultaneously, then they join at one point.

**Pros:**

- ✅ Safe - preserves all history
- ✅ Easy to understand
- ✅ Easy to revert (just revert merge commit)
- ✅ Recommended for collaboration

**Cons:**

- ⚠️ Creates extra merge commit
- ⚠️ History looks more complex

---

### 📖 Git Rebase (Rebasing)

**Visually:**

```
BEFORE:
main:           A---B---C---D
                     \
feat/bmvcs-dev:       X---Y---Z

AFTER rebase:
main:           A---B---C---D
                             \
feat/bmvcs-dev:               X'---Y'---Z' (rewritten commits)
```

**What happens:**

- Git "detaches" your commits (X, Y, Z)
- "Replays" them ON TOP of D (latest main commit)
- Creates NEW commits (X', Y', Z') with same content
- Old version (X, Y, Z) is deleted

**Analogy:**
You pick up your work and place it on top of the latest version, as if you always worked from it.

**Pros:**

- ✅ Clean, linear history
- ✅ No merge commits
- ✅ Professional git log

**Cons:**

- ⚠️ Rewrites history (changes SHAs)
- ⚠️ Requires force push
- ⚠️ Dangerous if others use your branch
- ⚠️ More complex to understand

---

### 🤔 Merge vs Rebase - Which to Choose?

| Criteria          | Merge                 | Rebase                         |
| ----------------- | --------------------- | ------------------------------ |
| **Safety**        | 🟢 Very safe          | 🟡 Safe (but rewrites history) |
| **Simplicity**    | 🟢 Easy to understand | 🟡 Requires understanding      |
| **History**       | Preserves everything  | Linear and clean               |
| **Rollback**      | Easy (revert)         | More complex                   |
| **For beginners** | ✅ Recommended        | ⚠️ After practice              |
| **Collaboration** | ✅ Safe               | ⚠️ Risk if others on branch    |

**For first time: RECOMMEND MERGE** 🎯

---

## Part 7: The Three Questions

### ❓ Question 1: Should we rebase/merge BEFORE or AFTER path fix?

**Context:**

- Your branch is based on old v6-alpha (30fb0e6)
- Latest v6-alpha (25c3d50) has 6 new commits
- Path fix changes 3 files (architect.md, pm.md, dev.md)
- Those 3 files are UNCHANGED in v6-alpha

**Options:**

**A) Path Fix → Merge (RECOMMENDED for first time)**

```bash
1. Make path fix in architect.md, pm.md, dev.md
2. git commit -m "fix: correct VCS config path..."
3. git merge upstream/v6-alpha
4. git push origin feat/bmvcs-dev
```

**Why:** Simple, safe, understandable.

**B) Merge → Path Fix**

```bash
1. git merge upstream/v6-alpha
2. Resolve conflicts (if any)
3. Make path fix
4. git commit and push
```

**Why:** Sync first, then fix.

**C) Path Fix → Rebase (for experienced users)**

```bash
1. Path fix
2. git rebase upstream/v6-alpha
3. Force push
```

**Why:** Clean history, but more complex.

**My recommendation:** **Option A** (Path Fix → Merge)

**Reasoning:**

- ✅ Logical flow: fix problem first, then sync
- ✅ Path fix commit is clearly visible
- ✅ Safest option (merge, not rebase)
- ✅ Easy to revert if needed
- ✅ No force push required

---

### ❓ Question 2: What to do with old VCS branches?

**Which branches:**

```
LOCAL:
- vcs-adaptation-templates
- vcs-agnostic-discovery
- vcs-discovery-core
- vcs-documentation

REMOTE (origin):
- vcs-adaptation-templates
- vcs-discovery-core
- vcs-documentation
```

**Context:**
These branches are your old PRs (#582, #583, #584) for v4 architecture. You consolidated them into feat/bmvcs-dev.

**Options:**

**A) Delete AFTER successful PR** (RECOMMENDED)

```bash
# AFTER feat/bmvcs-dev is merged into upstream
# Delete local
git branch -d vcs-adaptation-templates
git branch -d vcs-agnostic-discovery
git branch -d vcs-discovery-core
git branch -d vcs-documentation

# Delete remote
git push origin --delete vcs-adaptation-templates
git push origin --delete vcs-discovery-core
git push origin --delete vcs-documentation
```

**Why:** No longer needed, code is in feat/bmvcs-dev.

**B) Keep for history**

```bash
# Do nothing
```

**Why:** Might want to reference old versions.

**C) Archive with tags**

```bash
git tag archive/vcs-templates vcs-adaptation-templates
git tag archive/vcs-discovery vcs-agnostic-discovery
git tag archive/vcs-core vcs-discovery-core
git tag archive/vcs-docs vcs-documentation

# Then delete branches
git branch -d vcs-adaptation-templates
# etc...

# Push tags
git push origin --tags
```

**Why:** Keep reference but clean up branches.

**My recommendation:** **Option A** (Delete after PR)

**Reasoning:**

- ✅ Clean up your fork
- ✅ All code preserved in feat/bmvcs-dev
- ✅ Git history still has old commits
- ✅ Can always find them if needed via git log
- ⚠️ But wait until PR is merged!

**Timeline:**

```
NOW: Keep branches (do nothing)
  ↓
PR created and merged
  ↓
THEN: Delete old branches
```

---

### ❓ Question 3: PR Strategy and Coordination

**Target Branch:** `v6-alpha` ✅ (confirmed in `.git/config`)

**About PR #668:**

**What is PR #668?**

- Author: Mark Pundsack
- Base: `main` (NOT v6-alpha!)
- Changes: Adds VCS requirements to DoD checklist
- File: `bmad-core/checklists/story-dod-checklist.md`
- Mentions: #661 as "future enhancement"
- Status: Open

**Does it conflict with your work?**
❌ NO!

**Why no conflict:**

- PR #668 changes: `bmad-core/checklists/story-dod-checklist.md`
- Your changes: `src/modules/bmvcs/` and `src/modules/bmm/agents/`
- Different files = no conflicts

**Relationship:**

- PR #668: Adds VCS awareness to DoD checklist (quick fix for v4 users)
- Your work: Full BMVCS module for v6 (comprehensive solution)
- They complement each other!

**Should you coordinate?**

**Option A: Comment on #661**
Add comment mentioning:

- You're preparing BMVCS module PR
- PR #668 is complementary (DoD checklist)
- Your PR will provide full VCS integration

**Option B: No coordination needed**

- Different target branches (main vs v6-alpha)
- Different scope
- Let maintainers handle

**My recommendation:** **Option A** (brief comment)

**Suggested comment:**

```markdown
## Update: BMVCS Module PR Coming Soon

I'm preparing the BMVCS module PR targeting `v6-alpha`.

The module is complete with:

- ✅ VCS detection and configuration
- ✅ 5 workflow templates (GitHub Flow, GitFlow, Trunk-Based, Custom, No-VCS)
- ✅ Integration with Architect/PM/Dev agents
- ✅ Alpha testing completed

I noticed PR #668 adds VCS requirements to the DoD checklist - that's
complementary to this work and will help v4 users. The BMVCS module
will provide full VCS workflow adaptation for v6.

PR coming in the next few days after final sync with v6-alpha.
```

---

**PR Strategy for your work:**

**Option A: One Large PR (~5,000 lines)**

- Base: `v6-alpha`
- Title: `feat(bmvcs): Add BMVCS module for VCS workflow adaptation`
- Body: Reference #661, explain consolidation from #582-584
- All files in one PR

**Pros:**

- ✅ Complete feature in one place
- ✅ Easy to review holistically
- ✅ Issue #661 already exists as Epic
- ✅ Aligns with module-based v6 architecture

**Cons:**

- ⚠️ Large PR (~5,000 lines)
- ⚠️ Exceeds CONTRIBUTING.md 800-line guideline

**Option B: Split into 3 PRs**

- PR1: Core (tasks, agent, installer) ~1,500 lines
- PR2: Templates + Docs ~2,000 lines
- PR3: Examples + Integration ~1,500 lines

**Pros:**

- ✅ Follows CONTRIBUTING.md size guideline
- ✅ Easier to review individual pieces

**Cons:**

- ⚠️ Must wait for PR1 merge before PR2
- ⚠️ More overhead (3 PRs, 3 reviews)
- ⚠️ Feature split across multiple PRs
- ⚠️ Module incomplete until all 3 merged

**My recommendation:** **Option A** (One PR)

**Reasoning:**

- ✅ BMVCS is a cohesive module (v6 architectural unit)
- ✅ All tested together in Alpha Phase 2
- ✅ Issue #661 already sets expectation (Epic)
- ✅ Maintainers can request split if needed
- ✅ Similar to how bmm, bmb, cis modules were added

**Justification for size:**

```markdown
This PR is ~5,000 lines, exceeding the 800-line guideline. However:

1. BMVCS is a complete v6 module following bmm/bmb/cis pattern
2. All components tested together (Alpha Phase 2 complete)
3. Splitting would leave module in incomplete state
4. Issue #661 documents this as an Epic feature
5. Consolidates legacy PRs #582, #583, #584 into v6 architecture

I can split into smaller PRs if maintainers prefer.
```

---

## Part 8: Recommended Plan

### 🎯 Safest Path for First-Time Contributor

```
PHASE 1: Preparation (NOW)
├─ Understand situation ✅ (we're here)
├─ Make decisions
└─ Clean up package-lock.json

PHASE 2: Path Fix + Sync
├─ 1. Make path fix (3 files via Edit tool)
├─ 2. Commit path fix with detailed message
├─ 3. git merge upstream/v6-alpha
├─ 4. Resolve conflicts (if any - unlikely)
├─ 5. Test locally (optional but recommended)
└─ 6. git push origin feat/bmvcs-dev

PHASE 3: PR Creation
├─ 1. Update issue #661 with status comment
├─ 2. Create PR to bmad-code-org/BMAD-METHOD
├─ 3. Base: v6-alpha
├─ 4. Reference #661, #582, #583, #584
├─ 5. Include alpha testing results
└─ 6. Wait for review

PHASE 4: Cleanup (AFTER merge)
├─ 1. Delete old VCS branches locally
├─ 2. Delete old VCS branches on origin
└─ 3. Update documentation if needed
```

### 📋 Detailed Commands

**Phase 1: Preparation**

```bash
# Check status
git status

# Option A: Commit package-lock.json
git add package-lock.json
git commit -m "chore: update package-lock.json"

# Option B: Stash if you want to handle later
git stash push -m "WIP: package-lock.json"

# Verify branch
git branch --show-current
# Expected: feat/bmvcs-dev

# Fetch latest from upstream
git fetch upstream
```

**Phase 2: Path Fix + Sync**

```bash
# 1. Make path fix using Edit tool on:
# - src/modules/bmm/agents/architect.md (line 17)
# - src/modules/bmm/agents/pm.md (line 17)
# - src/modules/bmm/agents/dev.md (line 22)
# Change: bmad-core/vcs-config.yaml → .bmad/vcs-config.yaml

# 2. Commit
git add src/modules/bmm/agents/architect.md \
        src/modules/bmm/agents/pm.md \
        src/modules/bmm/agents/dev.md

git commit -m "$(cat <<'EOF'
fix(bmm): correct VCS config path in Architect/PM/Dev agents

ISSUE: Path Inconsistency
BMM agents were looking for VCS config at wrong path:
- Old: bmad-core/vcs-config.yaml (incorrect)
- New: .bmad/vcs-config.yaml (correct per BMVCS spec)

IMPACT:
VCS integration failed without manual workaround

FIX:
Updated 3 agent files to use correct path:
- src/modules/bmm/agents/architect.md (line 17)
- src/modules/bmm/agents/pm.md (line 17)
- src/modules/bmm/agents/dev.md (line 22)

TESTING:
Discovered during BMVCS Alpha Phase 2 testing
- Workaround documented, now properly fixed in source
- Test results: ~/test-bmvcs-install/testing/

AFFECTED AGENTS:
✅ Architect - VCS-aware documentation generation
✅ PM - VCS-aware requirements planning
✅ Dev - VCS-aware implementation guidance

This fix enables seamless VCS integration without manual intervention.

Related: #661
Testing: Alpha Phase 2 complete (2025-10-01)
EOF
)"

# 3. Merge upstream/v6-alpha
git merge upstream/v6-alpha -m "Merge upstream/v6-alpha into feat/bmvcs-dev

Brings feat/bmvcs-dev up to date with latest v6-alpha:
- TEA agent workflows (#660)
- SubAgents organization
- Installer improvements
- v6 flow documentation

No conflicts expected in BMVCS module files.
"

# 4. If conflicts occur (unlikely):
git status  # See conflicted files
# Fix conflicts manually
git add <fixed-files>
git commit  # Complete the merge

# 5. Optional: Test locally
# (Run any tests or validation you want)

# 6. Push to origin
git push origin feat/bmvcs-dev
```

**Phase 3: PR Creation**

```bash
# 1. Comment on issue #661
gh issue comment 661 --repo bmad-code-org/BMAD-METHOD --body "$(cat <<'EOF'
## 🚀 Ready for PR Submission

BMVCS module development complete and synced with v6-alpha!

### ✅ Completed Work
- All code from legacy PRs #582, #583, #584 consolidated into v6 module
- Path fix applied (correct VCS config path)
- Synced with latest upstream/v6-alpha
- Alpha Phase 2 testing complete

### 📦 Module Contents
- Core tasks: discover-vcs, create-vcs-adapted-doc, validate-vcs-config
- VCS Adapter agent
- 5 workflow templates (GitHub Flow, GitFlow, Trunk-Based, Custom, No-VCS)
- Complete documentation and examples
- Module installer integration

### 🎯 Next Steps
Creating PR to v6-alpha branch in next 1-2 days.

Branch: feat/bmvcs-dev (oblik-io/BMAD-METHOD)
Target: v6-alpha (bmad-code-org/BMAD-METHOD)
Size: ~5,000 lines (cohesive module, tested together)
EOF
)"

# 2. Create PR (when ready)
gh pr create --repo bmad-code-org/BMAD-METHOD \
  --base v6-alpha \
  --head oblik-io:feat/bmvcs-dev \
  --title "feat(bmvcs): Add BMVCS module for VCS workflow adaptation" \
  --body "$(cat <<'EOF'
## 🎯 Goal

Add BMVCS (BMAD Version Control Suite) module to v6 architecture, providing VCS-agnostic workflow adaptation for BMM agents.

## 📚 Background

**Legacy Work:**
- PRs #582, #583, #584 targeted v4 architecture (now closed)
- Consolidated and migrated to v6 modular structure
- Issue #661 tracks this Epic

**Module Purpose:**
BMVCS adapts BMAD to team's version control workflow:
- Detects VCS type (Git, SVN, Perforce, no-VCS)
- Adapts documentation to workflow (GitHub Flow, GitFlow, Trunk-Based, etc)
- Optional module - install only if needed
- Integrates with BMM agents (Architect, PM, Dev)

## ✅ What's Included

### Core Functionality
- **VCS Adapter Agent** (`agents/vcs-adapter.md`)
  - Commands: *discover, *adapt-doc, *validate, *explain
- **Tasks**
  - `discover-vcs.md` - Auto-detect VCS type and workflow
  - `create-vcs-adapted-doc.md` - Adapt docs to workflow
  - `validate-vcs-config.md` - Validate configuration
- **Setup Workflow** (`workflows/setup-vcs/`)
  - Interactive VCS configuration
  - Discovery and validation

### Templates
- `git-github-flow.yaml` - GitHub Flow adaptation
- `git-gitflow.yaml` - GitFlow adaptation
- `git-trunk-based.yaml` - Trunk-Based Development
- `custom-generic.yaml` - Custom workflow template
- `no-vcs.yaml` - No version control

### Integration
- BMM Architect agent - VCS-aware architecture docs
- BMM PM agent - VCS-aware requirements planning
- BMM Dev agent - VCS-aware code delivery
- Module installer configuration
- **Path fix included:** Corrected VCS config path in agents

### Documentation
- Complete README with usage examples
- VCS detection principles and proposal
- Development approach analysis
- Usage examples and reference implementations
- Alpha testing documentation

### Testing
- Alpha Phase 2 testing complete
- Test results: ~/test-bmvcs-install/testing/
- All workflows validated
- BMM integration verified

## 📊 Changes

**Module Structure:**
```

src/modules/bmvcs/
├── agents/vcs-adapter.md
├── tasks/ (3 tasks)
├── templates/vcs-adaptations/ (5 templates)
├── workflows/setup-vcs/
├── docs/ (complete documentation)
├── examples/
└── \_module-installer/

```

**BMM Agent Updates:**
- `src/modules/bmm/agents/architect.md` - VCS integration
- `src/modules/bmm/agents/pm.md` - VCS integration
- `src/modules/bmm/agents/dev.md` - VCS integration

**Stats:**
- ~31 files added
- ~5,000 lines total
- 3 BMM agent files modified
- Base: v6-alpha (synced 2025-10-01)

## 🧪 Testing

### Alpha Testing (Complete)
- VCS discovery with real Git repositories ✅
- VCS Adapter agent commands ✅
- Adaptation templates (GitHub Flow, GitFlow, Trunk-Based) ✅
- Module installer ✅
- BMM integration (Architect, PM, Dev) ✅
- Validation and error handling ✅

### Test Environment
- Test repo: ~/test-bmvcs-install
- Test logs: testing/01-13 (detailed results)
- Path fix validated ✅

## 📝 Size Justification

This PR is ~5,000 lines, exceeding the 800-line guideline. However:

1. **Cohesive Module:** BMVCS follows v6 module pattern (bmm/bmb/cis)
2. **Tested Together:** All components validated in Alpha Phase 2
3. **Complete Feature:** Splitting would leave module incomplete
4. **Epic Scope:** Issue #661 documents as Epic feature
5. **Consolidation:** Merges legacy PRs #582, #583, #584 into v6

I can split into smaller PRs if maintainers prefer.

## 🔗 Related

- Closes #661 (Epic)
- Supersedes #582, #583, #584 (legacy v4 PRs)
- Complements PR #668 (DoD checklist VCS requirements)

## ✅ Checklist

- [x] Follows v6 module structure
- [x] Module installer configured
- [x] Complete documentation
- [x] Examples provided
- [x] Alpha testing complete
- [x] BMM integration verified
- [x] No breaking changes to existing modules
- [x] Optional module (graceful degradation if not installed)

## 🎉 Success Criteria

- [ ] Code review approved
- [ ] No conflicts with v6-alpha
- [ ] Module installs without errors
- [ ] Core workflows functional
- [ ] Documentation clear and complete
- [ ] PR merged into v6-alpha

---

**Branch:** feat/bmvcs-dev
**Testing:** Complete (Alpha Phase 2)
**Status:** Ready for review
EOF
)"
```

**Phase 4: Cleanup (AFTER PR merged)**

```bash
# Only do this AFTER your PR is merged!

# Delete local branches
git branch -d vcs-adaptation-templates
git branch -d vcs-agnostic-discovery
git branch -d vcs-discovery-core
git branch -d vcs-documentation

# Delete remote branches
git push origin --delete vcs-adaptation-templates
git push origin --delete vcs-discovery-core
git push origin --delete vcs-documentation

# Note: vcs-agnostic-discovery might not be on remote
```

---

## Part 9: Decision Checklist

### ✅ Decisions You Need to Make

**Decision 1: Merge or Rebase?**

- [ ] **Option A: Merge** (recommended for first time)
- [ ] Option B: Rebase (if you want clean history)

**My recommendation:** ✅ Merge (safer, simpler)

---

**Decision 2: When to do Path Fix?**

- [ ] **Option A: Path Fix → then Merge** (recommended)
- [ ] Option B: Merge → then Path Fix

**My recommendation:** ✅ Path Fix first (logical order)

---

**Decision 3: One PR or Multiple?**

- [ ] **Option A: One large PR (~5,000 lines)** (recommended)
- [ ] Option B: Split into 3 PRs (more overhead)

**My recommendation:** ✅ One PR (cohesive module)

---

**Decision 4: Old VCS Branches?**

- [ ] Delete now
- [ ] **Delete after PR merged** (recommended)
- [ ] Keep for history
- [ ] Archive with tags

**My recommendation:** ✅ Delete after PR merged

---

**Decision 5: Comment on Issue #661?**

- [ ] **Yes, brief status update** (recommended)
- [ ] No, create PR directly

**My recommendation:** ✅ Yes, keep stakeholders informed

---

### 📝 Your Decision Summary

Fill this out after thinking:

```
MY DECISIONS:

1. Sync strategy: [ ] Merge  [ ] Rebase
2. Path fix timing: [ ] Before sync  [ ] After sync
3. PR strategy: [ ] One PR  [ ] Multiple PRs
4. Old branches: [ ] Delete now  [ ] Delete after PR  [ ] Keep
5. Issue comment: [ ] Yes  [ ] No

Notes:
___________________________________________
___________________________________________
___________________________________________

Ready to proceed: [ ] Yes  [ ] Need more info

Questions I still have:
___________________________________________
___________________________________________
___________________________________________
```

---

## 📚 Additional Resources

### Git Commands Reference

**Check branch status:**

```bash
git status
git branch --show-current
git log --oneline --graph -10
```

**Sync with upstream:**

```bash
git fetch upstream
git merge upstream/v6-alpha
# or
git rebase upstream/v6-alpha
```

**Undo operations (if needed):**

```bash
# Undo last commit (keep changes)
git reset --soft HEAD~1

# Abort merge
git merge --abort

# Abort rebase
git rebase --abort

# Undo changes to a file
git checkout HEAD -- <file>
```

**Check for conflicts:**

```bash
# See what would merge
git merge --no-commit --no-ff upstream/v6-alpha
git merge --abort  # Cancel the check
```

### Testing Locally

After path fix and merge:

```bash
# 1. Go to test repo
cd ~/test-bmvcs-install

# 2. Update BMAD installation (copy new files)
cp ~/github/BMAD-METHOD/src/modules/bmm/agents/architect.md \
   .claude/commands/bmad/bmm/agents/

# Similar for pm.md and dev.md

# 3. Test with a simple document
# Use Claude Code: /bmad:bmm:agents:architect
# Ask to adapt a doc for your VCS workflow

# 4. Verify it finds .bmad/vcs-config.yaml
# (No error about missing config)
```

---

## 🎯 Summary

### The Situation

- You have 12 commits of BMVCS work on feat/bmvcs-dev
- upstream/v6-alpha has 6 new commits you don't have
- Path fix needed in 3 BMM agent files
- Low conflict risk (your files unchanged in v6-alpha)

### Recommended Approach

1. **Path Fix first** - logical order, clear commit
2. **Merge upstream/v6-alpha** - safe, preserves history
3. **One large PR** - cohesive module, tested together
4. **Delete old branches after PR** - clean up when safe

### Why This Approach?

- ✅ Safest for first-time contributor
- ✅ Easy to understand and execute
- ✅ Easy to revert if needed
- ✅ No force push required
- ✅ Preserves all history
- ✅ Low risk of problems

### Next Step

**Think about the decisions, then tell me:**

1. Which approach you want to use
2. Any questions you still have
3. When you're ready to start

---

**Document Status:** Complete
**Last Updated:** 2025-10-01 19:30:00 EEST
**Author:** Claude Code (with user sd)
**Purpose:** Decision support for BMVCS PR preparation
