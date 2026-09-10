# Milestones, Deliverables & Rubrics

Graded milestones are **M1, M2, M6, M9** plus the mid-course practical, final report, defense, and diagnostic test. The others (M0, M3, M4, M5, M7, M8, M10) are **formative** - they receive written feedback and feed the graded milestones, but carry no direct weight. This keeps the marking load sustainable while ensuring nobody drifts for four weeks unnoticed.

| Instrument | Type | Weight |
|---|---|---:|
| Session knowledge checks (best 9 of 11) | formative-graded | 10% |
| **M1** Cleaning + decision log | graded | 10% |
| **M2** Pipeline + leakage audit | graded | 10% |
| **A5** Mid-course practical - *unseen dataset* | graded | 15% |
| **M6** Ensemble champion + Model Card v1 | graded | 10% |
| **M9** Regularisation ablation | graded | 10% |
| Final report + notebook | graded | 20% |
| Oral defense | graded | 10% |
| Diagnostic reasoning test | graded | 5% |
| M0, M3, M4, M5, M7, M8, M10 | formative | 0% |

**Universal rule:** in every rubric below, raw predictive performance is worth **at most 20%**. Reasoning, protocol correctness, and honesty carry the rest.

---

## M0 - Dataset Fact Sheet *(formative, after S1)*

**Deliverable:** one notebook. Shape and dtypes; the columns that are empty or constant; three questions the data can answer; one it cannot; a one-paragraph problem statement naming the client, the unit of observation, the target, and a success criterion.

**Feedback focus:** did they name a *unit of observation*? Most will say "a listing" without noticing that a host may own 588 of them.

---

## M1 - Cleaning Pipeline + Decision Log ⬛ *graded, 10%, after S2*

**Deliverable:** notebook + decision log table + `test.parquet` written and untouched.

The decision log has one row per cleaning decision: **what I did / why / what I would have lost otherwise / what this could bias**.

| Criterion | Weight | Excellent (A) | Adequate (C) | Poor (F) |
|---|---:|---|---|---|
| Split discipline | 20% | Split first, on the correct grouping, justified from measured group structure | Split first, random, grouping not considered | Split after cleaning, or not sealed |
| Defect identification | 20% | Finds all major categories incl. deceptive duplicates and empty columns | Finds the obvious ones (types, missing) | Misses type coercion or missingness |
| Missingness reasoning | 25% | Identifies mechanism per column; **measures** the bias from dropping; imputation matched to mechanism | Notes the rates and imputes plausibly | `dropna()` or `fillna(mean)` unexamined |
| Decision log quality | 25% | Every decision has a defensible *why* and a stated risk | Most decisions justified | Log is a list of commands |
| Reproducibility | 10% | Runs clean top to bottom, seeded | Runs with minor fixes | Does not run |

**Common mistakes:** `dropna()` on the whole frame; imputing review scores with the mean when those listings have zero reviews; `drop_duplicates()` deleting multi-unit operators; cleaning before splitting and not noticing.

---

## M2 - Preprocessing Pipeline + Leakage Audit ⬛ *graded, 10%, after S3*

**Deliverable:** a `ColumnTransformer`/`Pipeline` object + written leakage audit.

The audit names each suspicious column, its mechanism, the **measured** inflation it causes, and the decision taken.

| Criterion | Weight | Excellent (A) | Adequate (C) | Poor (F) |
|---|---:|---|---|---|
| Pipeline correctness | 25% | All fitted transforms inside the pipeline; nothing fitted on validation data | Pipeline used; one transform fitted outside | Manual preprocessing on the full frame |
| Traps found | 25% | Finds the direct leak **and** the derived one; explains the mechanism of each | Finds the direct leak | Finds neither; reports the inflated score as a result |
| Inflation quantified | 15% | Reports before/after with a correct protocol | Reports that it "improved" | No measurement |
| Encoding choices | 20% | Cardinality-aware; target encoding handled fold-safely or rejected with reason | Reasonable one-hot throughout | Encodes 69 categories without comment; or leaks via target encoding |
| Feature justification | 15% | ≥3 engineered features defended on domain grounds | Features created, thinly justified | Features created with no rationale |

**Common mistakes:** `StandardScaler().fit(X)` before the split; target-encoding the neighbourhood on the full training set; treating the decoy column as a leak without measuring; dropping only the column named like the target.

---

---

*This file currently covers M0–M2. M3–M10 are released as we reach them.*
