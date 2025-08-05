#!/usr/bin/env node

/**
 * PRP Runner Adapter for BMad-Method Integration
 * 
 * This tool provides integration between BMad-Method and PRPs-agentic-eng
 * by managing PRP execution, result collection, and integration with BMad workflow.
 */

const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs').promises;
const yaml = require('js-yaml');

class PRPRunnerAdapter {
  constructor(config = {}) {
    this.config = {
      runnerPath: config.runnerPath || 'tools/prp_runner.py',
      outputDir: config.outputDir || 'PRPs',
      workingDir: config.workingDir || process.cwd(),
      ...config
    };
  }

  /**
   * Execute a PRP using the PRPs-agentic-eng runner
   * @param {string} prpPath - Path to the PRP file
   * @param {Object} options - Execution options
   * @returns {Promise<Object>} Execution results
   */
  async executePRP(prpPath, options = {}) {
    const {
      mode = 'interactive',
      outputFormat = 'text',
      verbose = false,
      timeout = 300000 // 5 minutes default
    } = options;

    try {
      // Validate PRP file exists
      await this.validatePRPFile(prpPath);

      // Build runner command
      const command = this.buildRunnerCommand(prpPath, {
        mode,
        outputFormat,
        verbose
      });

      // Execute PRP
      const result = await this.runPRPCommand(command, { timeout });

      // Process results
      return await this.processResults(result, prpPath);

    } catch (error) {
      throw new Error(`PRP execution failed: ${error.message}`);
    }
  }

  /**
   * Validate PRP file exists and is properly formatted
   * @param {string} prpPath - Path to PRP file
   */
  async validatePRPFile(prpPath) {
    try {
      const stats = await fs.stat(prpPath);
      if (!stats.isFile()) {
        throw new Error(`PRP path is not a file: ${prpPath}`);
      }

      // Basic format validation
      const content = await fs.readFile(prpPath, 'utf8');
      if (!content.includes('## Goal') || !content.includes('## What')) {
        throw new Error(`PRP file does not appear to be in correct format: ${prpPath}`);
      }

    } catch (error) {
      if (error.code === 'ENOENT') {
        throw new Error(`PRP file not found: ${prpPath}`);
      }
      throw error;
    }
  }

  /**
   * Build PRP runner command with parameters
   * @param {string} prpPath - Path to PRP file
   * @param {Object} options - Command options
   * @returns {Array} Command array for spawn
   */
  buildRunnerCommand(prpPath, options) {
    const { mode, outputFormat, verbose } = options;
    
    const args = [
      this.config.runnerPath,
      '--prp-path', prpPath
    ];

    // Add mode-specific arguments
    if (mode === 'interactive') {
      args.push('--interactive');
    } else if (mode === 'headless') {
      args.push('--output-format', outputFormat);
    } else if (mode === 'streaming') {
      args.push('--output-format', 'stream-json');
    }

    // Add verbose flag if requested
    if (verbose) {
      args.push('--verbose');
    }

    return ['python', args];
  }

  /**
   * Execute PRP runner command
   * @param {Array} command - Command array
   * @param {Object} options - Execution options
   * @returns {Promise<Object>} Execution result
   */
  runPRPCommand(command, options = {}) {
    return new Promise((resolve, reject) => {
      const [executable, args] = command;
      const { timeout } = options;

      const child = spawn(executable, args, {
        cwd: this.config.workingDir,
        stdio: ['pipe', 'pipe', 'pipe'],
        env: { ...process.env }
      });

      let stdout = '';
      let stderr = '';
      let exitCode = null;

      // Set timeout
      const timeoutId = timeout ? setTimeout(() => {
        child.kill('SIGTERM');
        reject(new Error(`PRP execution timed out after ${timeout}ms`));
      }, timeout) : null;

      // Handle stdout
      child.stdout.on('data', (data) => {
        stdout += data.toString();
      });

      // Handle stderr
      child.stderr.on('data', (data) => {
        stderr += data.toString();
      });

      // Handle process completion
      child.on('close', (code) => {
        exitCode = code;
        
        if (timeoutId) {
          clearTimeout(timeoutId);
        }

        if (code === 0) {
          resolve({
            success: true,
            stdout,
            stderr,
            exitCode
          });
        } else {
          reject(new Error(`PRP execution failed with exit code ${code}: ${stderr}`));
        }
      });

      // Handle process errors
      child.on('error', (error) => {
        if (timeoutId) {
          clearTimeout(timeoutId);
        }
        reject(new Error(`PRP execution error: ${error.message}`));
      });
    });
  }

  /**
   * Process PRP execution results
   * @param {Object} result - Raw execution result
   * @param {string} prpPath - Original PRP file path
   * @returns {Object} Processed results
   */
  async processResults(result, prpPath) {
    const { stdout, stderr, exitCode } = result;

    // Parse output based on format
    let parsedOutput;
    try {
      if (stdout.includes('{') && stdout.includes('}')) {
        // Try to parse as JSON
        const jsonMatch = stdout.match(/\{[\s\S]*\}/);
        if (jsonMatch) {
          parsedOutput = JSON.parse(jsonMatch[0]);
        }
      }
    } catch (error) {
      // Fall back to text parsing
      parsedOutput = this.parseTextOutput(stdout);
    }

    // Collect generated artifacts
    const artifacts = await this.collectArtifacts(prpPath);

    return {
      success: true,
      exitCode,
      output: parsedOutput || stdout,
      stderr,
      artifacts,
      metadata: {
        prpPath,
        executionTime: new Date().toISOString(),
        runnerVersion: await this.getRunnerVersion()
      }
    };
  }

  /**
   * Parse text output from PRP execution
   * @param {string} output - Raw output text
   * @returns {Object} Parsed output
   */
  parseTextOutput(output) {
    const lines = output.split('\n');
    const result = {
      files: [],
      tests: [],
      errors: [],
      warnings: []
    };

    for (const line of lines) {
      if (line.includes('Created:') || line.includes('Modified:')) {
        const fileMatch = line.match(/(?:Created|Modified):\s*(.+)/);
        if (fileMatch) {
          result.files.push(fileMatch[1].trim());
        }
      } else if (line.includes('test') && line.includes('passed')) {
        result.tests.push(line.trim());
      } else if (line.includes('ERROR:') || line.includes('FAILED:')) {
        result.errors.push(line.trim());
      } else if (line.includes('WARNING:') || line.includes('Warning:')) {
        result.warnings.push(line.trim());
      }
    }

    return result;
  }

  /**
   * Collect artifacts generated during PRP execution
   * @param {string} prpPath - Original PRP file path
   * @returns {Array} List of generated artifacts
   */
  async collectArtifacts(prpPath) {
    const artifacts = [];
    const prpDir = path.dirname(prpPath);
    const workingDir = this.config.workingDir;

    try {
      // Look for common artifact patterns
      const patterns = [
        'src/**/*.py',
        'src/**/*.js',
        'src/**/*.ts',
        'tests/**/*.py',
        'tests/**/*.js',
        'tests/**/*.ts',
        '*.md',
        '*.json',
        '*.yaml',
        '*.yml'
      ];

      for (const pattern of patterns) {
        try {
          const files = await this.findFiles(path.join(workingDir, pattern));
          artifacts.push(...files);
        } catch (error) {
          // Pattern not found, continue
        }
      }

      // Remove duplicates and filter by modification time
      const uniqueArtifacts = [...new Set(artifacts)];
      const recentArtifacts = await this.filterRecentFiles(uniqueArtifacts, prpPath);

      return recentArtifacts;

    } catch (error) {
      console.warn(`Warning: Could not collect artifacts: ${error.message}`);
      return [];
    }
  }

  /**
   * Find files matching a pattern
   * @param {string} pattern - File pattern
   * @returns {Array} Matching files
   */
  async findFiles(pattern) {
    const { glob } = require('glob');
    return await glob(pattern, { cwd: this.config.workingDir });
  }

  /**
   * Filter files modified after PRP file
   * @param {Array} files - List of files
   * @param {string} prpPath - PRP file path
   * @returns {Array} Recently modified files
   */
  async filterRecentFiles(files, prpPath) {
    try {
      const prpStats = await fs.stat(prpPath);
      const recentFiles = [];

      for (const file of files) {
        try {
          const fileStats = await fs.stat(path.join(this.config.workingDir, file));
          if (fileStats.mtime > prpStats.mtime) {
            recentFiles.push(file);
          }
        } catch (error) {
          // File not accessible, skip
        }
      }

      return recentFiles;
    } catch (error) {
      console.warn(`Warning: Could not filter recent files: ${error.message}`);
      return files;
    }
  }

  /**
   * Get PRP runner version
   * @returns {string} Runner version
   */
  async getRunnerVersion() {
    try {
      const result = await this.runPRPCommand(['python', [this.config.runnerPath, '--version']]);
      return result.stdout.trim();
    } catch (error) {
      return 'unknown';
    }
  }

  /**
   * Validate PRP execution environment
   * @returns {Object} Validation results
   */
  async validateEnvironment() {
    const results = {
      runnerExists: false,
      pythonAvailable: false,
      workingDirValid: false,
      outputDirValid: false
    };

    try {
      // Check if runner exists
      await fs.access(this.config.runnerPath);
      results.runnerExists = true;
    } catch (error) {
      // Runner not found
    }

    try {
      // Check if Python is available
      const { execSync } = require('child_process');
      execSync('python --version', { stdio: 'pipe' });
      results.pythonAvailable = true;
    } catch (error) {
      // Python not available
    }

    try {
      // Check working directory
      await fs.access(this.config.workingDir);
      results.workingDirValid = true;
    } catch (error) {
      // Working directory not accessible
    }

    try {
      // Check output directory
      await fs.access(this.config.outputDir);
      results.outputDirValid = true;
    } catch (error) {
      // Output directory not accessible
    }

    return results;
  }
}

module.exports = PRPRunnerAdapter; 