# Iteration 1 — how we revised v1 → v2 in response to the reviews

Three reviewer critiques of v1 are saved alongside this file:
`iter1_reviewer1_clinical.md`, `iter1_reviewer2_ml.md`, `iter1_reviewer3_rigor.md`.
All three recommended **Major revision** and converged on the same core issues.

Each concern below is tagged **[FIXED in v2]** (addressed by rewriting/reframing),
**[CAVEATED]** (acknowledged in-text as a limitation because it needs data/experiments
we don't have), or **[→UNSURE]** (needs the author's input; logged in `UNSURE.md`).
We did **not** invent or alter any experimental number.

## Over-claiming / language (R1-M3, R2-M8, R3-M3) — [FIXED in v2]
- Removed "guarantee", "safely", "never collapsed", "transferred safely" from
  abstract, author summary, Discussion heading and body. Replaced with hedged
  wording tied to "the one held-out cohort tested."
- Retitled Discussion subsection "Federation as a robustness guarantee..." →
  "...more reliable transfer, not only an accuracy gain."
- Contextualised every effect size against CGM sensor error (~8–15 mg/dL) and
  seed sd; "substantially better" softened.
- Title: "a cross-country deployment" → "a cross-site deployment prototype"
  (two machines were not established as cross-country). [→UNSURE #12 to confirm]

## Reframe the OOD benefit (R1-M2, R2-M1) — [FIXED in v2]
- Now state plainly that 3 of 4 single-cohort models transfer within ~0.5 mg/dL
  of federation, and only single_ARISES collapses; reframed the benefit as
  "insurance against deploying the one bad-cohort model," not a 2 mg/dL average win.
- Added the per-single-model OOD numbers to the Results text.

## Method-ranking not significant (R1-minor3, R2-M6, R3-M3/M4) — [FIXED in v2]
- Downgraded "MLDG is the strongest global strategy" → "numerically best,
  within seed variation"; aligned abstract/Results/Discussion strength.
- Added explicit statement that margins (~0.1 mg/dL) are below seed sd and no
  significance test was run; noted OOD compares n=5 (MLDG) with n=4 (FedAvg/FedProx).

## MLDG mechanism (R2-M3) — [FIXED in v2] + [CAVEATED]
- Softened "MLDG optimises directly for the cross-domain transfer we evaluate" →
  it simulates cross-*patient* shift within a client, not cross-cohort shift; the
  causal reading is downgraded to a correlation.
- Clarified the decoder is single-shot (learned start token; encoder carries history).
- Full inner/outer update equations + inner-lr are [→UNSURE #13]; flagged that the
  "reuses Adam state" description needs a precise spec.

## Baseline fairness (R2-M2) — [CAVEATED] + [→UNSURE]
- Added a caveat that FedProx used a single untuned µ=0.05, so "weakest" is
  softened to "lowest here, untuned."
- Added a caveat that APFL may be under-tuned (possible frozen-α issue noted in
  the engineering report); flagged for verification. [→UNSURE #14]

## Privacy / deployment framing (R1-M7, R2-M8) — [FIXED in v2]
- Reframed the system as a feasibility/architecture prototype, not deployment-ready.
- "compatible with data-protection regimes" → no-raw-data-movement is a *necessary
  but not sufficient* step; security caveats moved into the Discussion deployment
  paragraph, not just Limitations.

## Clinical metrics (R1-M1, R1-M6) — [CAVEATED] + [→UNSURE]
- Added to Limitations: RMSE-only is behind field norm; no Clarke/Parkes error
  grid, MARD, hypo/hyper detection, or predictive uncertainty. Added to Future work.
- Flagged whether error-grid / MARD / event-detection numbers already exist. [→UNSURE #15]

## Design gaps → Limitations/Future work — [CAVEATED]
- No persistence / simple baseline (R2-M4): acknowledged; flagged whether our own
  persistence numbers exist. [→UNSURE #16]
- Single OOD cohort; leave-one-cohort-out available (R1-M2, R2-M5): strengthened
  in Limitations + Future work as the top next experiment.
- Finetuning: reframed — done on ReplaceBG's large 166-patient cohort (not a small
  clinic), gap ~0.3–0.4 mg/dL and untested; softened, added protocol/variant caveat.
- Seed sd understates patient-level deployment uncertainty (R3-M5): sentence added.
- Skipped seed 45 / irregular seed set noted.

## Smaller fixes — [FIXED in v2]
- Abstract de-jargoned: leads with the clinical problem, method roster deferred.
- "clinically actionable 30-minute horizon" → "commonly used warning horizon."
- Removed the 60-min claim from Methods/abstract (only 30-min reported); kept as future work.
- Un-bolded "Ours" in the external-comparison table (avoids implying a head-to-head win).
- Global normalisation: stated it is computed from the training cohorts (no OOD
  leakage). [→UNSURE #17 to confirm scope]
- Stated up front (Introduction) that findings are for adult T1D only.

## Preserved (reviewers praised) — no change
- The by-patient vs by-time external-comparison framing (all three reviewers
  called this the most rigorous part; R3 said keep it).
