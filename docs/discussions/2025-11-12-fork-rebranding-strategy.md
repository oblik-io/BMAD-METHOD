# Fork Rebranding Strategy - Legal and Practical Analysis

**Date:** 2025-11-12 20:00:00 EET
**Context:** Exploring options for fork naming and branding strategy
**Status:** 🔍 Discussion Phase - Decision Required
**Related:** [Governance Policy Framework](./2025-11-12-governance-policy-framework.md)

---

## Executive Summary

Аналіз можливості та доцільності перейменування BMAD-METHOD fork (наприклад, на "shi" або інше ім'я) для використання в oblik.io організації.

**Key Questions:**

- ✅ **Legally:** Чи можна перейменувати? (YES, з attribution)
- 🤔 **Practically:** Чи варто перейменовувати? (Depends on goals)
- ⏰ **Timing:** Коли приймати рішення? (Before oblik.io migration)

---

## Legal Analysis

### MIT License + Trademark Protection

**Source:** `LICENSE` file (lines 1-27)

#### What MIT License ALLOWS:

```
✅ Fork, modify, and distribute
✅ Use under DIFFERENT name
✅ Commercial use
✅ Sublicense
✅ Create derivative works
```

#### What TRADEMARK NOTICE RESTRICTS:

```
TRADEMARK NOTICE:
BMAD™, BMAD-CORE™ and BMAD-METHOD™ are trademarks of BMad Code, LLC.
The use of these trademarks does not grant any rights to use
the trademarks for any other purpose.
```

**Implications:**

❌ **CANNOT use in fork name:**

- BMAD-METHOD (exact trademark)
- BMad Method, BMad Core (variations)
- Any confusingly similar names

✅ **CAN use for fork:**

- shi (your example)
- oblik-method
- Any name NOT using BMAD trademarks

### Attribution Requirements (MANDATORY)

**MIT License requirement:**

> The above copyright notice and this permission notice shall be
> included in all copies or substantial portions of the Software.

**What this means:**

```markdown
## Required in LICENSE file:

Based on BMAD-METHOD
Original Copyright (c) 2025 BMad Code, LLC
Licensed under MIT License
Source: https://github.com/bmad-code-org/BMAD-METHOD

Modified work Copyright (c) 2025 [Your Organization]
```

**Where to include:**

1. **LICENSE file** (mandatory)
2. **README.md** (highly recommended)
3. **Documentation** (good practice)
4. **Agent/workflow headers** (optional)

---

## Rebranding Options Analysis

### Option 1: Conservative Fork Name

**Name:** `oblik-io/BMAD-METHOD-fork`
**Brand:** "BMAD-METHOD for oblik.io"

**Structure:**

```
oblik-io/BMAD-METHOD-fork/
├── LICENSE (original + attribution)
├── README.md
│   "Fork of BMAD-METHOD by oblik.io"
│   "Upstream: bmad-code-org/BMAD-METHOD"
├── .bmad/
│   ├── bmm/  (keep upstream names)
│   ├── bmb/
│   └── oblik/ (custom additions)
```

**Pros:**

- ✅ Absolutely clear це fork
- ✅ Leverage BMAD brand recognition
- ✅ Easy upstream contribution
- ✅ Minimal rebrand effort
- ✅ No trademark confusion
- ✅ Straightforward for team

**Cons:**

- ❌ Less distinctive identity
- ❌ Always "fork" status perception
- ❌ Tied to upstream branding
- ❌ "fork" suffix може виглядати непрофесійно

**Use case:** Best for organizations that plan heavy upstream contribution and want to stay aligned.

---

### Option 2: Partial Rebrand

**Name:** `oblik-io/oblik-method`
**Brand:** "oblik Method (based on BMAD-METHOD)"

**Structure:**

```
oblik-io/oblik-method/
├── LICENSE (dual copyright)
├── README.md
│   "# oblik Method"
│   "Based on BMAD-METHOD by BMad Code, LLC"
│   "Enhanced with oblik.io features"
├── docs/
│   ├── ATTRIBUTION.md (detailed credits)
├── .bmad/
│   ├── bmm/  (keep structure, upstream compatible)
│   ├── bmb/
│   └── oblik/ (custom modules)
```

**Pros:**

- ✅ Own organizational identity
- ✅ Still connected to BMAD (recognition)
- ✅ Upstream compatible (structure kept)
- ✅ Trademark safe
- ✅ Professional appearance
- ✅ Can evolve independently

**Cons:**

- ❌ Moderate rebrand effort
- ❌ Need clear attribution everywhere
- ❌ May confuse "is it BMAD or not?"
- ❌ Marketing overhead (explain relationship)

**Use case:** Best for organizations with significant custom features that want own brand but maintain upstream compatibility.

---

### Option 3: Full Rebrand

**Name:** `oblik-io/shi`
**Brand:** "shi Framework"

**Structure:**

```
oblik-io/shi/
├── LICENSE (dual copyright, prominent attribution)
├── README.md
│   "# shi Framework"
│   "Derived from BMAD-METHOD (MIT License)"
├── docs/
│   ├── ATTRIBUTION.md (complete history)
│   └── DIFFERENCES.md (divergence from upstream)
├── shi/
│   ├── shi-method/    (was bmm)
│   ├── shi-builder/   (was bmb)
│   └── shi-innovation/ (was cis)
```

**Pros:**

- ✅ Complete independence
- ✅ Own trademark potential
- ✅ Custom identity
- ✅ No naming confusion
- ✅ Marketing freedom
- ✅ Can diverge freely

**Cons:**

- ❌ High rebrand effort (всі файли, docs, код)
- ❌ Lost BMAD brand recognition
- ❌ Harder upstream sync (structure divergence)
- ❌ Community split risk
- ❌ Need strong justification
- ❌ Maintenance burden (independent ecosystem)

**Use case:** Best for organizations building commercial product with >50% custom code, or when upstream direction diverges significantly.

---

## Real-World Examples

### Successful Rebrands

#### 1. Chrome → Brave Browser

```
Strategy: Full rebrand
Attribution: Clear Chromium credits
Result: Successful distinct product
Lesson: Strong differentiation needed
```

#### 2. MySQL → MariaDB

```
Strategy: Full rebrand (post-Oracle acquisition)
Attribution: Maintained compatibility
Result: Thriving independent community
Lesson: Governance concerns justified fork
```

#### 3. Red Hat Enterprise Linux → Rocky Linux

```
Strategy: Community fork with new name
Attribution: Compatible, clear lineage
Result: Successful alternative
Lesson: Community need drove adoption
```

### Cautionary Tales

#### 1. Hudson → Jenkins

```
Problem: Trademark disputes, legal drama
Lesson: Clear legal foundation critical
Impact: Community confusion, slow migration
```

#### 2. Mambo → Joomla

```
Problem: Split community, confused users
Lesson: Communication is key
Impact: Both projects survived but competition
```

---

## Decision Framework

### When to Keep BMAD Name (Conservative)

**Choose Option 1 if:**

- [ ] Plan heavy upstream contribution (>50% changes go back)
- [ ] Fork duration: temporary (<1 year)
- [ ] Team size: small (<5 people)
- [ ] Custom features: minimal (<20% divergence)
- [ ] Upstream alignment: high (same direction)
- [ ] Legal resources: limited
- [ ] Marketing need: none (internal use)

**Example scenario:** KRTM project using BMAD-METHOD temporarily.

### When to Partial Rebrand (Balanced)

**Choose Option 2 if:**

- [ ] Plan some upstream contribution (20-50%)
- [ ] Fork duration: medium (1-3 years)
- [ ] Team size: medium (5-20 people)
- [ ] Custom features: moderate (20-50% divergence)
- [ ] Upstream alignment: moderate
- [ ] Legal resources: adequate
- [ ] Marketing need: moderate (external projects)
- [ ] Own organizational identity important

**Example scenario:** Enterprise org with custom agents and workflows for multiple projects.

### When to Full Rebrand (Independent)

**Choose Option 3 if:**

- [ ] Plan minimal upstream contribution (<20%)
- [ ] Fork duration: long-term (3+ years)
- [ ] Team size: large (20+ people)
- [ ] Custom features: extensive (>50% divergence)
- [ ] Upstream alignment: low (different direction)
- [ ] Legal resources: strong (lawyer review)
- [ ] Marketing need: high (commercial product)
- [ ] Building competitive product

**Example scenario:** Commercial product based on BMAD but with radically different approach.

---

## oblik.io Specific Analysis

### Current Situation Assessment

**Facts:**

- Organizations: @joyshmitz (personal), felectra (temp), oblik.io (planned)
- Current fork: felectra/BMAD-METHOD (wrong place)
- Primary use case: KRTM project (temp, government)
- Custom features: minimal (mostly consuming upstream)
- Duration: unclear (project lifecycle dependent)
- Team size: small (primarily @joyshmitz)

**Alignment check:**

```
✅ Temporary fork duration
✅ Small team
✅ Minimal custom features
✅ High upstream alignment
✅ Limited legal resources
✅ Internal use (no marketing)
```

**Conclusion:** Criteria match **Option 1 (Conservative)**

### Recommended Strategy for oblik.io

#### Phase 1: Now → KRTM Completion (Conservative)

**Repository:** `oblik-io/BMAD-METHOD`

```
Name: Simple fork name
Brand: "BMAD-METHOD fork maintained by oblik.io"
Structure: Keep bmm/, bmb/, cis/ names
Custom: Add oblik/ folder for extensions
Attribution: Clear in LICENSE + README

Rationale:
- Focus on using, not branding
- Easy upstream sync
- Minimal maintenance overhead
- Can rebrand later if needed
```

#### Phase 2: Post-KRTM Evaluation (Conditional)

**Trigger decision when:**

- [ ] KRTM project complete
- [ ] Have 3+ additional projects using fork
- [ ] Custom features reach 30%+ of codebase
- [ ] Team grows to 5+ people
- [ ] Commercial product consideration

**Then reassess:** Option 2 (Partial) or Option 3 (Full)

---

## Legal Compliance Checklist

### For ANY rebranding option:

#### LICENSE File Requirements

```markdown
✅ Include original MIT license text
✅ Original copyright: "Copyright (c) 2025 BMad Code, LLC"
✅ Your copyright: "Modified work Copyright (c) 2025 [Your Org]"
✅ Attribution statement: "Based on BMAD-METHOD"
✅ Original source URL: https://github.com/bmad-code-org/BMAD-METHOD
✅ Trademark notice preservation
✅ Date of fork
```

#### README.md Requirements

```markdown
✅ Clear statement: "Based on BMAD-METHOD"
✅ Link to original: bmad-code-org/BMAD-METHOD
✅ Attribution to BMad Code, LLC
✅ License badge (MIT)
✅ Differences section (what changed)
```

#### ATTRIBUTION.md (Recommended)

```markdown
✅ Detailed fork history
✅ Original authors credit
✅ List of significant modifications
✅ Upstream contribution guidelines
✅ Trademark disclaimers
```

#### Code/Documentation Headers

```markdown
Optional but recommended:
✅ Original author comments preserved
✅ Fork notation in changed files
✅ Attribution in generated content
```

---

## Implementation Plan (If Rebrand Approved)

### Pre-Rebrand Phase

```bash
Week 1: Legal Foundation
- [ ] Draft LICENSE with proper attribution
- [ ] Create ATTRIBUTION.md
- [ ] Document trademark strategy
- [ ] Legal review (if budget allows)
- [ ] Get team consensus

Week 2: Technical Planning
- [ ] Inventory all rename locations
- [ ] Create migration scripts
- [ ] Test rename in clone
- [ ] Document rollback procedure
- [ ] Prepare communication
```

### Rebrand Execution

```bash
Week 3: Repository Changes
- [ ] Create new repository (if name change)
- [ ] Update LICENSE file
- [ ] Update README.md
- [ ] Update all documentation
- [ ] Rebrand internal references
- [ ] Update CI/CD configs
- [ ] Test all workflows

Week 4: Deployment
- [ ] Migrate git history
- [ ] Update team remotes
- [ ] Archive old fork (if applicable)
- [ ] Monitor for issues
- [ ] Support team migration
```

### Post-Rebrand

```bash
Week 5+: Communication & Support
- [ ] Notify upstream (courtesy)
- [ ] Update external references
- [ ] Document migration path
- [ ] Help users transition
- [ ] Monitor community feedback
```

---

## Cost-Benefit Analysis

### Option 1: Conservative (BMAD-METHOD fork)

**Costs:**

- Time: 2-4 hours (setup attribution)
- Effort: Minimal
- Risk: Negligible
- Ongoing: Low (easy sync)

**Benefits:**

- Speed: Fastest to production
- Recognition: Leverage BMAD brand
- Compatibility: Full upstream sync
- Team: Easy onboarding

**ROI:** Excellent for temporary/small use

---

### Option 2: Partial Rebrand (oblik-method)

**Costs:**

- Time: 20-40 hours (rebrand effort)
- Effort: Moderate
- Risk: Medium (confusion potential)
- Ongoing: Medium (sync + brand management)

**Benefits:**

- Identity: Own organizational brand
- Flexibility: Can evolve independently
- Professional: Better external appearance
- Marketing: Own positioning

**ROI:** Good for growing organizations

---

### Option 3: Full Rebrand (shi)

**Costs:**

- Time: 80-160 hours (complete rebrand)
- Effort: High
- Risk: High (community split, confusion)
- Ongoing: High (independent ecosystem)

**Benefits:**

- Independence: Complete control
- Trademark: Own intellectual property
- Product: Commercial opportunity
- Divergence: Freedom to innovate

**ROI:** Only if building commercial product

---

## Open Questions for Decision

### Strategic Questions

1. **Purpose:** Що головна мета fork?
   - [ ] Temporary use (KRTM)
   - [ ] Long-term internal tool
   - [ ] Commercial product foundation
   - [ ] Community alternative

2. **Differentiation:** Наскільки відрізнятиметься від upstream?
   - [ ] <20% (mostly consuming)
   - [ ] 20-50% (moderate customization)
   - [ ] > 50% (significant divergence)

3. **Contribution:** Плани щодо upstream contribution?
   - [ ] Heavy contributor (most changes go back)
   - [ ] Occasional contributor
   - [ ] Independent (minimal contribution)

4. **Duration:** Скільки триватиме fork?
   - [ ] Short-term (<1 year)
   - [ ] Medium-term (1-3 years)
   - [ ] Long-term (3+ years)
   - [ ] Permanent

5. **Team:** Розмір команди що використовує?
   - [ ] Individual (@joyshmitz)
   - [ ] Small team (<5)
   - [ ] Medium team (5-20)
   - [ ] Large team (20+)

6. **Commercial:** Плани комерціалізації?
   - [ ] No (internal only)
   - [ ] Maybe (future consideration)
   - [ ] Yes (building product)

### Tactical Questions

7. **Timeline:** Коли потрібне рішення?
   - [ ] Immediately (before anything)
   - [ ] Before oblik.io migration
   - [ ] After first project (KRTM)
   - [ ] Can wait (flexible)

8. **Resources:** Доступні ресурси для rebrand?
   - [ ] Time: hours available?
   - [ ] Budget: legal review?
   - [ ] Team: support available?

9. **Reversibility:** Чи важлива можливість повернутися?
   - [ ] Must be reversible
   - [ ] Prefer reversible
   - [ ] One-way decision OK

---

## Recommendation Summary

### For Current Situation (oblik.io, KRTM use case)

**RECOMMENDED: Option 1 (Conservative)**

```
Repository: oblik-io/BMAD-METHOD
Approach: Fork with clear attribution
Timeline: Implement before oblik.io migration
Effort: 2-4 hours
Risk: Minimal
```

**Rationale:**

1. ✅ Matches current use case (temporary, small, consuming)
2. ✅ Fastest to production (minimal overhead)
3. ✅ Reversible decision (can rebrand later)
4. ✅ Focus on using not branding
5. ✅ Easy upstream contribution (structure aligned)

**When to reassess:**

- After KRTM completion
- When custom features >30%
- When team size >5
- When commercial consideration

### Alternative Path (If Strong Reasons)

**IF you have specific need for own brand:**

**CONSIDER: Option 2 (Partial Rebrand)**

```
Repository: oblik-io/oblik-method
Approach: Own name + BMAD attribution
Timeline: After governance decisions finalized
Effort: 20-40 hours
Risk: Medium
```

**Only if:**

- Have multiple projects planned (3+)
- Building organizational brand important
- External facing (not just internal)
- Can justify time investment

---

## Success Criteria

**Whichever option chosen, success means:**

1. ✅ **Legal Compliance**
   - Proper attribution in place
   - No trademark violations
   - MIT license terms followed

2. ✅ **Team Clarity**
   - Everyone understands fork vs upstream
   - Clear contribution guidelines
   - No confusion about origins

3. ✅ **Upstream Relationship**
   - Can contribute back easily
   - Sync mechanism works
   - Good community standing

4. ✅ **Practical Usability**
   - Team can use effectively
   - Documentation clear
   - Maintenance sustainable

5. ✅ **Strategic Alignment**
   - Supports oblik.io goals
   - Matches resource availability
   - Enables future flexibility

---

## Next Steps

### Immediate (This Week)

1. **Read this analysis completely**
2. **Answer Open Questions section**
3. **Decide preliminary direction:**
   - Conservative (keep BMAD name)
   - Partial rebrand (oblik-method)
   - Full rebrand (shi or other)
4. **Document decision rationale**

### Short-term (Before oblik.io migration)

5. **If Conservative chosen:**
   - Draft LICENSE with attribution
   - Update README with fork notice
   - Proceed with migration

6. **If Rebrand chosen:**
   - Complete legal review
   - Create detailed rebrand plan
   - Execute rebrand before migration

### Long-term (Post-Migration)

7. **Evaluation checkpoint:**
   - After KRTM complete
   - Assess actual vs planned usage
   - Revisit decision if needed

---

## References

**Legal:**

- [MIT License Text](../../LICENSE)
- [GitHub Fork Documentation](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks)
- [Trademark Basics](https://www.uspto.gov/trademarks)

**Related Discussions:**

- [Governance Policy Framework](./2025-11-12-governance-policy-framework.md)
- [Production Process Improvements](./2025-11-12-production-process-improvements.md)

**BMAD Documentation:**

- [Contributing Guidelines](../../CONTRIBUTING.md)
- [Enterprise Agentic Development](../../.bmad/bmm/docs/enterprise-agentic-development.md)

**Examples:**

- [MariaDB vs MySQL](https://mariadb.org/)
- [Rocky Linux](https://rockylinux.org/)
- [Brave Browser](https://brave.com/)

---

**Status:** 🔍 Decision Required Before Migration

**Priority:** P2 (важливо, але не критично - після governance decisions)

**Author:** @joyshmitz
**Last Updated:** 2025-11-12
**Version:** 1.0.0-draft
