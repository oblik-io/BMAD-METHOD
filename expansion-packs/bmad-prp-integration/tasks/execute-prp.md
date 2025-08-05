# Execute PRP Task

## Purpose

To execute a PRP using the PRPs-agentic-eng framework, managing the execution environment, handling the PRP runner integration, and ensuring successful implementation of features through optimized single-agent execution.

## SEQUENTIAL Task Execution (Do not proceed until current Task is complete)

### 0. Load Configuration and Validate Input

- Load `{root}/core-config.yaml` from the project root
- Validate that the PRP file exists and is in correct format
- Check that PRP runner is available and properly configured
- Verify execution environment and dependencies

### 1. Prepare Execution Environment

#### 1.1 PRP Runner Setup

- **Locate PRP Runner**: Find PRP runner executable (`prp_runner.py`)
- **Validate Runner**: Check runner version and compatibility
- **Configure Environment**: Set up Python environment and dependencies
- **Verify Permissions**: Ensure runner has necessary file access

#### 1.2 Project Context Setup

- **Working Directory**: Set up proper working directory for execution
- **File Paths**: Configure relative and absolute paths
- **Environment Variables**: Set required environment variables
- **Dependencies**: Verify project dependencies are available

#### 1.3 PRP Validation

- **Format Validation**: Verify PRP follows correct format
- **Context Completeness**: Check that PRP contains all necessary context
- **Validation Loops**: Verify validation loops are executable
- **Dependencies**: Check for any missing dependencies or context

### 2. Configure Execution Parameters

#### 2.1 Execution Mode Selection

- **Interactive Mode**: Real-time execution with user interaction
  - Suitable for development and debugging
  - Immediate feedback and course correction
  - User can intervene during execution

- **Headless Mode**: Automated execution without user interaction
  - Suitable for CI/CD and batch processing
  - Structured output for programmatic handling
  - No user intervention required

- **Streaming Mode**: Real-time progress monitoring
  - Continuous feedback and status updates
  - Suitable for long-running executions
  - Progress tracking and monitoring

#### 2.2 Output Configuration

- **Output Format**: Configure output format (text, json, stream-json)
- **Logging Level**: Set appropriate logging verbosity
- **Error Handling**: Configure error handling and recovery
- **Progress Reporting**: Set up progress tracking and reporting

### 3. Execute PRP

#### 3.1 PRP Runner Execution

- **Command Construction**: Build PRP runner command with parameters
- **Execution Launch**: Launch PRP runner with configured parameters
- **Process Management**: Monitor execution process and status
- **Output Capture**: Capture and process execution output

#### 3.2 Real-time Monitoring

- **Progress Tracking**: Monitor execution progress in real-time
- **Status Updates**: Provide regular status updates to user
- **Error Detection**: Detect and handle execution errors
- **Resource Monitoring**: Monitor resource usage and performance

#### 3.3 Interactive Support

- **User Interaction**: Handle user input and interaction (if interactive mode)
- **Decision Points**: Present decision points to user when needed
- **Error Recovery**: Provide error recovery options to user
- **Progress Reporting**: Keep user informed of execution progress

### 4. Handle Execution Results

#### 4.1 Result Collection

- **Output Processing**: Process and parse execution output
- **Artifact Collection**: Collect generated artifacts and files
- **Log Collection**: Gather execution logs and debugging information
- **Status Information**: Collect execution status and completion information

#### 4.2 Success Validation

- **Completion Check**: Verify execution completed successfully
- **Output Validation**: Validate generated output and artifacts
- **Quality Check**: Assess quality of generated code and implementation
- **Requirement Verification**: Verify all requirements were met

#### 4.3 Error Handling

- **Error Analysis**: Analyze any execution errors or failures
- **Error Classification**: Classify errors by type and severity
- **Recovery Options**: Provide recovery options and suggestions
- **Error Reporting**: Report errors with context and debugging information

### 5. Process Execution Output

#### 5.1 Output Parsing

- **Structured Output**: Parse structured output (JSON, etc.)
- **Text Output**: Process text output and logs
- **Artifact Analysis**: Analyze generated artifacts and files
- **Metadata Extraction**: Extract execution metadata and statistics

#### 5.2 Result Validation

- **Code Quality**: Assess quality of generated code
- **Test Results**: Validate test execution results
- **Performance Metrics**: Analyze performance and resource usage
- **Security Assessment**: Check for security issues or vulnerabilities

#### 5.3 Documentation Generation

- **Execution Summary**: Generate execution summary report
- **Artifact Documentation**: Document generated artifacts and files
- **Performance Report**: Create performance and resource usage report
- **Issue Report**: Document any issues or concerns

### 6. Integration with BMad Workflow

#### 6.1 Result Mapping

- **BMad Format**: Map execution results to BMad story format
- **Status Update**: Update story status based on execution results
- **Completion Notes**: Document execution results and completion notes
- **Traceability**: Maintain traceability between PRP and story

#### 6.2 Workflow Continuation

- **Next Steps**: Determine next steps in BMad workflow
- **Validation**: Prepare for validation phase
- **Documentation**: Update story documentation with results
- **Handoff**: Prepare for handoff to next phase

## Success Criteria

- [ ] PRP executed successfully using PRPs-agentic-eng framework
- [ ] All execution parameters properly configured
- [ ] Execution environment set up correctly
- [ ] Real-time monitoring and progress tracking active
- [ ] Execution results collected and processed
- [ ] Output validated against requirements
- [ ] Results mapped to BMad story format
- [ ] Integration with BMad workflow maintained

## Error Handling

### Environment Setup Errors
- **Missing Dependencies**: Install or configure missing dependencies
- **Permission Issues**: Resolve file and directory permissions
- **Configuration Errors**: Fix configuration and setup issues

### Execution Errors
- **Runner Errors**: Handle PRP runner errors and failures
- **Process Errors**: Manage execution process errors
- **Resource Errors**: Handle resource and performance issues

### Result Processing Errors
- **Output Parsing Errors**: Handle output parsing and processing errors
- **Validation Errors**: Address validation and quality issues
- **Integration Errors**: Resolve integration and mapping issues

## Output

The task produces execution results including:

1. **Execution Status**: Success/failure status and completion information
2. **Generated Artifacts**: Code files, tests, and other generated artifacts
3. **Execution Logs**: Detailed logs and debugging information
4. **Performance Metrics**: Resource usage and performance statistics
5. **Quality Assessment**: Code quality and validation results
6. **Integration Data**: Data mapped to BMad story format

The results are ready for validation and integration with the BMad workflow. 