# Convert Story to PRP Task

## Purpose

To convert a BMad-Method story into PRPs-agentic-eng format while preserving all requirements, context, and technical details. This task ensures that the PRP contains everything needed for one-pass implementation success through comprehensive context engineering.

## SEQUENTIAL Task Execution (Do not proceed until current Task is complete)

### 0. Load Configuration and Validate Input

- Load `{root}/core-config.yaml` from the project root
- Validate that the story file exists and is in correct BMad format
- Check that PRP output directory exists (`PRPs/`)
- Verify that all required templates and data files are available

### 1. Parse BMad Story Content

#### 1.1 Extract Story Components

- **Story Information**: Extract story ID, title, status, and basic metadata
- **Story Statement**: Parse the "As a... I want... so that..." format
- **Acceptance Criteria**: Extract numbered acceptance criteria list
- **Tasks/Subtasks**: Parse the task breakdown and dependencies
- **Dev Notes**: Extract technical context, architecture references, and implementation details
- **Testing Requirements**: Extract testing standards and validation requirements

#### 1.2 Validate Story Completeness

- Ensure all required story components are present
- Verify that technical context is sufficient for implementation
- Check that acceptance criteria are clear and measurable
- Validate that tasks are properly structured and sequenced

### 2. Map BMad Context to PRP Context

#### 2.1 Architecture Context Mapping

- **If `architectureVersion: >= v4` and `architectureSharded: true`**: 
  - Read relevant architecture documents based on story type
  - Map architecture sections to PRP context format
- **Else**: Use monolithic architecture file for context extraction

#### 2.2 Context Completeness Assessment

- **Documentation & References**: Map architecture documents to PRP format
  - Include relevant URLs, file paths, and documentation references
  - Add code examples and implementation patterns
  - Include known gotchas and technical constraints

- **Current Codebase Context**: Extract relevant project structure
  - File paths and naming conventions
  - Existing patterns and conventions
  - Technical stack and dependencies

- **Technical Constraints**: Identify and document
  - Version requirements and compatibility
  - Performance considerations
  - Security requirements
  - Integration constraints

### 3. Generate PRP Structure

#### 3.1 Goal Section

- **Feature Goal**: Extract specific, measurable end state from story
- **Deliverable**: Define concrete artifact (API endpoint, service class, etc.)
- **Success Definition**: How to know the feature is complete and working

#### 3.2 Why Section

- Extract business value and user impact from story
- Identify integration with existing features
- Document problems this solves and for whom

#### 3.3 What Section

- Convert story description to user-visible behavior
- Transform acceptance criteria to success criteria
- Maintain all technical requirements and constraints

#### 3.4 All Needed Context Section

- **Context Completeness Check**: Validate that PRP contains everything needed
- **Documentation & References**: Include all relevant documentation and examples
- **Current Codebase Context**: Provide project structure and patterns
- **Known Gotchas**: Document technical constraints and limitations

#### 3.5 Implementation Blueprint Section

- **Data Models**: Extract data model requirements from story
- **Implementation Tasks**: Convert BMad tasks to PRP format
- Maintain task dependencies and sequencing
- Include technical implementation details

#### 3.6 Validation Loop Section

- **Level 1: Syntax & Style**: Code quality and style checks
- **Level 2: Unit Tests**: Unit test requirements and coverage
- **Level 3: Integration Test**: Integration testing requirements

### 4. Validate Generated PRP

#### 4.1 Context Completeness Validation

- **Critical Check**: "If someone knew nothing about this codebase, would they have everything needed to implement this successfully?"
- Verify all necessary documentation is included
- Ensure code examples and patterns are provided
- Check that technical constraints are documented

#### 4.2 Information Density Validation

- Verify PRP uses keywords and patterns from the codebase
- Ensure context is information-dense and actionable
- Check that validation loops are executable

#### 4.3 Progressive Success Validation

- Verify implementation tasks are properly sequenced
- Ensure validation gates are progressive (syntax → tests → integration)
- Check that success criteria are clear and measurable

### 5. Generate PRP File

#### 5.1 File Creation

- Create PRP file: `PRPs/{story_id}.{story_title_short}.md`
- Use PRP template structure and formatting
- Include all mapped content and context

#### 5.2 Metadata and Traceability

- Add metadata linking back to original BMad story
- Include conversion timestamp and version information
- Maintain traceability between frameworks

### 6. Final Validation and Documentation

#### 6.1 PRP Quality Check

- Verify PRP follows PRPs-agentic-eng methodology
- Check that all sections are complete and accurate
- Validate that context is comprehensive and actionable

#### 6.2 Documentation Update

- Update story with PRP conversion status
- Document any conversion decisions or adaptations
- Maintain audit trail of conversion process

## Success Criteria

- [ ] BMad story successfully converted to PRP format
- [ ] All story requirements preserved and enhanced
- [ ] Technical context comprehensively mapped
- [ ] PRP passes context completeness check
- [ ] Validation loops are executable and comprehensive
- [ ] Traceability maintained between frameworks
- [ ] PRP file created and properly formatted

## Error Handling

### Story Parsing Errors
- **Missing Components**: Alert user and request missing information
- **Invalid Format**: Provide guidance on correct BMad story format
- **Incomplete Context**: Request additional technical context

### Context Mapping Errors
- **Missing Architecture**: Alert user to missing architecture documents
- **Incomplete Context**: Request additional context or documentation
- **Version Conflicts**: Handle version compatibility issues

### PRP Generation Errors
- **Template Errors**: Validate template structure and content
- **Format Issues**: Ensure PRP follows correct format
- **Validation Failures**: Address validation issues before completion

## Output

The task produces a complete PRP file in `PRPs/{story_id}.{story_title_short}.md` that contains:

1. **Goal**: Clear feature goal and success definition
2. **Why**: Business value and user impact
3. **What**: User-visible behavior and technical requirements
4. **All Needed Context**: Comprehensive context for implementation
5. **Implementation Blueprint**: Detailed implementation plan
6. **Validation Loop**: Executable validation and testing

The PRP is ready for execution using the PRPs-agentic-eng framework while maintaining full traceability to the original BMad story. 