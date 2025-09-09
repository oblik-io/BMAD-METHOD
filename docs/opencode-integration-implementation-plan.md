# OpenCode Integration Implementation Plan (Single PR, Small Commits)

This document describes how we’ll implement the OpenCode (SST) integration for BMAD-METHOD in a single PR composed of small, focused commits that comply with the repository’s CONTRIBUTING guidelines.

## Scope and Constraints

- JSON-only project-level integration (no Markdown generation).
- Existing project `opencode.json(c)`:
  - Only add BMAD `agent` and `command` entries.
  - Ensure `instructions` includes a single entry: `.bmad-core/core-config.yaml`.
  - Do not modify other top-level fields (e.g., `theme`, `model`, `small_model`, `permission`).
- No project `opencode.json(c)`:
  - Create a minimal `opencode.jsonc` with `$schema`, `instructions: [".bmad-core/core-config.yaml"]`, and `agent`/`command` populated.
  - Intentionally omit top-level `theme`, `model`, `small_model`, and `permission` to avoid overriding a global config.
- Idempotent behavior: safe re-runs; no duplication; preserve user entries and JSONC comments.
- Path mapping: Source is `bmad-core/...` in this repo; installed project references must use `.bmad-core/...` with POSIX-style `./`-prefixed relative paths.

## Single-PR Strategy

- Base branch: `next` (per CONTRIBUTING recommendations for new features).
- One PR containing ~6–9 small commits; each commit is independently reviewable and keeps the PR within the 200–400 LOC ideal (max 800 LOC).
- Each commit runs the standard validation: `npm run pre-release` (or at minimum `npm run format:check` and `npm run lint`).

## Commit-by-Commit Plan

1. docs(opencode): add implementation plan (this file)

- Goal: Check in the execution plan to guide the PR.
- Files: `docs/opencode-integration-implementation-plan.md`
- Validation: `npm run format:check` and `npm run lint`

2. feat(installer): register opencode target (metadata only)

- Goal: Add `opencode` to installer config (no runtime behavior yet).
- Files: `tools/installer/config/install.config.yaml`
- Validation: `npm run lint`

3. chore(deps): add JSONC support for config IO

- Goal: Add dependency to parse/write JSONC while preserving comments.
- Choice: `comment-json` (parse + stringify with comments)
- Files: `package.json` (+ lockfile updates by package manager)
- Validation: install completes; `npm run lint`

4. feat(installer): scaffold opencode handler (detect-only)

- Goal: Wire `case 'opencode'` and add `setupOpenCode()` with dry-run detection/logging (no write operations yet).
- Files: `tools/installer/lib/ide-setup.js`
- Validation: run the installer in a test repo; verify it detects an existing or missing config and exits without modifications.

5. feat(installer): minimal config creation/merge (instructions only)

- Goal:
  - If config exists: ensure `instructions` contains `.bmad-core/core-config.yaml` (append once).
  - If config is missing: create minimal `opencode.jsonc` with `$schema` and `instructions` only (empty `agent` and `command`).
- Files: `tools/installer/lib/ide-setup.js` (and optional `tools/installer/lib/opencode-config.js` helper)
- Validation: re-run safely; confirm idempotence.

6. feat(installer): add agent mapping + merge

- Goal: Map BMAD agents (core + expansions) to OpenCode `agent` entries with:
  - `description`, `mode`, `prompt: {file:...}`, default `tools`/`permission` by role.
  - Optional name prefix `bmad-`.
- Files: `tools/installer/lib/ide-setup.js` (and optional `tools/installer/lib/opencode-map.js` helper)
- Validation: verify agents are added once; re-run remains stable.

7. feat(installer): add command mapping + merge

- Goal: Map BMAD tasks to OpenCode `command` entries:
  - `template`: `{file:...}` (standardize on `{file:...}`; do not mix with `@file`).
  - `description` and optional `agent` per task.
- Files: `tools/installer/lib/ide-setup.js`
- Validation: verify commands are added once; re-run remains stable.

8. feat(installer): polish UX (prefix prompt + summary)

- Goal: Add a prompt to apply `bmad-` prefix to names; output a concise summary of added/updated/skipped entries and config path.
- Files: `tools/installer/lib/ide-setup.js`
- Validation: manual smoke in a test repo with and without pre-existing config.

9. docs(opencode): user guide update (JSON-only usage)

- Goal: Add a short OpenCode section in `docs/user-guide.md` describing usage and re-run behavior.
- Files: `docs/user-guide.md`
- Validation: `npm run format:check` and `npm run lint`

## Technical Details & Contracts

- Config detection order: `opencode.jsonc` → `opencode.json` → create `opencode.jsonc`.
- JSONC parsing/writing: use `comment-json` to preserve comments where present.
- Existing config path:
  - Only modify `instructions` (append `.bmad-core/core-config.yaml` if missing), `agent`, and `command` sections.
  - Never change top-level `theme`, `model`, `small_model`, or `permission`.
- New config path:
  - Create minimal file with `$schema`, `instructions`, `agent`, and `command`.
  - Exclude top-level `theme`, `model`, `small_model`, `permission`.
- Agent defaults (examples):
  - dev/build-like: `tools: { write: true, edit: true, bash: true }`, `permission: { edit: "allow", bash: "ask" }`
  - pm/analyst/plan: `tools: { write: false, edit: false, bash: false }`, `permission: { edit: "deny", bash: "deny" }`
  - qa: `tools: { write: true, edit: true, bash: false }`, `permission: { edit: "ask", bash: "deny" }`
- Commands: `template` references to BMAD tasks via `{file:...}` or `@file` strings; optional `agent` per task.
- Commands: `template` references use `{file:...}` consistently; optional `agent` per task (explicit where sensible).
- Prefix: Optional `bmad-` applied consistently to agent and command keys to avoid collisions.
- Idempotence: Re-runs should not duplicate or clobber user-defined entries; only update BMAD-managed keys.
- Mode values: restrict to `primary` and `subagent` unless spec confirms more.
- Default tools: minimal `{ write, edit, bash }` to avoid schema drift; extend later if needed.

### Collision strategy and BMAD-managed detection

- Collision handling (when prefix is off):
  - If an unprefixed key exists and is not BMAD-managed → skip and warn; suggest `--prefix bmad-`.
  - If a key is BMAD-managed → update idempotently.
- BMAD-managed detection:
  - Agent with `prompt` pointing into `.bmad-core/agents` or `.bmad-core/expansion-packs/.../agents`.
  - Command with `template` pointing into `.bmad-core/tasks` or `.bmad-core/expansion-packs/.../tasks`.

## Minimal JSONC Example (New Project Config)

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "instructions": [".bmad-core/core-config.yaml"],
  "agent": {
    "dev": {
      "description": "Product development / implementation agent",
      "mode": "primary",
      "prompt": "{file:./.bmad-core/agents/dev.md}",
      "tools": { "write": true, "edit": true, "bash": true },
      "permission": { "edit": "allow", "bash": "ask" },
    },
  },
  "command": {
    "test-design": {
      "description": "Design tests based on the test levels framework",
      "agent": "qa",
      "template": "{file:./.bmad-core/tasks/test-design.md}",
    },
  },
}
```

## Validation & QA

- Automated (prefer Bun, npm fallback):
  - `bun run format:check` (or `npm run format:check`)
  - `bun run lint` (or `npm run lint`)
  - Optionally `bun run pre-release` (or `npm run pre-release`)
- Manual smoke (in a temp repo):
  - With no `opencode.json(c)`: creates minimal JSONC, adds agents/commands.
  - With an existing `opencode.jsonc`: merges agents/commands and appends `.bmad-core/core-config.yaml` to `instructions` if missing; preserves other top-level fields and comments.
  - Re-run: no duplicates; only new/changed BMAD entries update.

## Acceptance Criteria

- Selecting `Opencode` integrates BMAD agents/commands into project-level `opencode.json(c)` or creates a minimal `opencode.jsonc`.
- Existing configs are preserved; only `instructions`, `agent`, and `command` are touched.
- Minimal new config contains only: `$schema`, `instructions`, `agent`, `command` (no theme/model/permission at top level).
- Idempotent behavior and expansion pack support are verified.
- User guide updated with JSON-only usage and re-run behavior.

## Out of Scope (Future)

- Markdown-based agent/command generation.
- Advanced provider-specific model settings at top-level.
- Force-overwrite behavior for colliding user-owned keys.
