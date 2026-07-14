# Iteration 3 — data verification + expansion (v4 → v5)

Triggered by your answers: you pointed me to `FLockit_GPFormer/output_arises_bolus/cgm`
(the CGM-only 5-seed source), pushed back on "statistically tied," and asked about
clinical metrics, persistence/pooled baselines, and the bolus variant. I aggregated the
raw per-seed CSVs (`scratchpad/aggregate.py`, `clinical.py`) and revised accordingly.

## 1. Table 1 numbers VERIFIED (resolves the #1 reviewer concern)
Aggregating `cgm/seed_{42,43,44,46,47}/<method>/best_model_*_irt.csv` reproduces Table 1:
- Held-in: fedavg 18.64/19.80/22.38/19.53 (avg 20.09), mldg 18.46/19.68/22.30/19.53
  (avg 19.99), fedprox, apfl, decoupled, all three ditto, and Local — **all match** to
  0.01 mg/dL. **ARISES single-cohort OOD collapse = 28.51 ± 6.85 — exact match.**
- So the "untraceable numbers" objection is resolved: the source simply hadn't been in
  the repo copy the reviewers saw. (One <0.1 mg/dL bookkeeping nuance on the Local-OOD
  mean; see UNSURE #29.)

## 2. THREE OOD cohorts, not one (major strengthening — addresses reviewers' single-OOD-cohort limitation)
The cgm outputs contain OOD results for **ReplaceBG, BrisT1D, and Flair**. Added a new
Table (`tab:ood`) and rewrote the OOD Results + Discussion. The robustness result now
**replicates on all three** held-out cohorts:
- Global models beat the mean single-cohort model on every cohort.
- single-ARISES collapses on all three (28.51 / 32.39 / 30.99) with sd 30–40× the
  federated models'.
- Updated Methods (seven cohorts, not five), Table 1 caption, ethics statement, abstract,
  Limitation (ii), and all singular "the OOD cohort" phrasings.

## 3. Significance test (resolves your "statistically tied" pushback AND editor NEW-3)
You were right that MLDG is better in both regimes — it is numerically best in **every**
held-in and OOD comparison and beats FedAvg on **4/5 seeds**. But a paired t-test at n=5
does not reach p<0.05 (held-in Δ=−0.09 mg/dL, t≈−1.3). So I replaced both the earlier
over-hedge ("statistically indistinguishable," which asserted non-significance without a
test) and any "MLDG is best" over-claim with the accurate middle: **"a small, consistent,
but not statistically significant improvement."** New Results heading + Discussion +
abstract + Limitation (iii) all say this. Also corrected the earlier false "FedAvg/FedProx
OOD missing a seed" note — that was the *bolus* variant; CGM OOD is complete n=5.

## 4. Clinical metrics (partial — what the data supports)
The CSVs carry TIR (time-in-range) actual/predicted and a forecast time-lag, but **no**
Clarke/Parkes grid or event-level detection (those need per-window predictions we don't
have exported). Added a Results paragraph: predicted vs actual TIR agree within ~2–4 pts
held-in and ~1.7–2.7 pts OOD; forecast lag ≈20 min (≈20–22 OOD), i.e. a chunk of the
30-min horizon is effectively persistence. Framed honestly with the full error grid as
the remaining gap.

## 5. Persistence & pooled-central baselines — NOT available
Neither exists in the outputs (no `persist*`/`central*`/`pool*` dirs). They can't be
produced without a new training run, which I can't do here. Kept as Limitations (iv,
viii) + Future work. (UNSURE — you'd need to run these.)

## 6. Bolus — kept, reframed with a real synthesis (your question)
`output_arises_bolus/bolus` is a full rerun (all methods, ~5 seeds), not the 2-seed
preliminary REPORT.md described. Synthesis: bolus does **nothing** for the global models
(±0.1 mg/dL, MLDG OOD unchanged at 21.34) BUT consistently **damps the single-ARISES
collapse** — lower mean and ~half the sd on all three OOD cohorts (ReplaceBG 26.86±3.45
vs 28.51±6.85; BrisT1D 31.95±3.42 vs 32.39±5.84; Flair 29.81±3.09 vs 30.99±6.23). The
coherent story: an exogenous input mildly regularises against the worst single-cohort
overfitting — the very failure federation already prevents, so bolus is redundant once
federated. **My recommendation: keep it** (it reinforces the main robustness narrative).
Upgraded the Methods + Results bolus text accordingly. (Confirm — UNSURE #31.)

## Net effect on the paper's standing
The two biggest reviewer objections (untraceable numbers; single OOD cohort) are now
resolved by data, and the significance question is answered honestly in a way that
supports your intuition without over-claiming. Remaining deferred items (full error grid,
persistence, pooled-central, LOCO, more seeds) genuinely need new runs.
