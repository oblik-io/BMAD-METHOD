# doc-index Workflow

Builds or updates a categorized, tagged documentation index after agents have generated project documentation. The index helps downstream workflows (e.g., create-story, story-context) quickly locate authoritative docs.

- Output: `docs/doc-index.md`
- Categories: Architecture, Requirements, Design, Testing & QA, API, Data, Security, Development, Operations, Decisions, Planning, Knowledge, Other
- Includes a machine-readable `json doc-index` code block at the top.

## Run

```bash
bmad sm doc-index
# or the alias
bmad sm update-doc-index
```

## Notes

- Safe to rerun anytime; defaults to incremental, but rebuilds full file content for consistency.
- Workflows `create-story` and `story-context` will preferentially consult this index when present.
