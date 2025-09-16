# VCS Workflow Detection Confidence Scoring

## Overview

The VCS auto-detection system uses a confidence-based scoring mechanism to suggest (not decide) the most likely workflow pattern. This document explains how confidence scores are calculated and interpreted.

## Core Principle

**"Detection as a HINT, not a DECISION"**

Even with 100% confidence, we always confirm with the user. Auto-detection saves time but doesn't replace human judgment.

## Confidence Score Calculation

### Score Range

- **0.0 - 1.0** (0% - 100%)
- **Threshold for suggestion: 0.7** (70%)
- Below threshold → marked as "unclear" → trigger clarifying questions

### Workflow Indicators and Weights

#### GitFlow (Maximum Score: 1.0)

| Indicator             | Weight | Detection Method                            |
| --------------------- | ------ | ------------------------------------------- |
| Develop branch exists | 0.3    | Check for `develop` or `development` branch |
| Release branches      | 0.3    | Pattern match `release/*` branches          |
| Hotfix branches       | 0.2    | Pattern match `hotfix/*` branches           |
| Version tags          | 0.2    | Tags matching `v*` pattern                  |

#### GitHub Flow (Maximum Score: 1.0)

| Indicator            | Weight | Detection Method                          |
| -------------------- | ------ | ----------------------------------------- |
| PR/MR merges         | 0.3    | Commit messages with "Merge pull request" |
| Short-lived features | 0.3    | Feature branches < 7 days lifespan        |
| Squash merges        | 0.2    | Commits with `(#\d+)` pattern             |
| No develop branch    | 0.2    | Absence of develop/development branch     |

#### Trunk-Based Development (Maximum Score: 1.0)

| Indicator           | Weight | Detection Method                         |
| ------------------- | ------ | ---------------------------------------- |
| Direct main commits | 0.4    | >50% commits directly to main/master     |
| Very short branches | 0.3    | Branches living < 1 day                  |
| Feature flags       | 0.3    | Commits mentioning feature flags/toggles |

## Confidence Interpretation

### High Confidence (≥ 70%)

```yaml
presentation:
  title: 'Detected workflow: {workflow}'
  confidence: '{score}%'
  action: 'Present with evidence and ask for confirmation'
```

Example:

```
🔍 Detected workflow: **GitFlow** (confidence: 85%)

Evidence:
✓ Found develop branch
✓ Found 3 release branches
✓ Found 5 version tags

Is this correct?
```

### Medium Confidence (40% - 69%)

```yaml
presentation:
  title: 'Possible workflow detected'
  action: 'Show evidence but emphasize uncertainty'
  fallback: 'Offer clarifying questions'
```

### Low Confidence (< 40%)

```yaml
presentation:
  title: 'Could not confidently detect workflow'
  action: 'Skip to clarifying questions or manual selection'
```

## Migration Detection

When patterns differ between time periods:

```yaml
time_windows:
  recent: 'last 30 days'
  historical: '30-90 days ago'

if_different:
  confidence_penalty: -0.2 # Reduce confidence
  action: 'Alert user about possible migration'
```

## Edge Cases and Adjustments

### Monorepo Detection

- Multiple package.json/go.mod files → reduce confidence by 0.1
- Different patterns in subdirectories → mark as "complex"

### Fresh Repository

- Less than 10 commits → automatically mark as "unclear"
- No branches besides main → suggest starting with GitHub Flow

### Polluted History

- Imported/migrated repos → check commit dates for anomalies
- Fork detection → warn about inherited patterns

## Confidence Improvement via Questions

When initial confidence is low, progressive questions can increase confidence:

```yaml
question_weights:
  team_size:
    '1 developer': { trunk_based: +0.3 }
    '2-5 developers': { github_flow: +0.2 }
    '6+ developers': { gitflow: +0.2 }

  release_frequency:
    'Daily': { trunk_based: +0.3 }
    'Weekly': { github_flow: +0.3 }
    'Monthly+': { gitflow: +0.3 }

  version_maintenance:
    'Yes': { gitflow: +0.4 }
    'No': { github_flow: +0.2, trunk_based: +0.2 }
```

## Caching Strategy

```yaml
cache_config:
  validity_period: 7_days

  on_cache_hit:
    if_expired: 'Re-run detection'
    if_valid: 'Ask for confirmation of cached result'

  invalidate_on:
    - Major workflow change detected
    - User explicitly requests re-detection
    - Cache older than 7 days
```

## Implementation Guidelines

### For Agent Developers

1. **Always treat detection as advisory**

   ```python
   if detection.confidence >= 0.7:
       suggest_workflow(detection.workflow)
   else:
       ask_clarifying_questions()
   ```

2. **Present evidence transparently**

   ```python
   for indicator in detection.evidence:
       print(f"✓ {indicator}")
   ```

3. **Allow easy override**
   ```python
   # Always provide escape hatch
   options.append("None of the above")
   ```

### For Users

1. **High confidence doesn't mean certainty** - Always review the suggestion
2. **Evidence matters more than score** - Check if the evidence matches your actual workflow
3. **Migration is normal** - If you're changing workflows, tell BMAD
4. **Custom is OK** - Don't force-fit into standard patterns

## Testing Confidence Scores

Test scenarios and expected confidence ranges:

| Scenario                              | Expected Confidence | Expected Workflow |
| ------------------------------------- | ------------------- | ----------------- |
| Clean GitFlow with all branches       | 90-100%             | GitFlow           |
| GitHub Flow with consistent PR merges | 70-85%              | GitHub Flow       |
| Mixed patterns                        | 30-60%              | Unclear           |
| Fresh repo (<10 commits)              | 0-30%               | Unclear           |
| Trunk-based with feature flags        | 70-90%              | Trunk-based       |

## Future Improvements

1. **Machine Learning Enhancement**
   - Learn from user corrections
   - Adjust weights based on success rate

2. **Extended Pattern Recognition**
   - Detect GitLab Flow
   - Recognize scaled patterns (e.g., Scaled Trunk-Based)

3. **Context-Aware Detection**
   - Consider repository language/framework
   - Account for team size if available

## Conclusion

Confidence scoring enables intelligent suggestions while respecting user autonomy. The goal is to save time for the 80% common cases while gracefully handling the 20% edge cases.

Remember: **The best workflow is the one your team actually follows, not what the detector suggests.**
