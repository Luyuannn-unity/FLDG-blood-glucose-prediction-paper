# Review — *Federated and meta-learned blood-glucose forecasting across sites: a domain-generalisation benchmark and a cross-country deployment*

**Reviewer 2 (machine learning: federated learning, domain generalisation, meta-learning, time-series transformers)**
**Venue:** PLOS Digital Health

---

## 1. Recommendation: **Major revision**

The manuscript addresses a genuinely useful and well-motivated question — which federated strategy to use for cross-site CGM forecasting, and whether held-in accuracy and out-of-distribution (OOD) transfer diverge — and the by-patient evaluation, the explicit held-in/OOD separation, and the honest positioning against by-time external baselines (Table 2) are commendable and above the norm for this literature. The writing is clear and the clinical framing is sound. However, as an ML contribution the paper has several methodological weaknesses that, in their current form, undercut its central claims. In brief: (i) the headline robustness result rests on a single OOD cohort and on a "collapse" number (single-ARISES OOD RMSE) that is **inconsistent across the three supporting artifacts I was given**; (ii) at least one baseline (APFL) appears to be **misconfigured** (the REPORT notes a frozen-α bug that contradicts the hyperparameters stated in the paper), and FedProx's single untuned µ makes the "FedProx is weakest" conclusion unsafe; (iii) the MLDG description — a second-order meta-gradient whose "inner step reuses the outer Adam optimiser state" — is non-standard, under-specified, and as written not reproducible, and the meta-train/meta-test split is *within-client across patients*, which does not simulate the *cross-cohort* shift the paper actually evaluates; (iv) there is **no naive/persistence or simple baseline**, so we cannot tell whether a 4.9 M-parameter transformer is warranted, especially since the paper's own Table 2 shows persistence within ~1 mg/dL of the transformer; (v) the method-ranking claims ("MLDG is the strongest global strategy") are asserted on differences of ~0.1 mg/dL that are smaller than the reported seed standard deviations, with no significance test; and (vi) the "we built a real FL system" contribution is over-claimed relative to a two-machine demo. None of these are fatal in principle, but together they require substantial additional experiments and rewriting. I believe they are addressable, hence major revision rather than reject.

---

## 2. Major concerns

### M1. The headline OOD "collapse" number is not reproducible across the supplied artifacts, and the main table may not match the underlying run.

The paper's central rhetorical device is that a single-cohort model "collapses" OOD:

> "the ARISES-only model, which collapses on ReplaceBG ($28.51 \pm 6.85$)" (Results); repeated in Discussion as "collapsed on ReplaceBG ($28.51 \pm 6.85$ mg/dL)."

This exact figure appears in **neither** supporting artifact. `RESULTS_arises_bolus.md` gives `single_ARISES` OOD = **26.86 ± 3.45**; `REPORT.md` (3-seed, CGM-only) gives **31.8 ± 5.95**. Three different values (28.51 / 26.86 / 31.8) for the same load-bearing claim. Similarly, the Local OOD average reported as **23.54** does not equal the mean of the four single-cohort OOD numbers in `RESULTS_arises_bolus.md` (22.01, 21.85, 26.86, 21.67 → **23.10**), and the per-cohort Local held-in numbers in Table 1 (e.g. ARISES 22.04, T1D-UOM 19.80) differ from the singles in the results file (21.94, 19.94).

Compounding this, the one detailed results artifact I was given (`RESULTS_arises_bolus.md`) is explicitly the **bolus** variant (`output_arises_bolus/bolus/`, "ARISES Bolus — Results Summary"), whereas Table 1 is labelled "**CGM-only**." I therefore could not verify Table 1 against any provided source, and the numbers I *could* cross-check do not line up. Because the entire "robustness guarantee" narrative hinges on this one collapse, the authors must (a) identify the exact run and seeds that produced Table 1, (b) reconcile the single-ARISES OOD figure across all reported locations, and (c) confirm the main table is CGM-only and not inadvertently drawn from the bolus run. As it stands this is a reproducibility and correctness problem in the paper's most important result.

### M2. APFL appears misconfigured; FedProx is untuned — so the baseline comparison is not fair.

`REPORT.md` states plainly:

> "For APFL we suspect this is the known frozen-α issue (α never moves from its 0.25 initialisation when its learning rate is set to the model's lr)."

But the manuscript claims APFL was run with "an adaptively updated α (initial 0.25, **α learning rate 0.1**)." These are contradictory: either α was frozen at 0.25 (the REPORT's diagnosis, α-lr = model lr = 1e-4), in which case APFL reduces to a fixed 25/75 mixture and is **not APFL at all** and is an unfair, under-tuned baseline; or α-lr was truly 0.1 and the REPORT's concern is stale. This must be resolved in code and the runs re-executed if α was frozen. A benchmark whose stated purpose is a head-to-head comparison cannot include a mis-specified personalised baseline.

Relatedly, FedProx is run at a **single, untuned** µ = 0.05, yet the paper repeatedly concludes "FedProx is consistently the weakest of the three global strategies." A proximal coefficient is exactly the kind of hyperparameter that must be swept (as Ditto's µ was, over {0.01, 0.1, 1.0}) before declaring a method inferior. MLDG's key hyperparameters (inner-loop learning rate / meta step size, meta-train/meta-test ratio) are not reported at all. The comparison currently mixes tuned and untuned methods, which biases the ranking.

### M3. The MLDG formulation is non-standard, under-specified, and its mechanism is mismatched to the transfer it is evaluated on.

Two distinct problems.

**(a) "Reusing the outer Adam optimiser state" in the inner step.** The paper describes MLDG as:

> "the model is updated with a second-order meta-gradient (the inner step reuses the outer Adam optimiser state)."

Canonical MLDG (Li et al. 2018) performs the inner adaptation with plain SGD at a fixed inner learning rate and differentiates the meta-test loss through that inner step. Reusing Adam's accumulated first/second moments for the inner update is unusual and raises concrete correctness questions that the paper does not answer: Does the inner step *advance* Adam's moment buffers (corrupting the subsequent outer update's momentum)? If the second-order term is real, is the graph retained through Adam's bias-corrected adaptive denominator (`create_graph=True`), or is this actually a first-order/FOMAML-style approximation being described loosely as "second-order"? The effective inner learning rate now depends on moment estimates that themselves depend on meta-train gradients, coupling the two splits in a way that is neither analysed nor ablated. As written, this cannot be reproduced from the text. Please give the exact inner/outer update equations, state whether the Hessian-vector product is computed, and report the inner learning rate.

**(b) The meta-split does not simulate the shift being evaluated.** The paper splits "the patient domains ... into meta-train and meta-test partitions" **within each client**, then FedAvg-aggregates. So MLDG only ever simulates *cross-patient* shift inside a single cohort; it never sees *cross-cohort* shift during meta-optimisation. Yet the OOD test (ReplaceBG) is precisely a *cross-cohort* shift. The Discussion's causal claim —

> "MLDG optimises directly for the cross-domain transfer we evaluate"

— therefore overstates the mechanism: MLDG optimises for cross-*patient* transfer within a site, not cross-cohort transfer. A federated-DG design that meta-splits *across clients* (the standard FedDG formulation, e.g. as surveyed in your ref li2025fedDGsurvey) would actually target the evaluated shift; the authors should either implement that, or soften the causal interpretation to a correlation. With ARISES (8 train patients) and T1D-UOM (10), the within-client patient-domain pool is also very small, so the meta-split is coarse — please report how many patient-domains fall on each side.

### M4. No naive / simple baseline — the transformer's complexity is unjustified.

There is no persistence (last-value / zero-order-hold), no linear/AR extrapolation, and no simple RNN baseline in the main experiments. This is a standard and, here, decisive omission: your own Table 2 shows persistence at **19.44** (HUPA-UCM) and **22.24** (T1D-UOM) from GlucoFM-Bench, versus your MLDG 18.46 / 19.53 — i.e. a 4.9 M-parameter, 6-encoder/2-decoder transformer is beating a trivial baseline by ~1–3 mg/dL. Readers cannot judge whether the architecture, the federation, or neither is doing the work without a persistence line in Table 1 (per client, held-in and OOD) and ideally a simple LSTM (which GlucoFM-Bench found *best* under full-shot). This matters doubly for the OOD claim: if persistence transfers to ReplaceBG at ~22 mg/dL, then "federation buys robustness" must be quantified against the trivial predictor that is robust by construction. Please add persistence and at least one lightweight learned baseline to every cell of Table 1.

### M5. The OOD conclusion rests on a single held-out cohort, when leave-one-cohort-out is essentially free.

The paper's strongest claim — robust transfer under distribution shift — is drawn from **one** OOD cohort (ReplaceBG), which the Limitations rightly flag. But with four training cohorts, a **leave-one-cohort-out (LOCO)** protocol yields four additional OOD estimates at no new data cost and would directly test whether "every federated model generalised ... and none collapsed" holds beyond a single, large, relatively benign US cohort. ReplaceBG (166+ patients) may also be an *easy* OOD target; a single favourable draw cannot support a "robustness guarantee" (a phrase used in the abstract and a section heading — see M8 on over-claiming). LOCO would substantially de-risk the central contribution and is the single most valuable additional experiment the authors could run.

### M6. Method-ranking claims are not statistically supported.

The Results and Discussion repeatedly assert a ranking — "MLDG is the strongest global strategy," "MLDG the best-supported default," "FedProx ... weakest." But the margins are ~0.1 mg/dL (held-in avg 19.99 vs 20.09; OOD 21.34 vs 21.43) against reported seed sds of 0.08–0.19 in `RESULTS_arises_bolus.md`. These differences are within noise. The Limitations concede "no formal significance test," yet the body text still states the ranking as fact. Please run paired tests across the shared seeds (e.g. paired t / Wilcoxon on per-seed OOD RMSE, or seed-blocked comparisons) and downgrade the language wherever differences are not significant. The defensible headline is almost certainly "all federated strategies transfer comparably and all beat single-cohort training OOD," not "MLDG wins."

### M7. Finetuning experiment is confounded and its effect is within noise.

The finetuning arm finetunes the global model on ReplaceBG's training patients vs. training on ReplaceBG from scratch, and concludes the federated init is a better starting point. Three issues: (a) the gap (21.04 vs 21.38) is ~0.34 mg/dL with sds of 0.04–0.09 — small, and no test is reported; (b) ReplaceBG has 166 training patients / ~980 k windows — a *large* new site, so the "a small clinic benefits" narrative is not what was tested; the interesting regime is a *data-poor* new site, which should be simulated by subsampling ReplaceBG patients; (c) the from-scratch comparator's protocol is unspecified (learning rate, number of rounds/epochs, early-stopping, which layers are finetuned) — if it used the same 25-round budget as federated training it may simply be undertrained, which would inflate the finetuning advantage. Please add the finetuning protocol, a data-fraction sweep, and significance tests, and temper "a site's own data trained in isolation did not beat the federated model even on that site's own patients," which is a strong claim on a large cohort with a marginal, untested gap.

### M8. The "real FL system" contribution is over-claimed relative to what was done.

The abstract, introduction, and title lean heavily on deployment. The title promises "**a cross-country deployment**"; the abstract says the system was run "**across two physically separate machines over the public internet**." Two machines — presumably both operated by the authors — is a proof-of-concept, not a cross-country, multi-site clinical deployment, and nothing in the paper establishes that the two machines were in different countries. There is no analysis of the things that make real FL hard: network failure/stragglers, heterogeneous hardware beyond byte-identical init, client dropout, wall-clock/communication cost, or any threat model (the Limitations concede no secure aggregation / DP). Building a stdlib HTTP server + clients is sound engineering but is not, by itself, an ML research contribution, and the "with minimal tooling / minimal dependencies" framing does not distinguish it from existing lightweight FL frameworks in any measured way. Please either (a) scale the demo to ≥3 genuinely independent sites with reported communication/latency/failure behaviour, or (b) substantially downgrade the framing (drop "cross-country" from the title, describe it as a feasibility prototype), and remove "robustness guarantee" (abstract + heading) — a single-OOD-cohort empirical result is not a guarantee.

### M9. Novelty as an ML contribution is thin and should be scoped honestly.

Every method benchmarked (FedAvg, FedProx, MLDG, APFL, Ditto) is off-the-shelf; there is no new algorithm, and the held-in/OOD split and by-patient evaluation, while good practice, are standard in the domain-generalisation literature. For a health-informatics venue an application benchmark can be a legitimate contribution *if* it is rigorous and reproducible — but that raises the bar on M1–M6 rather than lowering it. I would encourage the authors to (a) frame the contribution precisely as "the first rigorous, by-patient, held-in-vs-OOD federated benchmark on these four T1D cohorts + a deployment prototype," and (b) make the benchmark genuinely definitive (LOCO, tuned baselines, persistence, statistics, public code), which is where the real value lies. As currently written the ML novelty is oversold in the introduction.

---

## 3. Minor concerns

1. **Global normalisation and possible OOD leakage.** CGM is normalised with "a single *global* mean and standard deviation ($154.04 \pm 61.00$)." Was this statistic computed over the four training cohorts only, or over all five (including ReplaceBG)? If ReplaceBG contributed to the global mean/std, information from the OOD cohort has leaked into preprocessing and the "never seen during training" claim is weakened. State this explicitly. Also note the choice may disadvantage the *local* baselines (which might perform better under their own per-cohort normalisation), so it is not a neutral design decision; a per-client-norm local baseline would make that comparison fair.

2. **Seed set is irregular and runs are missing where it matters.** Seeds are 42, 43, 44, **46, 47** — 45 is skipped with no explanation (a silently dropped seed can bias results). The missing OOD runs are for FedAvg and FedProx (seed 46) and one T1D-UOM seed — i.e. exactly in the cells feeding the close held-in/OOD comparisons. Please explain the skipped seed, complete the missing runs, and confirm n per cell in the table itself.

3. **Patient counts disagree with source datasets.** The manuscript's own margin note flags HUPA-UCM 22 (vs 25) and T1D-UOM 14 (vs 17). State the filtering criterion explicitly rather than leaving it as a TODO.

4. **60-minute horizon omitted despite being available.** The intro motivates "30–60 minutes," but only 30-min is reported; `REPORT.md` says full-60-min MSE was already computed and gives the same winners. Report the 60-min RMSE — it is presumably a table export away and its omission looks selective.

5. **Decoder inputs under-described.** `REPORT.md` notes the decoder "is fed only a learned start token; the encoder carries all of the history," i.e. a single-shot (non-autoregressive) decoder. The manuscript does not say this. State whether decoding is autoregressive or single-shot and how the time-of-day mark enters the decoder, if at all.

6. **Bolus variant reconciliation.** Given that the one detailed results file is the bolus run, please make explicit which artifact underlies each table, and either integrate the bolus sensitivity check properly (with ≥3 complete seeds — `REPORT.md` notes only 2) or clearly mark it preliminary in the paper as well.

7. **ARISES anomaly unexplained.** `REPORT.md` concedes no explanation for ARISES being the only cohort where local beats FL held-in. The paper should at least discuss the confound (ARISES is both smallest and highest-glucose), since it is the same cohort driving the OOD collapse narrative.

8. **Code availability.** "Code ... is available from the authors" does not meet PLOS's availability expectations, and the author note admits a repository/DOI is still to be added. A public, versioned repository with seeds, configs, and the exact aggregation of Table 1 is needed for this benchmark to be useful.

9. **Compute/architecture justification.** No ablation supports $d_{\text{model}}=128$, 6 encoder / 2 decoder layers, $d_{\text{ff}}=2048$ (4.9 M params) for a 72→12 CGM task. A short capacity sweep, or at least a citation-backed justification, would help — especially given M4.

---

## 4. Concrete suggestions

1. **Reconcile every number in Tables 1–2 to a single, named, CGM-only run** and fix the single-ARISES OOD figure everywhere it appears (M1). Add an n-per-cell column.
2. **Run leave-one-cohort-out** (4 additional OOD folds) and report OOD RMSE per held-out cohort; this is the highest-value addition and would convert "single-cohort anecdote" into an actual generalisation result (M5).
3. **Fix/verify APFL's α update and sweep FedProx µ and MLDG's inner-lr**; re-run so every method is tuned before any ranking is stated (M2).
4. **Add persistence + a simple LSTM baseline** to every cell of Table 1, held-in and OOD (M4).
5. **Add paired significance tests** across seeds and rewrite ranking claims to match what is significant; the likely honest headline is "federation ≈ local held-in, uniformly better OOD; strategies indistinguishable" (M6).
6. **Give the full MLDG update equations**, clarify whether the second-order term is truly computed and what happens to Adam's moment buffers in the inner step, and consider a cross-client meta-split to match the evaluated shift (M3).
7. **Redo finetuning with a data-fraction sweep on the new site and a fully specified from-scratch comparator**, with tests (M7).
8. **Downgrade the deployment framing**: remove "cross-country" from the title unless the two machines were in different countries, describe the system as a feasibility prototype, and remove "robustness guarantee" (M8). If possible, run ≥3 independent sites and report communication/failure behaviour.
9. **State the normalisation scope** (train-only vs all-five) and add a per-client-norm local baseline for fairness (Minor 1).
10. **Release a public repository** with configs and seeds, and report the 60-min horizon you already have (Minor 4, 8).

I would be glad to review a revised version. The by-patient, held-in-vs-OOD framing is the right one, and with a definitive benchmark (tuned baselines, LOCO, persistence, statistics, reproducible numbers) and honest scoping of the system, this could become a genuinely useful reference for federated CGM forecasting.
