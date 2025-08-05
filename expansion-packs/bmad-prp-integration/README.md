# BMad-PRP Integration Expansion Pack

## Overview

The BMad-PRP Integration Expansion Pack combines the structured planning and team coordination of BMad-Method with the optimized single-agent execution of PRPs-agentic-eng. This integration provides the best of both approaches: systematic planning with one-pass implementation success.

## Features

### 🔄 **Hybrid Workflow**
- **BMad Planning**: Use PM, Architect, and SM agents for comprehensive planning
- **PRP Execution**: Convert stories to PRP format for optimized implementation
- **Seamless Integration**: Maintain traceability between frameworks
- **Quality Gates**: Comprehensive validation at each phase

### 🤖 **Specialized Agents**
- **PRP Converter**: Transforms BMad stories to PRP format
- **PRP Executor**: Manages PRP execution using PRPs-agentic-eng
- **PRP Validator**: Validates results and maps back to BMad format
- **Hybrid Orchestrator**: Coordinates the complete workflow

### 📋 **Workflow Phases**
1. **Planning Phase (BMad)**: Create PRD, architecture, and detailed stories
2. **PRP Generation**: Convert stories to PRP format with comprehensive context
3. **Execution Phase (PRP)**: Execute PRPs for one-pass implementation
4. **Validation & Integration**: Validate results and integrate back to BMad

## Installation

### Prerequisites
- BMad-Method v4.0+ installed
- Python 3.8+ (for PRP runner)
- PRPs-agentic-eng repository (for PRP runner)

### Install the Expansion Pack

```bash
# Install BMad with PRP integration
npx bmad-method install --expansion-packs bmad-prp-integration

# Or install separately
npx bmad-method install-expansion bmad-prp-integration
```

### Setup PRP Runner

```bash
# Clone PRPs-agentic-eng repository
git clone https://github.com/Wirasm/PRPs-agentic-eng.git
cd PRPs-agentic-eng

# Install Python dependencies
pip install -r requirements.txt

# Copy PRP runner to your project
cp PRPs/scripts/prp_runner.py /path/to/your/project/tools/
```

## Usage

### Basic Workflow

1. **Start with BMad Planning**:
   ```bash
   @pm Create a PRD for user authentication system
   @architect Design the system architecture
   @sm Create detailed stories for authentication features
   ```

2. **Convert Stories to PRPs**:
   ```bash
   @prp-converter Convert story 1.1 to PRP format
   ```

3. **Execute PRPs**:
   ```bash
   @prp-executor Execute PRP for user authentication
   ```

4. **Validate Results**:
   ```bash
   @prp-validator Validate execution results
   @qa Review implementation quality
   ```

### Advanced Workflow

#### Hybrid Orchestration
```bash
@hybrid-orchestrator Run complete hybrid workflow
```

#### Parallel Execution
```bash
@hybrid-orchestrator Run parallel workflow mode
```

#### Adaptive Execution
```bash
@hybrid-orchestrator Run adaptive workflow mode
```

### Command Reference

#### PRP Converter Commands
- `@prp-converter convert-story <story-id>` - Convert story to PRP
- `@prp-converter validate-prp <prp-file>` - Validate PRP format
- `@prp-converter enhance-context <prp-file>` - Enhance PRP context

#### PRP Executor Commands
- `@prp-executor execute <prp-file>` - Execute PRP
- `@prp-executor execute-interactive <prp-file>` - Interactive execution
- `@prp-executor execute-headless <prp-file>` - Headless execution
- `@prp-executor validate-environment` - Validate execution environment

#### PRP Validator Commands
- `@prp-validator validate-results <execution-results>` - Validate results
- `@prp-validator map-to-story <results>` - Map results to BMad format
- `@prp-validator quality-assessment <results>` - Quality assessment

#### Hybrid Orchestrator Commands
- `@hybrid-orchestrator run-workflow <mode>` - Run complete workflow
- `@hybrid-orchestrator status` - Check workflow status
- `@hybrid-orchestrator pause` - Pause workflow
- `@hybrid-orchestrator resume` - Resume workflow

## Configuration

### Core Configuration

Add to your `core-config.yaml`:

```yaml
prp:
  enabled: true
  runner-path: ./tools/prp_runner.py
  templates-path: ./PRPs/templates
  output-dir: ./PRPs
  validation:
    auto-validate: true
    quality-gates: true
    context-completeness: true
  execution:
    default-mode: interactive
    timeout: 300000
    verbose: false
```

### Environment Setup

```bash
# Set up PRP environment
export PRP_RUNNER_PATH=./tools/prp_runner.py
export PRP_OUTPUT_DIR=./PRPs
export PRP_TEMPLATES_DIR=./PRPs/templates
```

## Workflow Modes

### Sequential Mode
- Execute phases in sequence
- Validation gates between phases
- Suitable for complex projects

### Parallel Mode
- Execute compatible phases in parallel
- Dependency management
- Faster execution for simple projects

### Adaptive Mode
- Dynamic workflow adjustment
- Context-aware decision making
- Intelligent error recovery

## Quality Gates

### Planning Quality Gate
- [ ] PRD complete and validated
- [ ] Architecture designed and documented
- [ ] Stories created with acceptance criteria
- [ ] All requirements captured

### PRP Quality Gate
- [ ] PRP format valid
- [ ] Context complete and comprehensive
- [ ] Validation loops executable
- [ ] Traceability maintained

### Execution Quality Gate
- [ ] Execution successful
- [ ] Code quality acceptable
- [ ] Tests passing
- [ ] Requirements met

### Validation Quality Gate
- [ ] Acceptance criteria met
- [ ] Integration tests passing
- [ ] Quality standards met
- [ ] Documentation complete

## Error Handling

### Common Issues

#### PRP Runner Not Found
```bash
# Check if PRP runner is installed
ls tools/prp_runner.py

# Install PRP runner
cp /path/to/PRPs-agentic-eng/PRPs/scripts/prp_runner.py tools/
```

#### Python Environment Issues
```bash
# Check Python version
python --version

# Install dependencies
pip install -r requirements.txt
```

#### Context Completeness Issues
```bash
# Enhance PRP context
@prp-converter enhance-context <prp-file>

# Add missing documentation
@prp-converter add-documentation <prp-file> <doc-path>
```

### Recovery Procedures

#### Execution Failures
1. Check execution environment
2. Validate PRP format and context
3. Debug execution issues
4. Fall back to BMad development workflow if needed

#### Validation Failures
1. Address quality issues
2. Fix failing tests
3. Resolve integration problems
4. Re-run validation phase

## Testing

### Run Tests
```bash
# Run unit tests
npm test -- expansion-packs/bmad-prp-integration/tests/unit/

# Run integration tests
npm test -- expansion-packs/bmad-prp-integration/tests/integration/

# Run end-to-end tests
npm test -- expansion-packs/bmad-prp-integration/tests/e2e/
```

### Test Coverage
```bash
# Generate coverage report
npm run test:coverage -- expansion-packs/bmad-prp-integration/
```

## Examples

### Simple Feature Implementation

1. **Create Story**:
   ```markdown
   Story 1.1: User Login
   
   As a user, I want to login with email and password, so that I can access the application.
   
   Acceptance Criteria:
   - User can enter email and password
   - System validates credentials
   - User receives JWT token on success
   - Error message shown for invalid credentials
   ```

2. **Convert to PRP**:
   ```bash
   @prp-converter convert-story 1.1
   ```

3. **Execute PRP**:
   ```bash
   @prp-executor execute PRPs/1.1.user-login.md
   ```

4. **Validate Results**:
   ```bash
   @prp-validator validate-results
   ```

### Complex System Implementation

1. **Planning Phase**:
   ```bash
   @pm Create PRD for e-commerce platform
   @architect Design microservices architecture
   @sm Create stories for all features
   ```

2. **PRP Generation**:
   ```bash
   @prp-converter convert-all-stories
   ```

3. **Parallel Execution**:
   ```bash
   @hybrid-orchestrator run-workflow parallel
   ```

4. **Integration Validation**:
   ```bash
   @prp-validator validate-integration
   @qa review-complete-system
   ```

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

## Troubleshooting

### Debug Mode
```bash
# Enable debug logging
export PRP_DEBUG=true
export BMAD_DEBUG=true

# Run with verbose output
@prp-executor execute --verbose <prp-file>
```

### Log Files
- PRP execution logs: `logs/prp-execution.log`
- BMad workflow logs: `logs/bmad-workflow.log`
- Integration logs: `logs/integration.log`

### Common Solutions

#### Context Issues
- Add missing documentation to PRP
- Enhance code examples and patterns
- Include known gotchas and constraints

#### Execution Issues
- Check Python environment and dependencies
- Validate PRP runner installation
- Verify file permissions and paths

#### Integration Issues
- Check BMad configuration
- Validate story format compatibility
- Ensure traceability is maintained

## Contributing

### Development Setup
```bash
# Clone the repository
git clone https://github.com/bmadcode/bmad-method.git
cd bmad-method

# Install dependencies
npm install

# Set up development environment
npm run setup:dev
```

### Running Tests
```bash
# Run all tests
npm test

# Run specific test suite
npm test -- expansion-packs/bmad-prp-integration/

# Run with coverage
npm run test:coverage
```

### Code Style
```bash
# Format code
npm run format

# Lint code
npm run lint

# Fix linting issues
npm run lint:fix
```

## Support

### Documentation
- [BMad-Method User Guide](../bmad-core/user-guide.md)
- [PRPs-agentic-eng Documentation](https://github.com/Wirasm/PRPs-agentic-eng)
- [Integration Examples](./examples/)

### Community
- [Discord Community](https://discord.gg/gk8jAdXWmj)
- [GitHub Issues](https://github.com/bmadcode/bmad-method/issues)
- [GitHub Discussions](https://github.com/bmadcode/bmad-method/discussions)

### Getting Help
1. Check the documentation and examples
2. Search existing issues and discussions
3. Ask questions in the Discord community
4. Create a new issue with detailed information

## License

This expansion pack is licensed under the MIT License. See the [LICENSE](../../LICENSE) file for details.

## Acknowledgments

- **BMad-Method Team**: For the core framework and support
- **PRPs-agentic-eng Team**: For the PRP methodology and runner
- **Community Contributors**: For feedback and improvements

---

**Happy coding with BMad-PRP Integration! 🚀** 