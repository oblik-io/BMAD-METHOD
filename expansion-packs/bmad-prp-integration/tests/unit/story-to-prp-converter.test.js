const { describe, it, expect, beforeEach } = require('@jest/globals');
const path = require('path');
const fs = require('fs').promises;

// Mock the PRP runner adapter
jest.mock('../../tools/prp-runner-adapter');

describe('Story to PRP Converter', () => {
  let converter;
  let mockStory;
  let mockArchitecture;

  beforeEach(() => {
    // Reset mocks
    jest.clearAllMocks();
    
    // Mock story content
    mockStory = {
      id: '1.1',
      title: 'User Authentication',
      status: 'Draft',
      story: 'As a user, I want to authenticate with email and password, so that I can access protected resources',
      acceptanceCriteria: [
        'User can login with valid email and password',
        'User receives JWT token upon successful login',
        'Invalid credentials return appropriate error message'
      ],
      tasks: [
        'Create authentication service',
        'Implement login endpoint',
        'Add JWT token generation',
        'Write unit tests'
      ],
      devNotes: {
        technicalContext: 'Use JWT tokens for authentication',
        architecture: 'Follow REST API patterns',
        testing: 'Use pytest for unit tests'
      }
    };

    // Mock architecture content
    mockArchitecture = {
      techStack: 'Python, FastAPI, SQLAlchemy',
      patterns: 'REST API, JWT authentication',
      testing: 'pytest, coverage > 80%'
    };
  });

  describe('Story Parsing', () => {
    it('should parse BMad story format correctly', async () => {
      // Test story parsing functionality
      const parsedStory = await converter.parseStory(mockStory);
      
      expect(parsedStory).toBeDefined();
      expect(parsedStory.goal).toBeDefined();
      expect(parsedStory.acceptanceCriteria).toHaveLength(3);
      expect(parsedStory.tasks).toHaveLength(4);
    });

    it('should extract story components accurately', async () => {
      const components = await converter.extractComponents(mockStory);
      
      expect(components.storyStatement).toContain('As a user');
      expect(components.acceptanceCriteria).toContain('User can login');
      expect(components.tasks).toContain('Create authentication service');
    });

    it('should validate story completeness', async () => {
      const validation = await converter.validateStory(mockStory);
      
      expect(validation.isComplete).toBe(true);
      expect(validation.missingComponents).toHaveLength(0);
    });
  });

  describe('Context Mapping', () => {
    it('should map BMad architecture to PRP context', async () => {
      const context = await converter.mapContext(mockStory, mockArchitecture);
      
      expect(context.documentation).toBeDefined();
      expect(context.codebaseContext).toBeDefined();
      expect(context.technicalConstraints).toBeDefined();
    });

    it('should preserve technical context during mapping', async () => {
      const context = await converter.mapContext(mockStory, mockArchitecture);
      
      expect(context.technicalConstraints).toContain('JWT');
      expect(context.codebaseContext).toContain('FastAPI');
    });

    it('should handle missing architecture gracefully', async () => {
      const context = await converter.mapContext(mockStory, null);
      
      expect(context.documentation).toBeDefined();
      expect(context.warnings).toContain('No architecture context available');
    });
  });

  describe('PRP Generation', () => {
    it('should generate valid PRP format', async () => {
      const prp = await converter.generatePRP(mockStory, mockArchitecture);
      
      expect(prp).toContain('## Goal');
      expect(prp).toContain('## Why');
      expect(prp).toContain('## What');
      expect(prp).toContain('## All Needed Context');
      expect(prp).toContain('## Implementation Blueprint');
      expect(prp).toContain('## Validation Loop');
    });

    it('should include all story requirements in PRP', async () => {
      const prp = await converter.generatePRP(mockStory, mockArchitecture);
      
      expect(prp).toContain('User can login with valid email and password');
      expect(prp).toContain('Create authentication service');
      expect(prp).toContain('JWT tokens');
    });

    it('should create executable validation loops', async () => {
      const prp = await converter.generatePRP(mockStory, mockArchitecture);
      
      expect(prp).toContain('### Level 1: Syntax & Style');
      expect(prp).toContain('### Level 2: Unit Tests');
      expect(prp).toContain('### Level 3: Integration Test');
    });
  });

  describe('Validation', () => {
    it('should validate PRP context completeness', async () => {
      const prp = await converter.generatePRP(mockStory, mockArchitecture);
      const validation = await converter.validatePRP(prp);
      
      expect(validation.contextComplete).toBe(true);
      expect(validation.validationLoopsExecutable).toBe(true);
    });

    it('should detect missing context', async () => {
      const incompleteStory = { ...mockStory, devNotes: {} };
      const prp = await converter.generatePRP(incompleteStory, mockArchitecture);
      const validation = await converter.validatePRP(prp);
      
      expect(validation.contextComplete).toBe(false);
      expect(validation.missingContext).toBeDefined();
    });

    it('should validate information density', async () => {
      const prp = await converter.generatePRP(mockStory, mockArchitecture);
      const validation = await converter.validatePRP(prp);
      
      expect(validation.informationDensity).toBeGreaterThan(0.7);
    });
  });

  describe('File Operations', () => {
    it('should create PRP file with correct naming', async () => {
      const prp = await converter.generatePRP(mockStory, mockArchitecture);
      const filePath = await converter.savePRP(prp, mockStory);
      
      expect(filePath).toContain('PRPs/1.1.user-authentication.md');
    });

    it('should maintain traceability to original story', async () => {
      const prp = await converter.generatePRP(mockStory, mockArchitecture);
      await converter.savePRP(prp, mockStory);
      
      const savedPRP = await fs.readFile('PRPs/1.1.user-authentication.md', 'utf8');
      expect(savedPRP).toContain('Original Story: 1.1');
      expect(savedPRP).toContain('Conversion Date:');
    });
  });

  describe('Error Handling', () => {
    it('should handle invalid story format', async () => {
      const invalidStory = { id: '1.1' }; // Missing required fields
      
      await expect(converter.generatePRP(invalidStory, mockArchitecture))
        .rejects.toThrow('Invalid story format');
    });

    it('should handle missing dependencies', async () => {
      // Mock missing dependencies
      jest.spyOn(fs, 'access').mockRejectedValue(new Error('File not found'));
      
      await expect(converter.validateEnvironment())
        .rejects.toThrow('Missing required dependencies');
    });

    it('should provide helpful error messages', async () => {
      try {
        await converter.generatePRP(null, mockArchitecture);
      } catch (error) {
        expect(error.message).toContain('Story is required');
      }
    });
  });

  describe('Integration', () => {
    it('should integrate with BMad workflow', async () => {
      const result = await converter.convertStoryToPRP(mockStory, mockArchitecture);
      
      expect(result.success).toBe(true);
      expect(result.prpPath).toBeDefined();
      expect(result.traceability).toBeDefined();
    });

    it('should maintain BMad story format compatibility', async () => {
      const result = await converter.convertStoryToPRP(mockStory, mockArchitecture);
      
      expect(result.bmadCompatible).toBe(true);
      expect(result.storyId).toBe('1.1');
    });

    it('should support workflow continuation', async () => {
      const result = await converter.convertStoryToPRP(mockStory, mockArchitecture);
      
      expect(result.nextSteps).toBeDefined();
      expect(result.workflowState).toBe('ready_for_execution');
    });
  });
}); 