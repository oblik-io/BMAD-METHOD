<!-- BMAD BMM Documentation Index (doc-index) Workflow Instructions -->

````xml
<critical>The workflow execution engine is governed by: {project_root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {installed_path}/workflow.yaml</critical>
<critical>This workflow scans generated documentation AFTER agents/workflows have produced them, then builds/updates a categorized, tagged Markdown index at {output_file}.</critical>
<critical>Default: non-interactive, incremental true. Always prefer regeneration over prompts. If discovery fails, HALT with clear message.</critical>

<workflow>

  <step n="1" goal="Resolve inputs and discover candidates">
    <action>Resolve variables: scan_dirs, include_globs, exclude_globs, output_file, category_patterns, max_desc_words, incremental.</action>
    <action>For each directory in {{scan_dirs}}: recursively GLOB include_globs then filter out exclude_globs and hidden files. Limit to markdown files (.md, .mdx).</action>
    <action>Normalize paths to be relative to project root and use forward slashes.</action>
    <check>HALT if no candidate files found: "No documentation files found under configured scan_dirs"</check>
  </step>

  <step n="2" goal="Extract metadata and categorize">
    <action>For each candidate file:
      - READ the file
      - Extract title: first level-1 heading (# ...) or first non-empty line
      - Extract a brief description: summarize opening paragraph or first section to {{max_desc_words}} words (do NOT invent domain facts)
      - Compute last_updated from file mtime
      - Infer categories from filename/content using {{category_patterns}} (lowercase filename + headings). Assign the BEST single archetype; if strong signals for several, pick primary and add others as tags
      - Compute tags: derive from keywords (e.g., api, security, ci, ux, db, testing, nfr, performance, accessibility, mobile, backend, frontend, devops, adr)
    </action>
    <action>Build a data record for each file: { path, title, description, category, tags[], last_updated }</action>
    <action>Keep a deduplicated set by normalized relative path.</action>
  </step>

  <step n="3" goal="Merge with existing index (if incremental)">
    <action>If {{incremental}} and {output_file} exists: READ file and locate the Machine Index JSON code block fenced as ```json doc-index ... ```</action>
    <action>If present, PARSE JSON into priorIndex. Merge: update entries for changed files, add new files, remove entries for missing files under current scan scope. Preserve prior tags if not conflicting. If absent or parse fails, treat as full rebuild.</action>
  </step>

  <step n="4" goal="Render Markdown index using template">
    <action>Initialize {output_file} from template if creating new. If updating, rebuild complete content to avoid drift.</action>
    <action>Write a Machine Index JSON code block at the top using fence label "json doc-index" with schema: { version, generated_at, project_root: "{project-root}", files: [ { path, title, description, category, tags, last_updated } ] }</action>
    <action>Under each archetype section in the template (Architecture, Requirements, Design, Testing & QA, API, Data, Security, Development, Operations, Decisions, Planning, Knowledge, Other):
      - Sort entries alphabetically by title
      - Emit bullets: "- [Title](./relative/path) — short description [tags: tag1, tag2]"
      - If a category has no entries, leave section with a note "(none indexed)"</action>
    <action>Place a Tag Glossary at the bottom: List unique tags alphabetically with brief meaning derived from first occurrence context (one short phrase each).</action>
  </step>

  <step n="5" goal="Validate and save">
    <invoke-task optional="true">Optionally run helper task at bmad/core/tasks/index-docs.xml for baseline grouping; then prefer doc-index results for final output.</invoke-task>
    <invoke-task>Validate against checklist at {installed_path}/checklist.md using bmad/core/tasks/validate-workflow.xml</invoke-task>
    <action>Save to {output_file}. Report total indexed files and categories coverage.</action>
  </step>

</workflow>
````
