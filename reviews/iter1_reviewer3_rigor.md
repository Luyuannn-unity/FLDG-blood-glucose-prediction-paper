# Reviewer 3 report — statistical rigor, experimental design, reproducibility

**Manuscript:** *Federated and meta-learned blood-glucose forecasting across sites: a domain-generalisation benchmark and a cross-country deployment*
**Venue:** PLOS Digital Health
**Reviewer focus:** numeric consistency between text/tables and the underlying results, statistical treatment, internal consistency, and honesty of the external comparison.

---

## 1. Recommendation

**Major revision.**

The study is well-motivated, the writing is clear, and the framing of the two evaluation regimes (held-in vs OOD) is genuinely useful. The external-comparison subsection is, to its credit, unusually honest about the by-patient vs by-time distinction and does not claim to beat prior work. However, as the reviewer responsible for checking that the numbers are real, I cannot currently trace the paper's central results table to any source data I was given. The manuscript states that Table `tab:main` is the **CGM-only, 5-seed** model, but the only 5-seed source file provided is the **bolus** variant (`RESULTS_arises_bolus.md`), whose per-cohort numbers differ from the table by 0.05–0.15 mg/dL almost everywhere, and the only CGM-only source (`REPORT.md`) is **3 seeds** and reports different, approximate values. Two of the paper's most rhetorically load-bearing numbers — the ARISES OOD collapse (`28.51 ± 6.85`) and the local-baseline OOD mean (`23.54`) — appear in **neither** source file; they match each other internally but cannot be verified against any provided data. The finetuning numbers, by contrast, match the bolus file exactly, which raises a separate concern about whether the Results section mixes variants. None of these problems is necessarily fatal — they may reflect a CGM-only 5-seed export that simply was not shared with me — but as submitted, the primary results are not reproducible from the materials at hand, and the "MLDG is best" claim is not statistically defensible at the reported margins. These must be resolved before acceptance.

---

## 2. Major concerns

**M1. The main results table cannot be traced to any provided source.**
Table `tab:main` is captioned "CGM-only RMSE ... Mean over 5 random seeds." The only 5-seed file (`RESULTS_arises_bolus.md`) is the **bolus** variant. Comparing them cell-by-cell, the table is *close to but systematically different from* the bolus numbers:

- MLDG held-in: table `18.46 / 19.68 / 22.30 / 19.53`; bolus `18.46 / 19.76 / 22.39 / 19.58`. Only HUPA-UCM matches; ABC4D/ARISES/T1D-UOM differ by 0.05–0.09.
- FedAvg held-in: table `18.64 / 19.80 / 22.38 / 19.53`; bolus `18.75 / 19.84 / 22.44 / 19.58`. All four differ.
- FedProx held-in: table `18.89 / 19.94 / 22.60 / 19.67`; bolus `18.95 / 19.95 / 22.75 / 19.80`. All four differ.
- Local (single-cohort) held-in: table `18.81 / 19.95 / 22.04 / 19.80`; bolus singles `18.86 / 19.94 / 21.94 / 19.94`. All four differ.

`REPORT.md` is CGM-only but only 3 seeds (42/43/44) and gives figure-level approximations (FedAvg OOD `21.5 ± 0.1`, local OOD average `24.2 ± 1.6`, single-ARISES OOD `31.8 ± 5.95`), not the precise table values. **Net effect: the entire CGM-only 5-seed table is untraceable to the materials provided.** The values are plausible and internally coherent (see M4), so I suspect a CGM-only 5-seed results file exists but was not supplied. Please provide that file (per-seed CSVs or the aggregated table it was built from) so every cell can be verified, and confirm the seed set used.

**M2. Two headline numbers appear in no source file.**
- The ARISES OOD collapse is quoted three times as **`28.51 ± 6.85`** (abstract-adjacent Results and Discussion). The bolus file gives single-ARISES OOD `26.86 ± 3.45`; `REPORT.md` gives `31.8 ± 5.95`. The manuscript value matches **neither**, and the SD `6.85` is larger than both sources' SDs.
- The local-baseline OOD mean is **`23.54`**. The mean of the four bolus singles on ReplaceBG is `23.10`; the CGM 3-seed report says `24.2`. Again, `23.54` matches neither.

These two numbers carry the paper's central "robustness" message ("transfers catastrophically ... collapsed on ReplaceBG"). They must be sourced to a specific results file. (They are internally consistent with each other — see M4 — but internal consistency is not verification.)

**M3. "MLDG is the strongest global strategy" is not statistically defensible at the stated margins.**
The paper's second headline claim rests on margins that are within seed noise:
- Held-in average: MLDG `19.99` vs FedAvg `20.09` vs Ditto(μ=1.0) `20.09` — a `0.10` mg/dL gap against per-cohort seed SDs of `~0.08–0.24`.
- OOD: MLDG `21.34` vs FedAvg `21.43` — a `0.09` gap; the bolus-file OOD SDs are `±0.12` for both.

With five seeds, no significance test, and overlapping error bars, "MLDG is best OOD" and "best held-in" are not supported beyond "numerically lowest." The manuscript *does* hedge this in Limitations ("suggestive rather than definitive"), which is good, but the Results and Discussion state it far more strongly ("MLDG is the strongest global strategy," "best both held-in and OOD," "the best-supported default"). Please align the strength of the claim across sections, and add at least a paired test across seeds (or bootstrap CIs) if the ranking is to be asserted.

**M4. OOD ranking mixes different seed counts (unequal footing).**
Per `RESULTS_arises_bolus.md`, FedAvg and FedProx OOD are **n=4** (seed_46's `best_model_ood_test_irt.csv` is missing), while MLDG OOD is **n=5**. The paper's central OOD head-to-head — MLDG `21.34` vs FedAvg `21.43` — therefore compares a 5-seed mean against a 4-seed mean. Similarly `single_T1D-UOM2` is n=4 (seed_47 absent). The manuscript acknowledges the missing seeds exist, but does not acknowledge that the OOD comparison it draws its main conclusion from is computed over **different seed sets**. Either impute/rerun the missing seed, or restrict the OOD comparison to the common seed subset, and state per-cell `n` in the table.

**M5. Seed SD is being used where patient/deployment uncertainty is what matters.**
All reported uncertainties (`± 0.04` to `± 0.44`) are **across seeds**, i.e. they quantify optimisation stochasticity for a fixed patient split, not variability across patients. The external baselines report SD **across patients** (`± 2.6` to `± 4.8`). The manuscript correctly labels this in the `tab:prior` caption, but the tiny seed SDs should not be read — and in `tab:main` risk being read — as evidence the models are precise on new patients. A single fixed test-patient split means the point estimates themselves have unquantified patient-sampling uncertainty. Please add a sentence making explicit that seed SD understates real deployment uncertainty, and ideally report patient-level dispersion (e.g. per-patient RMSE distribution) for at least the main model.

**M6. Possible variant mismatch between the main table and the finetuning result.**
The finetuning numbers in the text — FedProx→finetune `20.98 ± 0.06`, FedAvg→finetune `21.04 ± 0.04`, MLDG→finetune `21.04 ± 0.07`, from-scratch `21.38 ± 0.09` — match `RESULTS_arises_bolus.md` **exactly**. But that file is the **bolus** variant, whereas the Results section presents these numbers as a continuation of the CGM-only story. If the finetuning experiment was run on the bolus pipeline while the main table is CGM-only, the Results section silently mixes two model variants. Please confirm which variant the finetuning result comes from and label it accordingly; if it is bolus, either rerun CGM-only or state the variant explicitly.

---

## 3. Numeric-consistency findings

Manuscript value vs the value in the provided source files. "Bolus" = `RESULTS_arises_bolus.md` (5-seed, bolus variant); "REPORT" = `FLockit_GPFormer/REPORT.md` (3-seed, CGM-only); "Summary" = `paper_summary.txt`.

| # | Manuscript claim | MS value | Source value | Verdict |
|---|---|---|---|---|
| 1 | MLDG held-in HUPA-UCM | 18.46 | bolus 18.46 | matches (coincidental — CGM-only source not provided) |
| 2 | MLDG held-in ABC4D | 19.68 | bolus 19.76 | mismatch (no CGM-only source) |
| 3 | MLDG held-in ARISES | 22.30 | bolus 22.39 | mismatch |
| 4 | MLDG held-in T1D-UOM | 19.53 | bolus 19.58 | mismatch |
| 5 | MLDG OOD ReplaceBG | 21.34 | bolus 21.34 | matches (coincidental) |
| 6 | FedAvg held-in (4 clients) | 18.64/19.80/22.38/19.53 | bolus 18.75/19.84/22.44/19.58 | mismatch (all four) |
| 7 | FedAvg OOD | 21.43 | bolus 21.48 (n=4); REPORT 21.5±0.1 | mismatch |
| 8 | FedProx held-in (4 clients) | 18.89/19.94/22.60/19.67 | bolus 18.95/19.95/22.75/19.80 | mismatch (all four) |
| 9 | FedProx OOD | 21.57 | bolus 21.71 (n=4) | mismatch |
| 10 | Local held-in (4 cohorts) | 18.81/19.95/22.04/19.80 | bolus singles 18.86/19.94/21.94/19.94 | mismatch (all four) |
| 11 | Local OOD mean | 23.54 | bolus singles mean 23.10; REPORT 24.2 | **untraceable** (matches neither) |
| 12 | ARISES-only OOD collapse | 28.51 ± 6.85 | bolus 26.86 ± 3.45; REPORT 31.8 ± 5.95 | **untraceable** (matches neither) |
| 13 | Local baseline OOD SD | 1.65 | REPORT 1.6 (CGM 3-seed) | approx / untraceable (paired with a mean, 23.54, from a different basis) |
| 14 | Ditto μ=0.01 ARISES | 21.98 | bolus 22.03 | mismatch |
| 15 | APFL / APFL-dec / Ditto held-in rows | see table | bolus rows differ 0.02–0.20 | mismatch (systematic, no CGM-only source) |
| 16 | FedProx→finetune | 20.98 ± 0.06 | bolus 20.98 ± 0.06 | **matches** (but bolus variant — see M6) |
| 17 | FedAvg→finetune | 21.04 ± 0.04 | bolus 21.04 ± 0.04 | matches (bolus variant) |
| 18 | MLDG→finetune | 21.04 ± 0.07 | bolus 21.04 ± 0.07 | matches (bolus variant) |
| 19 | ReplaceBG-from-scratch | 21.38 ± 0.09 | bolus 21.38 ± 0.09 | matches (bolus variant) |
| 20 | Held-in avg (Local 20.15) | 20.15 | mean(18.81,19.95,22.04,19.80)=20.15 | internally consistent |
| 21 | Held-in avg (FedAvg 20.09) | 20.09 | mean=20.088 | internally consistent |
| 22 | Held-in avg (FedProx 20.28) | 20.28 | mean=20.275 | internally consistent |
| 23 | Held-in avg (MLDG 19.99) | 19.99 | mean=19.993 | internally consistent |
| 24 | Held-in avg (APFL/APFLdec/Ditto×3) | 20.28/20.37/20.11/20.19/20.09 | means=20.283/20.368/20.105/20.193/20.090 | all internally consistent |
| 25 | 23.54 vs 28.51 self-consistency | — | mean(22.0,21.9,28.51,21.7)≈23.51 | internally consistent with each other (still untraceable to a file) |
| 26 | Dataset windows HUPA-UCM | 291,728 | REPORT 244,630+4,708+42,390=291,728 | matches |
| 27 | Dataset windows ABC4D/ARISES/T1D-UOM | 562,043/126,248/300,796 | REPORT splits sum to same | matches |
| 28 | Patient counts 22/25/12/14 | 22/25/12/14 | REPORT (18+2+2)/(19+3+3)/(8+2+2)/(10+2+2) | matches REPORT (differs from dataset papers — noted in-text) |
| 29 | External GlucoFM HUPA/T1D-UOM | 16.71(4.82)/20.81(4.26) | Summary identical | matches |
| 30 | External Zhu ARISES/ABC4D | 20.23(3.38)/20.25(2.60) | Summary identical | matches |
| 31 | Abstract: FedAvg 21.4 / MLDG 21.3 / single 23.5 / held-in ≈20 | rounded | consistent with tab:main | matches (as rounding) |

**Bottom line of the table:** every *internal* arithmetic check passes (held-in averages, window sums, patient counts) and every *external* baseline number is correctly transcribed. What fails is *external verifiability of the paper's own primary results*: the whole CGM-only 5-seed block (rows 2–15) cannot be reconciled with any provided file, and rows 11–12 are the two numbers doing the most rhetorical work.

---

## 4. Minor concerns

1. **`sd 1.65` provenance (row 13).** The Results and Discussion pair the local OOD mean `23.54` with an across-seed SD of `1.65`. The only nearby source value is REPORT's `24.2 ± 1.6` (CGM, 3 seeds). Pairing a mean that matches no file with an SD that appears to come from the 3-seed run looks like a splice of two runs. Please confirm both come from the same CGM-only 5-seed export.

2. **Cohort naming.** The source calls the fourth client `T1D-UOM2`; the manuscript uses `T1D-UOM`. Confirm these are the same cohort and standardise.

3. **Bold in `tab:prior` is misleading.** Bold conventionally marks the best value in a column; here "Ours (MLDG)" is bolded even though the external by-time numbers are *lower* (nominally better). The caption explains the numbers are not head-to-head, but bolding the worse-looking values invites misreading. Consider un-bolding or adding an explicit "not directly comparable" glyph.

4. **`tab:main` does not report OOD SDs or per-cell n.** Given M3–M4, the OOD column should carry `± SD` and an `n` per cell so readers can judge the MLDG-vs-FedAvg margin themselves.

5. **60-minute horizon deferred.** A `% TODO` in the source and the Limitations both defer the 60-min horizon. For a "clinically actionable" framing this is a real gap; at minimum state why 30-min alone suffices for the deployment argument.

6. **Global normalisation statistic `154.04 ± 61.00` mg/dL** is not present in any provided file. Minor, but include the script/manifest that produces it for reproducibility.

7. **Single-seed test-patient split.** With only one by-patient split, the point estimates depend on which patients happened to land in each cohort's test group (especially ARISES, 2 test patients per REPORT). Cross-validated splits (or at least reporting per-patient RMSE) would strengthen the generalisation claim considerably.

8. **Bolus variant is described but its results are not in the paper**, yet the finetuning numbers appear to come from it (M6). Either surface the bolus sensitivity results properly or keep the finetuning experiment CGM-only.

---

*Assessment of external-comparison honesty:* Good. The by-patient vs by-time distinction is stated plainly, the claim is explicitly "match, not beat," the SD-type difference (patients vs seeds) is flagged in the caption, and non-comparable papers (AEGIS 15-min/mmol/L, Kolev synthetic, Manchanda window-averaged, Tan & McBeth MARD-only) are correctly excluded with reasons that match `paper_summary.txt`. This section is the most rigorous part of the manuscript and should be preserved.
