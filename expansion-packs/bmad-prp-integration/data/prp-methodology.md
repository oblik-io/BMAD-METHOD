# PRP Methodology for BMad Integration

## Overview

This document outlines the PRP (Product Requirement Prompt) methodology as implemented in PRPs-agentic-eng and how it integrates with BMad-Method's structured planning approach.

## PRP Core Principles

### 1. Context is King
- **Comprehensive Context**: Every PRP must contain ALL necessary documentation, examples, and caveats
- **Information Density**: Use keywords and patterns from the codebase
- **Context Completeness**: "If someone knew nothing about this codebase, would they have everything needed to implement this successfully?"

### 2. Validation Loops
- **Executable Validation**: Provide executable tests/lints the AI can run and fix
- **Progressive Success**: Start simple, validate, then enhance
- **Quality Gates**: Multiple validation levels (syntax → tests → integration)

### 3. One-Pass Implementation
- **Complete Context**: All implementation details included in PRP
- **Clear Requirements**: Specific, measurable success criteria
- **Actionable Tasks**: Detailed implementation blueprint with dependencies

## PRP Structure

### Goal Section
```
**Feature Goal**: [Specific, measurable end state]
**Deliverable**: [Concrete artifact - API endpoint, service class, etc.]
**Success Definition**: [How you'll know this is complete and working]
```

### Why Section
- Business value and user impact
- Integration with existing features
- Problems this solves and for whom

### What Section
- User-visible behavior and technical requirements
- Success criteria with specific measurable outcomes

### All Needed Context Section
```
### Context Completeness Check
_Before writing this PRP, validate: "If someone knew nothing about this codebase, would they have everything needed to implement this successfully?"_

### Documentation & References
- url: [Complete URL with section anchor]
  why: [Specific methods/concepts needed for implementation]
  critical: [Key insights that prevent common implementation errors]

- file: [exact/path/to/pattern/file.py]
  why: [Specific pattern to follow - class structure, error handling, etc.]
  pattern: [Brief description of what pattern to extract]
  gotcha: [Known constraints or limitations to avoid]

### Known Gotchas
# CRITICAL: [Library name] requires [specific setup]
# Example: FastAPI requires async functions for endpoints
```

### Implementation Blueprint Section
```
### Data models and structure
Create the core data models, we ensure type safety and consistency.

### Implementation Tasks (ordered by dependencies)
Task 1: CREATE src/models/{domain}_models.py
Task 2: IMPLEMENT src/services/{domain}_service.py
Task 3: ADD src/api/{domain}_endpoints.py
```

### Validation Loop Section
```
### Level 1: Syntax & Style
ruff check src/ --fix
mypy src/

### Level 2: Unit Tests
uv run pytest tests/test_{domain}.py -v

### Level 3: Integration Test
curl -X POST http://localhost:8000/{domain}/create \
 -H "Content-Type: application/json" \
 -d '{"field": "value"}'
```

## Integration with BMad-Method

### Story to PRP Conversion

#### Mapping BMad Story Components
- **Story Statement** → **Goal Section**
- **Acceptance Criteria** → **Success Criteria**
- **Dev Notes** → **All Needed Context**
- **Tasks/Subtasks** → **Implementation Blueprint**
- **Testing Requirements** → **Validation Loop**

#### Context Preservation
- **Architecture Documents**: Map BMad architecture context to PRP format
- **Technical Constraints**: Preserve all technical constraints and gotchas
- **Implementation Patterns**: Maintain existing code patterns and conventions
- **Testing Standards**: Convert BMad testing requirements to PRP validation

### PRP to Story Conversion

#### Mapping PRP Results to BMad
- **Implementation Results** → **Dev Agent Record**
- **Validation Results** → **QA Review**
- **Generated Artifacts** → **Story Completion Notes**
- **Performance Metrics** → **Story Validation Results**

#### Quality Assurance
- **Code Quality**: Validate against BMad coding standards
- **Test Coverage**: Ensure test coverage meets BMad requirements
- **Integration Testing**: Verify integration with existing BMad workflow
- **Documentation**: Update BMad story documentation with results

## Best Practices

### PRP Creation
1. **Start with BMad Story**: Use BMad story as foundation
2. **Enhance Context**: Add comprehensive context and examples
3. **Validate Completeness**: Ensure context completeness check passes
4. **Test Validation Loops**: Verify validation loops are executable
5. **Maintain Traceability**: Keep links to original BMad story

### PRP Execution
1. **Environment Setup**: Ensure proper execution environment
2. **Context Validation**: Verify all context is available
3. **Progressive Validation**: Run validation loops progressively
4. **Error Handling**: Handle errors and provide recovery options
5. **Result Collection**: Collect and validate execution results

### Result Integration
1. **Quality Validation**: Validate results against BMad standards
2. **Context Mapping**: Map results back to BMad story format
3. **Documentation Update**: Update story with execution results
4. **Workflow Continuation**: Prepare for next BMad workflow phase

## Validation Standards

### Context Completeness
- [ ] All necessary documentation included
- [ ] Code examples and patterns provided
- [ ] Technical constraints documented
- [ ] Validation loops executable
- [ ] Information density sufficient

### Implementation Quality
- [ ] Code follows project patterns
- [ ] Tests cover all requirements
- [ ] Performance meets standards
- [ ] Security requirements met
- [ ] Documentation complete

### Integration Consistency
- [ ] BMad story requirements preserved
- [ ] Architecture context maintained
- [ ] Testing standards followed
- [ ] Quality gates passed
- [ ] Traceability maintained

## Error Handling

### Context Issues
- **Missing Documentation**: Request additional documentation
- **Incomplete Context**: Enhance context with examples
- **Outdated Information**: Update context with current information

### Execution Issues
- **Environment Problems**: Fix execution environment
- **Dependency Issues**: Resolve missing dependencies
- **Validation Failures**: Address validation issues

### Integration Issues
- **Format Mismatches**: Handle format conversion issues
- **Context Loss**: Preserve context during conversion
- **Quality Issues**: Address quality and compliance issues

## Success Metrics

### Conversion Quality
- **Context Preservation**: 95%+ context preserved during conversion
- **Format Compliance**: 100% PRP format compliance
- **Validation Completeness**: All validation loops executable
- **Traceability**: Full traceability between frameworks

### Execution Success
- **Success Rate**: 90%+ successful PRP executions
- **Quality Compliance**: 95%+ quality standards met
- **Performance**: <10% overhead on execution time
- **Error Recovery**: 80%+ error recovery success rate

### Integration Effectiveness
- **Workflow Continuity**: Seamless workflow integration
- **Quality Maintenance**: Maintained quality standards
- **User Experience**: Improved development experience
- **Productivity**: Increased development productivity 