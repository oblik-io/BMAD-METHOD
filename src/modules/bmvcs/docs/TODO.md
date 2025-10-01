# BMVCS Module - TODO List

**Last Updated:** 2025-10-01
**Status:** Active Development
**Current Phase:** Phase 3 Planning

---

## High Priority

### Path Fix (Session 4)

**Status:** Ready for execution
**Plan:** See `BMM_AGENTS_VCS_CONFIG_PATH_FIX.md`

- [ ] Fix path in `src/modules/bmm/agents/architect.md` (line 68)
- [ ] Fix path in `src/modules/bmm/agents/pm.md` (line 68)
- [ ] Fix path in `src/modules/bmm/agents/dev.md` (line 73)
- [ ] Change: `bmad-core/vcs-config.yaml` → `.bmad/vcs-config.yaml`
- [ ] Test integration without workaround in test-bmvcs-install
- [ ] Remove workaround directory (`bmad-core/`) from test repo
- [ ] Verify all BMM agents work seamlessly

**Estimated Time:** 15-25 minutes

---

## Phase 3: Documentation & Quality

### 3.1 User Documentation (In Progress)

**Research Complete:** ✅ KB Mode found and analyzed

#### KB Mode Extension

- [ ] Design BMVCS additions to `.bmad-core/data/bmad-kb.md`
- [ ] Add "VCS-Aware Agents" section to KB
- [ ] Update "Agents" topic (#4) with VCS examples
- [ ] Add workflow-specific adaptation explanations
- [ ] Test KB Mode with BMVCS content

**Reference:** `KB_MODE_RESEARCH_FINDINGS.md`

#### BMM Integration Guide

- [ ] Create `BMM_INTEGRATION_GUIDE.md` in appropriate location
- [ ] Document VCS Adapter usage
- [ ] Add BMM + BMVCS integration patterns
- [ ] Include examples per workflow (GitHub Flow, GitFlow, Trunk-Based)
- [ ] Add troubleshooting section

#### Quick Start & Troubleshooting

- [ ] Create `QUICK_START.md` for BMVCS
- [ ] Create `TROUBLESHOOTING.md` with common issues
- [ ] Add real project examples
- [ ] Create video/GIF demos (optional)

**Estimated Time:** 2-3 hours total

---

### 3.2 Developer Documentation

- [ ] Document VCS Adapter Agent architecture
- [ ] Explain template adaptation mechanism
- [ ] Detail confidence scoring algorithm (if not already in VCS_DETECTION_CONFIDENCE.md)
- [ ] Add contribution guidelines for BMVCS
- [ ] Document template development guide
- [ ] Add API/interface contracts

**Deliverables:**

- `ARCHITECTURE.md` (or expand existing docs)
- `TEMPLATE_GUIDE.md`
- `CONTRIBUTING.md`

**Estimated Time:** 2 hours

---

### 3.3 API Documentation

- [ ] Document `vcs-config.yaml` schema formally
- [ ] Document template YAML schema
- [ ] Add inline JSDoc comments to code
- [ ] Create schema validation files
- [ ] Generate API reference

**Deliverables:**

- `schemas/vcs-config.schema.json`
- `schemas/template.schema.json`
- `API_REFERENCE.md`

**Estimated Time:** 2 hours

---

### 3.4 Automated Testing

- [ ] Create test suite for each workflow
- [ ] Add YAML validation tests
- [ ] Create template loading tests
- [ ] Add integration tests with mock BMM agents
- [ ] Performance benchmarks
- [ ] CI/CD pipeline setup

**Deliverables:**

- `tests/workflows/` - Workflow tests
- `tests/templates/` - Template tests
- `tests/integration/` - Integration tests
- `.github/workflows/test-bmvcs.yml` - CI pipeline

**Estimated Time:** 3-4 hours

---

### 3.5 Performance Optimization

- [ ] Profile template loading
- [ ] Optimize large document adaptation
- [ ] Cache configuration when possible
- [ ] Test with repos >100K files
- [ ] Benchmark all operations
- [ ] Document performance characteristics

**Target Metrics:**

- Discovery: < 2 seconds
- Validation: < 1 second
- Adaptation: < 5 seconds for large docs
- Config load: < 100ms

**Estimated Time:** 2-3 hours

---

## Documentation Standards (Future)

### Naming Conventions

- [ ] Review and apply `SESSION_END_PROTOCOL.md` naming if applicable
- [ ] Apply `DOCUMENTATION_CONVENTIONS.md` sequential numbering (01-99) if needed
- [ ] Standardize document naming across module
- [ ] Ensure consistency with BMAD v6 module standards

### README Updates

- [ ] Update `src/modules/bmvcs/docs/README.md` with new documents
- [ ] Add links to research findings
- [ ] Add links to TODO (this file)
- [ ] Organize by category (Principles, Research, Plans, Guides)

### Metadata

- [ ] Add creation dates to all docs
- [ ] Add "Last Updated" timestamps
- [ ] Add version numbers where appropriate
- [ ] Add status indicators (Draft, Review, Final)

---

## Future Enhancements (Post-Phase 3)

### SM/TEA Agent Integration (Optional)

- [ ] Evaluate if SM agent needs VCS awareness
- [ ] Evaluate if TEA agent needs VCS awareness
- [ ] Document decision and rationale

**Context:** Currently 3/5 BMM agents have VCS integration (Architect, PM, Dev). SM and TEA don't have it by design.

### Additional VCS Support

- [ ] SVN workflow templates
- [ ] Perforce workflow templates
- [ ] Mercurial workflow templates
- [ ] Custom workflow enhancement

### Advanced Features

- [ ] Auto-detection enhancement
- [ ] Migration guides between workflows
- [ ] Team collaboration patterns
- [ ] Multi-repo scenarios

---

## Completed Tasks

### Phase 2: Alpha Testing ✅

- [x] Core BMVCS functionality tested
- [x] VCS Adapter Agent tested (sections 2.1-2.5)
- [x] BMM integration tested (sections 2.6-2.9)
- [x] Path inconsistency discovered and documented
- [x] Workaround created for immediate use
- [x] All test results documented in `~/test-bmvcs-install/testing/`

### Research & Planning ✅

- [x] KB Mode research completed (KB_MODE_RESEARCH_FINDINGS.md)
- [x] Path fix plan created (BMM_AGENTS_VCS_CONFIG_PATH_FIX.md)
- [x] Phase 3 strategy defined
- [x] Documentation structure organized

---

## Notes

- **Test Repository:** `~/test-bmvcs-install/` contains all alpha test results
- **Session Documentation:** See `SESSION_END_*.md` files in test repo
- **Branch:** All work on `feat/bmvcs-dev`
- **Integration:** Path fix required before Phase 3.1 implementation (but not planning)

---

**Priority Order for Next Sessions:**

1. **Session 4:** Execute path fix (enables testing)
2. **Session 5+:** Implement Phase 3.1 (user documentation)
3. **Later:** Phase 3.2-3.5 (developer docs, testing, performance)

---

**Generated:** 2025-10-01 18:45:00 EEST
**Module:** BMVCS (BMAD VCS Adapter)
**Status:** Phase 3 Planning → Ready for Session 4
