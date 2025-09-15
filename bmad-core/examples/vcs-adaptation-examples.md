# VCS Adaptation Examples

## Real-World Scenarios: How BMAD Adapts

### Example 1: Startup with GitHub Flow

**Context:** 5-person team, web SaaS, deploys daily

**Discovery:**

```
BMAD: "How does your team manage code versions?"
User: "Git with GitHub"
BMAD: "Which Git workflow best describes your approach?"
User: "GitHub Flow - simple feature branches"
```

**BMAD Adapts:**

- Architect generates lightweight, PR-sized architecture updates
- SM creates 1-3 day stories that map to single PRs
- Dev suggests branch names like `feature/add-user-auth`
- All docs optimized for quick review in PR comments

**Generated Architecture Snippet:**

```markdown
## Payment Service Update

_PR: #234 - feature/add-stripe-integration_

### Changes in This PR

- New Stripe webhook handler
- Updated payment models
- Added retry logic

### Testing

- [ ] Unit tests for webhook handler
- [ ] Integration test with Stripe test mode
- [ ] Manual testing checklist in PR
```

---

### Example 2: Enterprise with GitFlow

**Context:** 50-person team, banking software, quarterly releases

**Discovery:**

```
BMAD: "How does your team manage code versions?"
User: "Git with corporate server"
BMAD: "Which Git workflow?"
User: "GitFlow - we have develop, release, and hotfix branches"
```

**BMAD Adapts:**

- Architect creates version-oriented architecture docs
- PM generates release-scoped PRDs
- SM groups stories by release version
- Dev follows strict branch naming

**Generated Architecture Snippet:**

```markdown
## Release 2.4.0 Architecture

### Version Highlights

- New authentication system (breaking change)
- Performance improvements
- Database migration required

### Branch Status

- develop: v2.5.0 features in progress
- release/2.4.0: Final testing
- hotfix/2.3.1: Critical fix for production

### Migration Guide

From 2.3.x to 2.4.0:

1. Run migration script
2. Update config files
3. Restart services in order
```

---

### Example 3: No Version Control

**Context:** Data scientist, one-time analysis script

**Discovery:**

```
BMAD: "How does your team manage code versions?"
User: "No version control needed - this is a one-time script"
```

**BMAD Adapts:**

- All code in single, runnable package
- Extensive inline documentation
- No commit messages or branch references
- Date-stamped delivery

**Generated Package:**

```
customer_analysis_20240315/
├── README.md           # Complete instructions
├── requirements.txt    # All Python dependencies
├── analysis.py        # Full script with comments
├── data/
│   └── sample.csv     # Sample data format
└── output/
    └── results_template.xlsx
```

**README Content:**

```markdown
# Customer Analysis Script

Generated: 2024-03-15

## Quick Start

1. Install dependencies: pip install -r requirements.txt
2. Place your data in data/input.csv
3. Run: python analysis.py
4. Results appear in output/

## No Version Control Required

This is a complete, self-contained package.
```

---

### Example 4: Custom SVN Workflow

**Context:** Game studio using Subversion

**Discovery:**

```
BMAD: "How does your team manage code versions?"
User: "Other version control system"
BMAD: "Which system?"
User: "Subversion (SVN)"
```

**BMAD Adapts:**

- Uses "revision" instead of "commit"
- References trunk/branches/tags structure
- Revision numbers, not hashes
- SVN-specific commands

**Generated Instructions:**

```markdown
## Integration Steps

1. Update your working copy:
   svn update

2. Create feature branch:
   svn copy ^/trunk ^/branches/feature-player-inventory

3. After implementation:
   svn merge ^/branches/feature-player-inventory

4. Commit with revision message:
   svn commit -m "Add player inventory system (refs ticket #456)"
```

---

### Example 5: Trunk-Based with Feature Flags

**Context:** Netflix-style continuous deployment

**Discovery:**

```
BMAD: "How does your team manage code versions?"
User: "Git with GitHub"
BMAD: "Which Git workflow?"
User: "Trunk-Based - we deploy continuously"
```

**BMAD Adapts:**

- Everything behind feature flags
- Tiny, hours-long tasks
- Direct commits or same-day PRs
- Progressive rollout plans

**Generated Story:**

````markdown
## Story: Add Recommendation Engine

Size: 4 hours
Flag: `recommendation-engine-v2`

### Implementation

```python
if feature_flag.is_enabled("recommendation-engine-v2", user_id):
    return new_recommendation_engine(user_id)
else:
    return legacy_recommendations(user_id)
```
````

### Rollout Plan

- Hour 1-2: Implement behind flag (0% users)
- Hour 3: Deploy and enable for employees
- Hour 4: Enable for 1% external users
- Day 2: 10% if metrics good
- Day 3: 50%
- Day 5: 100% and schedule flag removal

```

---

### Example 6: Complex Multi-VCS Setup

**Context:** Enterprise with mixed systems

**Discovery:**
```

BMAD: "How does your team manage code versions?"
User: "Custom/Complex setup"
BMAD: "Please describe:"
User: "Frontend in Git, backend in Perforce, configs in SVN"

````

**BMAD Adapts:**
- Asks for component-specific preferences
- Generates VCS-appropriate artifacts per component
- Uses neutral terminology in cross-component docs

**Generated Guidance:**
```markdown
## Multi-VCS Development Guide

### Frontend (Git/GitHub Flow)
- Feature branches from main
- PR review process
- Deploy on merge

### Backend (Perforce)
- Create changelist for features
- Submit after review
- Changelist numbers in deployment notes

### Configuration (SVN)
- Update from trunk before changes
- Commit with revision references
- Tag for production releases

### Cross-Component Changes
When updating across systems:
1. Frontend PR: #123
2. Backend Changelist: 456789
3. Config Revision: r1234

Reference all three in deployment ticket.
````

## Key Takeaways

1. **BMAD never assumes** - always discovers first
2. **Adapts terminology** - commit/changelist/revision as appropriate
3. **Respects workflows** - doesn't try to "improve" existing processes
4. **Practical focus** - generates what works with their tools
5. **Clear communication** - uses the team's language

This flexibility makes BMAD valuable to ANY team, regardless of their VCS choice.
