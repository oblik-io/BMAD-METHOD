# BMAD-METHOD × OpenCode (SST) Integration Plan (JSON-only)

This plan delivers first-class OpenCode CLI/TUI integration for BMAD-METHOD using a project-level `opencode.json`/`opencode.jsonc` — no Markdown generation fallback. It mirrors our Codex integration goals and prioritizes file references to BMAD sources so updates flow automatically.

## Objectives

- Generate/merge a project-level OpenCode config with BMAD agents and commands.
- Use file references (`{file:...}` and `@file`) to avoid duplicating BMAD content.
- Support all relevant agent/command options in OpenCode JSON.
- Be idempotent and non-destructive when a project already has `opencode.json(c)`.
- Minimize name collisions; optionally prefix names with `bmad-`.

## References

- Config: https://opencode.ai/docs/config/
- Agents: https://opencode.ai/docs/agents/#configure
- Commands: https://opencode.ai/docs/commands/

## High-Level Approach

1. Add a new IDE target `opencode` in the installer.
2. Detect an existing project-level `opencode.jsonc` or `opencode.json`; if none, create `opencode.jsonc`.
3. Merge BMAD agents and commands into the config using file references to BMAD source files.
4. Preserve user entries; only add or update BMAD-managed keys.
5. Support expansion packs using the same mapping and relative path logic.

## Path mapping (source → installed)

- Source in this repo: `bmad-core/...` and `expansion-packs/...`.
- Installed in a user project: `.bmad-core/...` and `.bmad-core/expansion-packs/...`.
- All `opencode.json(c)` references must target the installed `.bmad-core/...` paths and be POSIX-style, `./`-prefixed relative to the project root.

## Mapping BMAD → OpenCode (JSON-only)

- Agents (from `.bmad-core/agents/*.md` and expansion packs) → `agent` entries:
  - Key: agent ID (optionally with prefix, e.g., `bmad-dev`).
  - Fields supported:
    - `description`: from BMAD YAML `whenToUse` or a generated fallback.
  - `mode`: `primary` | `subagent` (map core roles to `primary`, specialists to `subagent`).
    - `prompt`: `{file:./relative/path/to/.bmad-core/agents/{agent}.md}` (or expansion path).
    - Optional: `model`, `temperature`.
  - `tools`: conservative defaults `{ write: true, edit: true, bash: true }` (add more later as needed).
    - `permission`: `{ edit: allow|ask|deny, bash: allow|ask|deny|{pattern map}, webfetch: allow|ask|deny }`.
    - Provider-specific options pass through unchanged.

- Commands (from `.bmad-core/tasks/*.md`, `common/tasks/*.md`, and expansion tasks) → `command` entries:
  - Key: task ID (optionally with prefix, e.g., `bmad-test-design`).
  - Fields supported:
  - `template`: `{file:./relative/path/to/task.md}` (use `{file:...}` consistently).
    - `description`: from the task’s heading/summary or a generated fallback.
  - `agent`: optional; set explicitly where sensible (e.g., `dev`, `pm`, `qa`). If omitted, OpenCode’s default applies.
    - `model`: optional override per command.

## Project Config Creation/Merge Strategy

- Detection order: `opencode.jsonc` → `opencode.json` → create `opencode.jsonc`.
- `$schema`: `https://opencode.ai/config.json`.
- Existing project config present:
  - Only add BMAD `agent` and `command` entries.
  - Ensure `instructions` includes the single entry: `.bmad-core/core-config.yaml` (append if missing).
  - Do not add or modify other top-level fields (e.g., `theme`, `model`, `small_model`, `permission`).
  - Idempotent: preserve user entries and comments; never remove non-BMAD entries.
- No project config present:
  - Create a minimal `opencode.jsonc` containing:
    - `$schema`: `https://opencode.ai/config.json`
    - `instructions`: [ ".bmad-core/core-config.yaml" ]
    - `agent`: { ...BMAD agents... }
    - `command`: { ...BMAD commands... }
  - Intentionally do NOT set `theme`, `model`, `small_model`, or `permission` here to avoid overriding a global configuration.
  - Paths must be relative to the project root.

## Defaults for Tools & Permissions

- dev/build-like agents: `tools: { write: true, edit: true, bash: true }`, `permission: { edit: "allow", bash: "ask" }`.
- pm/analyst/plan: `tools: { write: false, edit: false, bash: false }`, `permission: { edit: "deny", bash: "deny" }`.
- qa: `tools: { write: true, edit: true, bash: false }`, `permission: { edit: "ask", bash: "deny" }`.
- reviewer/read-only: `tools: { write: false, edit: false, bash: false }`, `permission: { edit: "deny", bash: "deny" }`.

## Installer UX & Flow

- When `opencode` is selected:
  - Detect `opencode.jsonc` or `opencode.json` at project root.
  - If config exists: add BMAD `agent`/`command` and ensure `.bmad-core/core-config.yaml` is present in `instructions` (no other top-level changes).
  - If config does not exist: create minimal `opencode.jsonc` with `$schema`, `instructions: [".bmad-core/core-config.yaml"]`, `agent`, and `command`.
  - Ask: “Prefix agent/command names with `bmad-`?” (default: off).
  - Output a summary of added/updated/skipped entries and the config file path.

## Implementation Plan (code)

1. Config entry: add `opencode` to `tools/installer/config/install.config.yaml` with a brief description.
2. Switch wiring: in `tools/installer/lib/ide-setup.js`, add `case 'opencode': return this.setupOpenCode(installDir, selectedAgent, { prefix });`.
3. Implement `setupOpenCode(installDir, selectedAgent, { prefix })`:
   - Resolve project root, detect existing OpenCode config file.
   - Parse with a JSONC-capable parser (e.g., `jsonc-parser` or `comment-json`).
   - Build BMAD agent and command maps using existing helpers (agents/tasks from core + expansion packs).
   - Apply defaults (tools/permissions) by agent category.
   - Merge into `agent`/`command` sections (idempotent, preserve user entries).
   - Write back preserving comments/format when possible.
4. Docs: update `docs/user-guide.md` with an OpenCode section describing usage in JSON mode and re-run behavior.
5. Optional: add npm script if `package.json` exists: `"bmad:opencode": "bmad-method install -f -i opencode"`.

## JSONC Example (minimal project-level config)

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "instructions": [ ".bmad-core/core-config.yaml" ],
  "agent": {
    "dev": {
      "description": "Product development / implementation agent",
      "mode": "primary",
      "prompt": "{file:./.bmad-core/agents/dev.md}",
      "tools": { "write": true, "edit": true, "bash": true },
      "permission": { "edit": "allow", "bash": "ask" }
    },
    "pm": {
      "description": "Product management and planning agent",
      "mode": "primary",
      "prompt": "{file:./.bmad-core/agents/pm.md}",
      "tools": { "write": false, "edit": false, "bash": false },
      "permission": { "edit": "deny", "bash": "deny" }
    }
  },
  "command": {
    "review-changes": {
      "description": "Review recent changes",
      "agent": "dev",
      "template": "{file:./.bmad-core/tasks/review-changes.md}"
    },
    "test-design": {
      "description": "Design tests based on the test levels framework",
      "agent": "qa",
      "template": "{file:./.bmad-core/tasks/test-design.md}"
    }
  }
}

## Name collisions and BMAD-managed detection

- Collision handling (when prefix is off):
  - If an unprefixed key exists and is not BMAD-managed → skip and report a collision; suggest re-run with `--prefix bmad-`.
  - If a key is BMAD-managed → update it idempotently.
- BMAD-managed detection heuristics:
  - Agent with `prompt` referencing `.bmad-core/agents` or `.bmad-core/expansion-packs/.../agents`.
  - Command with `template` referencing `.bmad-core/tasks` or `.bmad-core/expansion-packs/.../tasks`.

## Acceptance Criteria

- Selecting `Opencode` merges BMAD agents/commands into a project’s `opencode.json(c)` or creates a new `opencode.jsonc`.
- Agents reference BMAD agent files via `prompt: {file:...}`; commands reference tasks via `template`.
- Doc updates describe how to use the integration and how it behaves on updates.
```
