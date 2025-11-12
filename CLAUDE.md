# CLAUDE.md - BMAD-METHOD Fork Configuration

**Version:** 1.0.0
**Created:** 2025-11-12 17:50:00 EET
**Fork Status:** Personal fork for process improvements and experimentation
**Upstream:** https://github.com/bmad-code-org/BMAD-METHOD
**Language:** Ukrainian (communication) / English (code)

---

## ⚠️ CRITICAL: Fork Status

**THIS IS A PERSONAL FORK - NOT THE UPSTREAM PROJECT.**

**Pull Request Policy:**

- ❌ **DO NOT** push to upstream (bmad-code-org/BMAD-METHOD)
- ✅ **DO** push to origin (your fork)
- ✅ **DO** experiment freely on feature branches
- ✅ **DO** sync from upstream when beneficial

**Workflow:**

```bash
# Correct workflow
git push origin feature/your-branch      # ✅ Push to YOUR fork

# NEVER do this (unless explicitly collaborating)
git push upstream feature/your-branch    # ❌ DON'T push to upstream
```

**Rationale:** Це fork для особистих process improvements, експериментів, та customization. Ми можемо вільно вносити зміни без обмежень upstream проєкту.

---

## Project Overview

**BMAD-METHOD** - Business Management Agile Design Method platform for AI-assisted product development.

**This Fork Focus:**

- Production process improvements для documentation-heavy проєктів
- Trusted repository patterns для fork maintainers
- Process optimization frameworks (Value Stream Mapping, TOC, Agile)
- Integration experiments (Beads ↔ BMad ↔ Git ↔ CI/CD)

**Key Documentation:**

- `docs/discussions/` - Process improvement discussions
- `.beads/` - Issue tracking database (prefix: BMAD-METHOD)
- `.claude/skills/bd-issue-tracking/` - Beads skill для persistent memory

---

## Beads Integration

**Issue Tracker:** Beads (bd) для persistent task tracking across sessions.

### MCP Server Available

Beads MCP server надає tools для AI agents:

- `mcp__plugin_beads_beads__set_context` - Set workspace context
- `mcp__plugin_beads_beads__ready` - Get ready-to-work tasks
- `mcp__plugin_beads_beads__create` - Create new issues
- `mcp__plugin_beads_beads__update` - Update issue status/notes
- `mcp__plugin_beads_beads__show` - Get issue details
- `mcp__plugin_beads_beads__close` - Close completed issues

**Always call `set_context` before using other MCP tools:**

```
mcp__plugin_beads_beads__set_context("/Users/sd/github/BMAD-METHOD")
```

### Skill Available

**Location:** `.claude/skills/bd-issue-tracking/`

**Use the skill when:**

- Starting new session (check `bd ready`, `bd list --status in_progress`)
- Creating issues for multi-session work
- Documenting complex dependencies
- Need persistent memory across compaction cycles

**Skill provides:**

- Complete bd CLI reference
- Decision criteria (bd vs TodoWrite)
- Session handoff protocols
- Compaction survival strategies

**Activation:**

```bash
# Claude Code detects skill automatically
# Or invoke explicitly if needed
```

### When to Use Beads vs TodoWrite

**Use Beads (bd) when:**

- ✅ Work spans multiple sessions or days
- ✅ Complex dependencies exist (blockers, epics, subtasks)
- ✅ Need persistent context after compaction
- ✅ Strategic/fuzzy work with evolving requirements

**Use TodoWrite when:**

- ✅ Single-session tactical tasks
- ✅ Linear execution (no branching)
- ✅ All context in current conversation
- ✅ Simple progress tracking

**Golden rule:** Якщо робота може бути забута після compaction, це критична втрата → use Beads.

### Session Start Protocol

**Every session start in BMAD-METHOD:**

1. Set beads context (MCP):

   ```
   mcp__plugin_beads_beads__set_context("/Users/sd/github/BMAD-METHOD")
   ```

2. Check ready work:

   ```
   mcp__plugin_beads_beads__ready()
   ```

3. Check in-progress work:

   ```
   mcp__plugin_beads_beads__list(status="in_progress")
   ```

4. Report to user:
   ```
   "Found X items ready: [summary]"
   "Issue Y in progress: [last session notes]. Continue?"
   ```

**Never skip session start checks** - це foundation для continuity після compaction.

---

## Language Policy

**Communication:** Ukrainian
**Code/Variables/Functions:** English
**Documentation:** Ukrainian (discussions, guides), English (technical specs, code comments)
**Commit Messages:** English (conventional commits format)

**Why?** Українська для стратегічного thinking та communication, English для universal code/tech standards.

---

## Git Workflow

**Branch Strategy:**

- `main` - stable fork state (synced from upstream periodically)
- `feature/*` - experimental branches (push to origin)
- `sync/upstream-*` - temporary branches для pulling upstream changes

**Commit Standards:**

```
<type>(<scope>): <subject>

[optional body]
```

**Types:** feat, fix, docs, chore, refactor, test, ci

**Example:**

```
feat(process): add production process metrics framework

Implement metrics framework for documentation-heavy projects
based on Agile and Theory of Constraints insights.

Related: BMAD-METHOD-c4q
```

**Co-Authoring:** Optional (не автоматично). Додавайте manually якщо потрібно.

---

## Development Principles

### 1. Brutal Honesty

- **NO ASSUMPTIONS** - Verify, don't assume
- **NO OUTDATED DOCS** - Call out inconsistencies immediately
- **ADMIT IGNORANCE** - "Don't know" → ask, don't fabricate
- **REALITY CHECK** - Test claims against reality

### 2. Quality > Speed

- Complete одну feature повністю перед наступною
- Test before moving on
- Prefer working solution над красивою теорією

### 3. Beads for Memory

- Multi-session work → Beads issue (з notes field!)
- Single session task → TodoWrite
- Checkpoint progress перед compaction (70%+ token usage)

### 4. Documentation Standards

**For discussions (this fork):**

- Store in `docs/discussions/YYYY-MM-DD-topic.md`
- Include: Date, Context, Participants (agents), Insights, Next Steps
- Reference related Beads issues

**For code/workflows (upstream compatibility):**

- Follow BMAD Method conventions
- YAML for configs (`.bmad/` structure)
- Markdown for documentation
- XML for workflow instructions

---

## Fork-Specific Workflows

### Syncing from Upstream

```bash
# Add upstream remote (once)
git remote add upstream https://github.com/bmad-code-org/BMAD-METHOD.git

# Fetch upstream changes
git fetch upstream

# Create sync branch
git checkout main
git checkout -b sync/upstream-YYYY-MM-DD

# Merge upstream/main
git merge upstream/main

# Resolve conflicts (prioritize fork customizations)
# Test thoroughly
# Push to origin
git push origin sync/upstream-YYYY-MM-DD

# Create PR to merge into fork main (review changes)
# After merge, delete sync branch
```

### Sharing Insights with Upstream (Optional)

Якщо process improvements виявляються корисними:

1. Create clean feature branch від upstream/main
2. Cherry-pick relevant commits (without fork-specific customizations)
3. Open PR до upstream **ONLY if explicitly valuable to community**
4. Describe clearly: problem solved, approach, benefits

**Default:** Keep improvements in fork unless compelling reason to share.

---

## Production Process Tracking

**Current Focus:** Production process improvements (Epic: BMAD-METHOD-ive)

**Active Issues:**

- `BMAD-METHOD-8on` - Trusted Repository Pattern docs
- `BMAD-METHOD-c4q` - Production Metrics Framework docs
- `BMAD-METHOD-3ti` - Strategic Shifts for Knowledge Work docs

**Check status:**

```bash
bd ready --priority 2
bd show BMAD-METHOD-ive
```

**Update progress:**

```bash
bd update BMAD-METHOD-8on --status in_progress
bd update BMAD-METHOD-8on --notes "COMPLETED: ... IN PROGRESS: ... NEXT: ..."
```

---

## Useful Resources

### Internal Documentation

- `docs/discussions/` - Process discussions and insights
- `.beads/issues.jsonl` - Issue tracking database
- `.claude/skills/bd-issue-tracking/` - Beads skill reference

### Upstream Resources

- **Docs:** `docs/` (upstream BMAD documentation)
- **Bundles:** https://bmad-code-org.github.io/bmad-bundles/
- **GitHub:** https://github.com/bmad-code-org/BMAD-METHOD

### Related Projects

- **KRTM:** https://github.com/joyshmitz/krtm (context for process improvements)
- **Beads:** https://github.com/bmad-code-org/beads (issue tracker)

---

## Common Tasks

### Working on Process Improvements

1. Check ready issues: `bd ready`
2. Show issue details: `bd show BMAD-METHOD-XXX`
3. Mark in progress: `bd update BMAD-METHOD-XXX --status in_progress`
4. Work on task (create docs, code, etc.)
5. Update notes at milestones
6. Commit changes with issue reference
7. Close when complete: `bd close BMAD-METHOD-XXX`

### Creating New Discussion Documents

```bash
# Template location
docs/discussions/YYYY-MM-DD-topic.md

# Create beads issue first
bd create "Discussion: Topic Name" -t task -p 2

# Write document
# Link to beads issue in document
# Update beads notes with key insights

# Commit
git add docs/discussions/
git commit -m "docs: add discussion on topic name

Key insights: ...

Related: BMAD-METHOD-XXX"
```

### Testing Workflows

```bash
# Run all tests (upstream quality gates)
npm test

# Specific test suites
npm run test:schemas
npm run test:install
npm run validate:bundles
npm run lint
npm run format:check
```

---

## Red Flags to Avoid

🚫 **Pushing to upstream** (unless explicitly collaborating)
🚫 **Multiple tasks simultaneously** (complete one first)
🚫 **Assumptions without verification**
🚫 **Forgetting to update beads notes** (before compaction)
🚫 **Using TodoWrite for multi-session work** (use Beads instead)

---

## Contact and Support

**Fork Maintainer:** @joyshmitz (GitHub)
**Upstream Project:** @bmad-code-org
**Issues:** Track in `.beads/` (local), or GitHub Issues (for collaboration)

---

**Goal:** Experiment freely, improve production processes, capture insights in Beads, maintain high quality, share learnings when valuable.

**Version:** 1.0.0
**Last Updated:** 2025-11-12 17:50:00 EET
**Repository Type:** Personal Fork (Experimental)
**Issue Tracker:** Beads (bd CLI + MCP Server + Skill)
