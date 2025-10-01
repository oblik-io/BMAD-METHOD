# BMAD-METHOD Path Fix Plan

**Created:** 2025-10-01 17:45:00 EEST
**Repository:** ~/github/BMAD-METHOD
**Branch:** feat/bmvcs-dev
**Issue:** Path inconsistency in BMM agents VCS integration

---

## Executive Summary

**Problem:** BMM agents look for VCS config at wrong path

- **Expected (BMVCS):** `.bmad/vcs-config.yaml`
- **Actual (Agents):** `bmad-core/vcs-config.yaml`
- **Impact:** VCS integration doesn't work without manual workaround

**Solution:** Update 3 agent source files to use correct path

**Estimated Time:** 15 minutes

---

## Current State Analysis

### Repository Info

- **Location:** `~/github/BMAD-METHOD`
- **Current Branch:** `feat/bmvcs-dev`
- **Last Commit:** `84920e1` - chore(bmvcs): remove testing notes
- **Origin:** `https://github.com/oblik-io/BMAD-METHOD.git` (your fork)
- **Upstream:** `https://github.com/bmad-code-org/BMAD-METHOD.git` (main repo)
- **Status:** Has uncommitted change in `package-lock.json`

### PR Status

- **Existing PR:** To `github.com/joyshmitz/BMAD-METHOD` (mentioned by user)
- **Note:** No PR visible to oblik-io/BMAD-METHOD via `gh pr list`
- **Implication:** May need to create PR to oblik-io after fix

### Affected Files (Source)

Located in: `~/github/BMAD-METHOD/src/modules/bmm/agents/`

1. **architect.md** - Line 68

   ```xml
   <i>Check if VCS configuration exists in bmad-core/vcs-config.yaml
   ```

2. **pm.md** - Line 68

   ```xml
   <i>Check if VCS configuration exists in bmad-core/vcs-config.yaml
   ```

3. **dev.md** - Line 73
   ```xml
   <i>Check if VCS configuration exists in bmad-core/vcs-config.yaml
   ```

---

## Execution Plan

### Phase 1: Pre-Fix Verification (5 min)

#### Step 1.1: Clean Working Directory

```bash
cd ~/github/BMAD-METHOD
git status
```

**Decision Point:**

- If only `package-lock.json` modified → commit or stash
- If other changes → review and decide

**Action:**

```bash
# Option A: Commit package-lock.json
git add package-lock.json
git commit -m "chore: update package-lock.json"

# Option B: Stash
git stash push -m "WIP: package-lock.json before path fix"
```

#### Step 1.2: Verify Current Branch

```bash
git branch --show-current
# Expected: feat/bmvcs-dev
```

#### Step 1.3: Backup Current State

```bash
git log -1 --oneline > /tmp/bmad-before-fix.txt
git diff HEAD -- src/modules/bmm/agents/ > /tmp/bmad-agents-before.diff
```

---

### Phase 2: Apply Fix (5 min)

#### Step 2.1: Update architect.md

```bash
cd ~/github/BMAD-METHOD
```

**File:** `src/modules/bmm/agents/architect.md`
**Line:** 68

**Change:**

```diff
- <i>Check if VCS configuration exists in bmad-core/vcs-config.yaml
+ <i>Check if VCS configuration exists in .bmad/vcs-config.yaml
```

**Full context (lines 68-72):**

```xml
<i>Check if VCS configuration exists in .bmad/vcs-config.yaml
→ GitHub Flow: lightweight docs focusing on individual PRs
→ GitFlow: version-oriented documentation with release cycles
→ Trunk-Based: flag-gated incremental documentation
→ No VCS: comprehensive monolithic documentation
```

#### Step 2.2: Update pm.md

**File:** `src/modules/bmm/agents/pm.md`
**Line:** 68

**Change:**

```diff
- <i>Check if VCS configuration exists in bmad-core/vcs-config.yaml
+ <i>Check if VCS configuration exists in .bmad/vcs-config.yaml
```

**Full context (lines 68-72):**

```xml
<i>Check if VCS configuration exists in .bmad/vcs-config.yaml
→ GitHub Flow: feature-scoped PRDs with 1-3 day stories
→ GitFlow: release-scoped PRDs with 3-5 day stories and versioning
→ Trunk-Based: flag-gated increments with <1 day stories
→ No VCS: comprehensive upfront requirements
```

#### Step 2.3: Update dev.md

**File:** `src/modules/bmm/agents/dev.md`
**Line:** 73

**Change:**

```diff
- <i>Check if VCS configuration exists in bmad-core/vcs-config.yaml
+ <i>Check if VCS configuration exists in .bmad/vcs-config.yaml
```

**Full context (lines 73-77):**

```xml
<i>Check if VCS configuration exists in .bmad/vcs-config.yaml
→ GitHub Flow: atomic commits with conventional commit style
→ GitFlow: descriptive commits with branch prefixes
→ Trunk-Based: feature-flag wrapped changes with frequent commits
→ No VCS: complete packaged code delivery
```

---

### Phase 3: Verification (3 min)

#### Step 3.1: Verify Changes

```bash
cd ~/github/BMAD-METHOD
git diff src/modules/bmm/agents/architect.md
git diff src/modules/bmm/agents/pm.md
git diff src/modules/bmm/agents/dev.md
```

**Expected output for each file:**

- One line changed: `bmad-core/vcs-config.yaml` → `.bmad/vcs-config.yaml`
- Context preserved
- No other changes

#### Step 3.2: Check Line Numbers

```bash
grep -n "\.bmad/vcs-config\.yaml" src/modules/bmm/agents/architect.md
grep -n "\.bmad/vcs-config\.yaml" src/modules/bmm/agents/pm.md
grep -n "\.bmad/vcs-config\.yaml" src/modules/bmm/agents/dev.md
```

**Expected:**

- architect.md:68
- pm.md:68
- dev.md:73

#### Step 3.3: Verify No Other Files Affected

```bash
git status
```

**Expected:** Only 3 files modified:

- `src/modules/bmm/agents/architect.md`
- `src/modules/bmm/agents/pm.md`
- `src/modules/bmm/agents/dev.md`

---

### Phase 4: Commit & Push (2 min)

#### Step 4.1: Stage Changes

```bash
cd ~/github/BMAD-METHOD
git add src/modules/bmm/agents/architect.md
git add src/modules/bmm/agents/pm.md
git add src/modules/bmm/agents/dev.md
```

#### Step 4.2: Commit

```bash
git commit -m "$(cat <<'EOF'
fix(bmm): correct VCS config path in Architect/PM/Dev agents

ISSUE: Path Inconsistency
BMM agents were looking for VCS config at wrong path:
- Old: bmad-core/vcs-config.yaml (incorrect)
- New: .bmad/vcs-config.yaml (correct per BMVCS spec)

IMPACT:
VCS integration failed without manual workaround (copy config to both locations)

FIX:
Updated 3 agent files to use correct path:
- src/modules/bmm/agents/architect.md (line 68)
- src/modules/bmm/agents/pm.md (line 68)
- src/modules/bmm/agents/dev.md (line 73)

TESTING:
Discovered during BMVCS Alpha Phase 2 testing (sections 2.6-2.7)
- Test repo: ~/test-bmvcs-install
- Test results: testing/12-ALPHA-ARCHITECT-INTEGRATION-SECTION-2-6.md
- Workaround documented, now properly fixed in source

AFFECTED AGENTS:
✅ Architect - VCS-aware documentation generation
✅ PM - VCS-aware requirements planning
✅ Dev - VCS-aware implementation guidance
❌ SM - No VCS integration (by design)
❌ TEA - No VCS integration (by design)

This fix enables seamless VCS integration without manual intervention.

Related: feat/bmvcs-dev branch development
Testing: Alpha Phase 2 complete (2025-10-01)
EOF
)"
```

#### Step 4.3: Push to Origin

```bash
git push origin feat/bmvcs-dev
```

**Result:** Updates existing branch on `oblik-io/BMAD-METHOD`

---

### Phase 5: Test in test-bmvcs-install (Optional, 10 min)

**Purpose:** Verify fix works in test environment

#### Step 5.1: Reinstall BMAD-METHOD in Test Repo

```bash
cd ~/test-bmvcs-install

# Option A: Full reinstall
# rm -rf .claude/commands/bmad
# cd ~/github/BMAD-METHOD && npm run install

# Option B: Copy only updated agents
cp ~/github/BMAD-METHOD/src/modules/bmm/agents/architect.md .claude/commands/bmad/bmm/agents/
cp ~/github/BMAD-METHOD/src/modules/bmm/agents/pm.md .claude/commands/bmad/bmm/agents/
cp ~/github/BMAD-METHOD/src/modules/bmm/agents/dev.md .claude/commands/bmad/bmm/agents/
```

#### Step 5.2: Remove Workaround

```bash
cd ~/test-bmvcs-install
rm -rf bmad-core/
```

#### Step 5.3: Test Integration

```bash
# Create simple test document
cat > test-fix.md <<'EOF'
# Test Architecture

Simple test to verify VCS integration.
EOF

# Test with Architect agent (in new Claude Code session)
# Command: /bmad:bmm:agents:architect
# Request: "Adapt this document for our VCS workflow"
```

**Expected Result:**

- Agent reads `.bmad/vcs-config.yaml` ✅
- No error about missing config ✅
- Document adapted per workflow ✅
- No manual workaround needed ✅

---

## Post-Fix Actions

### Immediate (After Phase 4)

1. **Update PR Description** (if PR exists to joyshmitz/BMAD-METHOD)
   - Add note about path fix
   - Reference Alpha testing results
   - Link to fix commit

2. **Consider Creating PR to oblik-io/BMAD-METHOD**
   ```bash
   cd ~/github/BMAD-METHOD
   gh pr create --base main --head feat/bmvcs-dev \
     --title "feat(bmvcs): VCS Adapter with path fix" \
     --body "Includes path inconsistency fix discovered in Alpha testing"
   ```

### Follow-up (Next Session)

1. **Document Fix in Test Results**
   - Update `~/test-bmvcs-install/SESSION_END_PHASE_2_COMPLETE_2025-10-01.md`
   - Add "Fixed in source" status

2. **Clean Up Test Workaround**

   ```bash
   cd ~/test-bmvcs-install
   rm -rf bmad-core/
   git add bmad-core/
   git commit -m "chore: remove VCS config workaround after upstream fix"
   ```

3. **Update TESTING_STATUS.md**
   - Mark path issue as "✅ FIXED in source"
   - Update status from "⚠️ Workaround" to "✅ Resolved"

---

## Risk Assessment

### Low Risk ✅

- **Change scope:** Only 3 files, 1 line each
- **Change type:** String literal (path)
- **Testing:** Extensively tested in Alpha Phase 2
- **Rollback:** Simple git revert if needed

### Medium Risk ⚠️

- **Integration:** Requires BMVCS to be present
- **Backwards compat:** Old installations will break (acceptable - alpha)

### High Risk ❌

- None identified

---

## Rollback Plan

If fix causes issues:

```bash
cd ~/github/BMAD-METHOD
git revert HEAD
git push origin feat/bmvcs-dev
```

Or targeted rollback:

```bash
git checkout HEAD~1 -- src/modules/bmm/agents/architect.md
git checkout HEAD~1 -- src/modules/bmm/agents/pm.md
git checkout HEAD~1 -- src/modules/bmm/agents/dev.md
git commit -m "revert: rollback VCS config path change"
```

---

## Success Criteria

✅ **Phase 1:** Clean working directory, verified branch
✅ **Phase 2:** All 3 files updated correctly
✅ **Phase 3:** Changes verified, no unintended modifications
✅ **Phase 4:** Committed and pushed to origin
✅ **Phase 5:** (Optional) Tested in test-bmvcs-install

**Definition of Done:**

- [ ] 3 agent files updated with correct path
- [ ] Commit created with detailed message
- [ ] Pushed to origin/feat/bmvcs-dev
- [ ] No breaking changes introduced
- [ ] (Optional) Verified in test environment

---

## Notes from Alpha Testing

**Source:** `~/test-bmvcs-install/testing/12-ALPHA-ARCHITECT-INTEGRATION-SECTION-2-6.md`

**Discovery Context:**

- Section 2.6: Architect Agent Integration testing
- Date: 2025-10-01 15:40:00 EEST
- Workaround: `cp .bmad/vcs-config.yaml bmad-core/vcs-config.yaml`

**Test Results:**

- GitHub Flow adaptation: 65 → 262 lines (+303%)
- GitFlow adaptation: 65 → 410 lines (+531%)
- Integration works with workaround
- Value proposition validated: 99%+ time savings

**Recommendation:**
Fix in source (BMAD-METHOD repo) rather than test repo

---

## Timeline Estimate

| Phase           | Task                 | Time       |
| --------------- | -------------------- | ---------- |
| 1               | Pre-fix verification | 5 min      |
| 2               | Apply fix (3 files)  | 5 min      |
| 3               | Verification         | 3 min      |
| 4               | Commit & push        | 2 min      |
| **Total**       | **Core fix**         | **15 min** |
| 5               | Optional testing     | +10 min    |
| **Grand Total** | **With testing**     | **25 min** |

---

## Checklist for Next Session

**Before Starting:**

- [ ] Read this plan document
- [ ] Verify still on `feat/bmvcs-dev` branch
- [ ] Check no conflicting changes

**During Execution:**

- [ ] Follow phases sequentially
- [ ] Verify each step before proceeding
- [ ] Document any deviations

**After Completion:**

- [ ] Verify push successful
- [ ] Update test repo status
- [ ] Mark issue as resolved in session docs

---

**Plan Status:** READY FOR EXECUTION
**Recommended Session:** Fresh session with full context
**Prerequisites:** None (all info in this plan)

**Generated:** 2025-10-01 17:45:00 EEST
**Testing Reference:** ~/test-bmvcs-install/SESSION_END_PHASE_2_COMPLETE_2025-10-01.md
