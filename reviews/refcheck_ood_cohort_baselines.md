# Ref-check: Published forecasting baselines on our three OOD test cohorts

**Purpose.** We evaluate ReplaceBG, BrisT1D and FLAIR as **held-out, out-of-distribution cohorts** (federated training on HUPA-UCM, ABC4D, ARISES, T1D-UOM only; no training on any of the three). This document collects **published** short-horizon forecasting accuracy on those three datasets so we can honestly position our zero-shot numbers against models that were *actually trained on* each dataset.

**Our numbers (RMSE@30, mg/dL):**

| Cohort | MLDG | FedAvg | FedProx |
|---|---|---|---|
| ReplaceBG | 21.34 | 21.43 | 21.57 |
| BrisT1D | 26.31 | 26.37 | 26.51 |
| FLAIR | 25.05 | 25.07 | 25.22 |

**Bottom line up front.**
- **ReplaceBG** has excellent, protocol-matched published baselines. Our zero-shot number sits *inside* the pack of models trained on ReplaceBG. This is a strong, defensible claim.
- **BrisT1D** has **no** usable published RMSE@30 in mg/dL. Every candidate is either a different horizon (Kaggle = 60 min), different units (mmol/L), or normalized-scale RMSE. Do **not** claim a comparison.
- **FLAIR** has **no** published glucose-forecasting baseline at all, per-dataset. Do **not** claim a comparison.

Verification note: all numbers below were read from the primary source (publisher full text, author-accepted manuscript PDF, or arXiv). Search-engine summaries were **not** trusted — several conflated papers and produced numbers I could not reproduce from source. Anything I could not confirm is marked **UNVERIFIED**.

---

## 1. Summary table

| Dataset | Paper | Model | RMSE@30 (mg/dL) | Split | Trained on that dataset? | Comparable to our zero-shot? |
|---|---|---|---|---|---|---|
| **ReplaceBG** | Zhu et al. 2024, IEEE JBHI (**GPFormer**) | GPFormer (Transformer + MLDG) | **19.2 ± 3.8** | **By patient** — 46 hold-out subjects, unseen | **Yes** (developed on REPLACE-BG) | **Yes** — best comparator |
| ReplaceBG | Zhu et al. 2024, IEEE JBHI | N-BEATS | **21.2** | By patient (same 46 hold-out) | Yes | **Yes** |
| ReplaceBG | Zhu et al. 2024, IEEE JBHI | Bi-LSTM | **21.7** | By patient (same 46 hold-out) | Yes | **Yes** |
| ReplaceBG | Zhu et al. 2024, IEEE JBHI | ARIMA | 28.1 | By patient | Yes | Yes |
| ReplaceBG | Zhu et al. 2024, IEEE JBHI | SVR | 37.4 | By patient | Yes | Yes |
| **ReplaceBG** | Zhu, Howson & Nevado-Holgado 2026, EBioMedicine (**GluLLM**) | GluLLM (LLaMA-3.2-1B + adapters) | **20.6 ± 3.5** | **By patient** — 180 dev / 46 hold-out | **Yes** | **Yes** (caveat: uses insulin + EHR features) |
| ReplaceBG | idem | Crossformer | **21.1 ± 3.6** | By patient | Yes | Yes |
| ReplaceBG | idem | TCN | **21.3 ± 3.7** | By patient | Yes | Yes |
| ReplaceBG | idem | N-BEATS | **21.4 ± 3.7** | By patient | Yes | Yes |
| ReplaceBG | idem | GRU | **22.1 ± 3.7** | By patient | Yes | Yes |
| ReplaceBG | Jaloli & Cescon 2023, JDST | CNN-LSTM | 9.28 ± 1.31 (uni) / 9.73 ± 1.34 | "Forward chaining" rolling — **test patients re-enter training** | Yes | **NO — do not cite as a baseline** (15-min grid; leaky protocol; extreme outlier) |
| ReplaceBG | Fang et al. 2026, iScience (MT-HypoNet) | MT-HypoNet | **not reported per-dataset** | Inter-patient 5-fold CV; REPLACE-BG used as *external validation without retraining* | **No** (trained on Loop) | Methodologically relevant, **no usable number** |
| ReplaceBG / BrisT1D / FLAIR | Jeffries et al. 2026, arXiv (**MetaboNet-Bench**) | GluForecast / LSTM / UniTS / LightGBM / Gluformer | **19.95 / 20.06 / 20.44 / 20.84 / 21.97** — **POOLED over 13 datasets** | By patient ("novel patients split", ~10% subjects/dataset) | Yes (pooled) | **Caveat** — pooled, **no per-dataset breakdown** |
| **BrisT1D** | Kaggle *BrisT1D Blood Glucose Prediction Competition* | many | n/a | Train 9 participants (first 3 mo); test 15 participants, **includes unseen participants** | Yes | **NO — 60-min horizon, mmol/L** |
| BrisT1D | Maqsood et al. 2025, FedCSIS | Attention MTL + PPO | RMSE 0.0419 (**normalized**) | Not stated | Yes | **NO — normalized scale** |
| BrisT1D | AutoBiGluNet 2026, Health Inf Sci Syst | Autoformer + BiLSTM | RMSE 0.0674 (**normalized**) | Not stated | Yes | **NO — normalized scale** |
| BrisT1D | GlucoNet-MM 2025, Diabetes Obes Metab | MTL + Decision Transformer | MAE 0.031 (**normalized**); RMSE not given | Not stated | Yes | **NO — normalized scale** |
| BrisT1D | GAT-BiGRU 2026, JAMIA | Temporal GAT + BiGRU | 15.3 mg/dL (**horizon ambiguous**) | **UNVERIFIED** (paywalled) | Yes | **Caveat — UNVERIFIED**, likely not usable |
| **FLAIR** | — | — | **NONE FOUND** | — | — | **No baseline exists** |

---

## 2. Detailed per-paper notes

### 2.1 ReplaceBG

#### (A) GPFormer — Zhu et al., IEEE JBHI 2024 — **THE key comparator**

- **Authors:** Taiyu Zhu, Ioannis Afentakis, Kezhi Li, Ryan Armiger, Neil Hill, Nick Oliver, Pantelis Georgiou
- **Venue:** IEEE Journal of Biomedical and Health Informatics, 2024. **DOI: 10.1109/JBHI.2024.3428921**
- **Open-access AAM:** https://discovery.ucl.ac.uk/id/eprint/10197097/ · PubMed: https://pubmed.ncbi.nlm.nih.gov/39012743/

This is **the direct antecedent of our work** — same MLDG domain-generalization framing, same REPLACE-BG cohort.

> "Leveraging meta-learning for domain generalization, we propose GPFormer, a Transformer-based **zero-shot learning** method designed for multi-horizon glucose prediction. We developed GPFormer on the **REPLACE-BG dataset, comprising 226 participants with T1D**, and proceeded to evaluate its performance using three external clinical datasets with CGM data."

> "we applied **meta-learning for domain generalization (MLDG)**, a model agnostic meta-learning framework, to tackle this more challenging scenario of zero-shot learning."

**Split — BY PATIENT (this is the important part).** Figure 3 is captioned:

> "Multi-horizon glucose prediction performance of GPFormer and the considered baseline method on the **hold-out subjects in the REPLACE-BG dataset**." — axis label: **"Hold-Out Subjects in REPLACE-BG Dataset (n = 46)"**

> "five-fold cross validation ... were introduced to fine-tune hyperparameters, where **the training sets and the validation sets were also partitioned on an individual basis**. Following the model training and validation, we evaluated the GPFormer model on the hold-out [subjects]"

So: **226 subjects → 180 development / 46 hold-out, partitioned by individual.** Test subjects are entirely unseen, but they come from the **same cohort** the model trained on (in-distribution).

**RMSE@30 on REPLACE-BG hold-out (Table II, mg/dL — units confirmed from Fig. 3 axis "RMSE (mg/dL)"):**

| Model | 30 min | 60 min | 90 min | 120 min |
|---|---|---|---|---|
| **GPFormer** | **19.2** | 32.3 | 41.6 | 48.2 |
| N-BEATS | **21.2** | 34.1 | 43.3 | 49.7 |
| Bi-LSTM | **21.7** | 34.7 | 43.7 | 50.0 |
| ARIMA | 28.1 | 45.1 | 80.2 | 98.2 |
| SVR | 37.4 | 50.5 | 60.9 | 69.2 |

> "Notably, over a 30-minute prediction horizon, GPFormer achieved RMSE (mean±SD) of **19.2±3.8, 22.9 ± 3.9, 18.9 ± 3.2, and 15.9 ± 4.0** for the **REPLACE-BG, ABC4D, OhioT1DM, and GVAS** datasets, respectively."

**These are point RMSEs at PH=30, not window averages.** (The paper separately uses an "overall RMSE ... averaging the mean square error for all prediction horizons from 5 minutes to 120 minutes" **only for cross-validation and ablations** — do not confuse the two.)

**Features — CGM only (+ timestamps). Explicitly no insulin/carbs:**

> "**Given that our model does not explicitly use insulin bolus and carbohydrate intake information**, a six-hour window effectively captures the glucose level changes resulting from these events."

Input window = 6 h. REPLACE-BG is 226/226 CSII, mean glucose 159.9 ± 26.4 mg/dL.

**Note for us:** GPFormer's *external* zero-shot RMSE@30 on **ABC4D is 22.9** — and ABC4D is one of our *training* cohorts. Useful reciprocal data point.

#### (B) GluLLM — Zhu, Howson & Nevado-Holgado, EBioMedicine 2026

- **Venue:** EBioMedicine 2026;129:106343. **DOI: 10.1016/j.ebiom.2026.106343**. PMID 42349253. PMC13320499.
- Preprint: medRxiv 2025.07.12.25331188.
- Same senior lead author (Taiyu Zhu) as GPFormer → **same 226-subject REPLACE-BG cohort and same 180/46 by-patient split.**

> "the REPLACE-BG dataset was first divided into a **development set comprising 180 individuals and a hold-out testing set of 46 individuals**."

From the published abstract (verified against Europe PMC):

> "We trained and evaluated GluLLM on the REPLACE-BG dataset, which includes 226 individuals with type 1 diabetes... Compared with **15 state-of-the-art deep learning baselines**... GluLLM (LLaMA 3.2 1B backbone) demonstrated superior performance, with significantly lower **30-min root mean square error** than the strongest baseline (Crossformer) on REPLACE-BG and Móstoles (**20.6 ± 3.5** and 9.6 ± 2.9 mg/dL; p < 0.001)"

**RMSE@30 on REPLACE-BG hold-out (mg/dL), top-5 as published:**

| Model | RMSE@30 |
|---|---|
| **GluLLM** | **20.6 ± 3.5** |
| Crossformer | 21.1 ± 3.6 |
| TCN | 21.3 ± 3.7 |
| N-BEATS | 21.4 ± 3.7 |
| GRU | 22.1 ± 3.7 |

**Features:** CGM (6 h history, 5-min sampling; L=72, τ=12) **+ insulin bolus + demographics/EHR (age, sex, BMI, HbA1c)** — i.e. **richer inputs than ours**. Worth stating: they get 20.6 *with* insulin+EHR and *with* in-cohort training; we get 21.34 with neither.

⚠️ The full 15-baseline table is not reproduced in a single published table; only the top-5 are shown. Treat "15 baselines" as a claim, not an extractable list.

#### (C) Jaloli & Cescon, J Diabetes Sci Technol 2023 — **DO NOT USE AS A BASELINE**

- **Citation:** Jaloli M, Cescon M. *Long-Term Prediction of Blood Glucose Levels in Type 1 Diabetes Using a CNN-LSTM-Based Deep Neural Network.* J Diabetes Sci Technol. 2023;17(6):1590–1601. **DOI: 10.1177/19322968221092785**. PMC10658677.
- Reports **RMSE@30 = 9.28 ± 1.31 mg/dL** (and 9.73 ± 1.34 for the combined CNN-LSTM) on Replace-BG.

**Three reasons this is not comparable — flag explicitly if a reviewer raises it:**

1. **Different sampling grid.** > "the CGM variable was uniformly **resampled every 15 minutes** in both data sets". A 30-min horizon on a 15-min grid is a 2-step-ahead problem; on our (and GPFormer's/GluLLM's) 5-min grid it is 6-step-ahead. **Strictly easier task.**
2. **Leaky split.** > "the model is trained on an 80% subset of patients and forecast for the remaining 20% which are test patients. **Through a rolling basis process, the same forecasted patients are then included as part of the next training data set** and model is tested on a new 20% subset of patients." Test patients from earlier folds re-enter training. This is *not* a clean by-patient hold-out.
3. **Extreme outlier.** 9.3 mg/dL @ 30 min is roughly **half** the RMSE of every other REPLACE-BG result in the literature (19–22 mg/dL), including two papers by the group that curated the cohort. Values in the 9–10 mg/dL range at PH=30 are widely regarded as implausible for free-living CGM. Additionally, min–max normalization was fit over "the entire data set", which can leak test-set range information.

**Recommendation:** cite it only in a sentence noting that reported REPLACE-BG results vary widely because of protocol heterogeneity, and that we align to the GPFormer/GluLLM protocol.

#### (D) Fang et al., iScience 2026 (MT-HypoNet) — methodologically relevant, no usable number

- **Citation:** Fang S, Zhang H, Hu D, et al. *Glucose forecasting and hypoglycemia forewarning in type 1 and type 2 diabetes using deep learning.* iScience. 2026;29(4):115294. **DOI: 10.1016/j.isci.2026.115294**. PMC13019577.
- **Highly relevant framing:** the model was **trained on the Loop Study dataset** and "directly applied ... to the remaining datasets in the retrospective cohort" (which includes REPLACE-BG) **without retraining** — i.e. the *same* zero-shot/external-validation setup we use.
- Split: **inter-patient 5-fold CV** — "a subset of patients as the training group, while the **held-out patients** (test fold) were used for evaluation."
- Features: CGM + optional carbs, basal insulin, bolus insulin, time-of-day.
- ❌ **BUT:** results are aggregated **by diabetes type (T1D vs T2D), not by dataset.** REPLACE-BG appears only in the Table 1 demographics. **No REPLACE-BG-specific RMSE@30.** → **UNVERIFIED / unusable as a numeric baseline**, but excellent as a *citation for the legitimacy of zero-shot cross-cohort evaluation*.

#### (E) MetaboNet-Bench — Jeffries et al., arXiv 2026 — covers all three, but POOLED

- **Citation:** Jeffries N, Wolff MK, Royston S, Healey E, Mayer C, Klonoff D, Snyder M, Wang T. *MetaboNet-Bench: A Multi-modal Benchmark for Glucose Forecasting in Type 1 Diabetes.* arXiv:2606.18640 (v1 17 Jun 2026; v2 25 Jun 2026).
- Companion dataset paper: Wolff MK, Calhoun P, Aiello EM, Qin Y, Royston SF. *MetaboNet: The Largest Publicly Available Consolidated Dataset for Type 1 Diabetes Management.* arXiv:2601.11505.

**This is the only source that touches all three of our cohorts.** Table 3 (verbatim subject counts) includes:

| Dataset | # Subjects |
|---|---|
| ReplaceBG | 208 |
| **Flair** | **113** |
| **BrisT1D** | **19** |
| HUPA-UCM | 22 |
| T1D-UOM | 14 |
| (+ CTR3 303, DCLP3 112, DCLP5 100, IOBP2 332, Loop 845, PEDAP 65, AZT1D 23, Shanghai T1DM 12) | |

**Split — by patient:**
> "First, the split is performed **by patient**, so that roughly **10% of the subjects in each individual dataset are assigned exclusively to the test set**; this split is hereafter referred to as the **novel patients split (Task 1)**."
> Task 2 (known patients): "10% of the subjects from the remaining training set are further divided, with the **time-sorted second half of their data** assigned to the test set."

**RMSE@30 (mg/dL), Task 1 — POOLED ACROSS ALL 13 DATASETS:**

| Model | RMSE@30 |
|---|---|
| GluForecast | 19.95 |
| LSTM | 20.06 |
| UniTS | 20.44 |
| LightGBM | 20.84 |
| Gluformer | 21.97 |

Table caption: > "Model performance with 95% bootstrap confidence intervals (1,000 resamples) and DTS error grid zones for a **30-minute prediction horizon**."

Harmonization: 5-minute reading interval; "We performed linear interpolation up to 30 minutes between valid CGM readings." Modalities: CGM + insulin + carbs.

⚠️ **CRITICAL CAVEATS:**
1. **No per-dataset RMSE breakdown exists anywhere in the paper** (I checked the appendix). You **cannot** extract "MetaboNet-Bench's ReplaceBG number" or "…FLAIR number" or "…BrisT1D number". Pooled ≠ per-dataset, and the pool is dominated by Loop (845) + IOBP2 (332) + CTR3 (303).
2. **Their training pool includes HUPA-UCM and T1D-UOM — two of our four training cohorts.** So MetaboNet-Bench is *not* an independent OOD comparison for us; if anything it overlaps our train set. Mention this if we cite it.
3. Their models see **insulin + carbs**; our zero-shot setup should state its feature set explicitly.

**Usable claim:** "State-of-the-art multimodal models trained *in-distribution* on a 13-dataset pool that includes ReplaceBG, FLAIR and BrisT1D achieve ~20–22 mg/dL RMSE@30 on novel patients (Jeffries et al. 2026)." That is a fair, hedged framing.

### 2.2 BrisT1D

#### Dataset of record
- **Paper:** James SG, Armstrong MEG, O'Kane AA, Emerson H, Abdallah ZS. *BrisT1D Dataset: Young Adults with Type 1 Diabetes in the UK using Smartwatches.* arXiv:2507.17757 (2025).
- **Data DOI:** 10.5523/bris.33z5jc8fa6tob21ptrugzqog08 (BrisT1D-Open); restricted portion at 10.5523/bris.yonrplcb4bvi2vhhn2ehtmpey.
- 24 young adults, UK, 6-month longitudinal study; CGM + insulin pump + smartwatch.
- **The dataset paper reports NO forecasting benchmark results.** It is a descriptor paper only.

#### Kaggle "BrisT1D Blood Glucose Prediction Competition" — **NOT COMPARABLE**

- URL: https://www.kaggle.com/competitions/brist1d
- **Horizon = 60 minutes, not 30.** Official evaluation text: > "Submissions are evaluated on **Root Mean Square Error (RMSE)** between the predicted blood glucose levels **an hour into the future** and the actual values that were then collected."
- **Units = mmol/L** (UK dataset). A leaderboard RMSE is therefore in mmol/L. (For scale: 2.0 mmol/L × 18.018 = 36.0 mg/dL; 2.5 mmol/L = 45.0 mg/dL.)
- **Split (from the competition data description, mirrored verbatim in participant repos):** > "The training set takes samples from the **first three months of study data from nine of the participants**" … "The testing set takes samples from the remainder of the study period from **fifteen of the participants (so unseen participants appear in the testing set)**."
  → A **hybrid** split: partly temporal, partly by-patient; the test set mixes seen and unseen participants.
- **1st place:** "Sebastian Cuya — 1st Place Solution: Single LGBM model." **The exact leaderboard RMSE could not be retrieved** (Kaggle serves a JS-only shell; both WebFetch and curl return the SPA skeleton). → **UNVERIFIED.**

**Verdict: the Kaggle task is a 60-min-horizon, mmol/L problem on a bespoke windowed CSV. It is apples-to-oranges against our RMSE@30 in mg/dL. Do not compare.**

#### Published papers using BrisT1D — all non-comparable or unverifiable

| Paper | Reported | Problem |
|---|---|---|
| Maqsood S, Belousovienė E, Maskeliūnas R. *Attention-Based Multi-Task Learning and PPO Reinforcement Learning for Explainable Blood Glucose Prediction.* FedCSIS 2025, Annals CSIS vol. 43. DOI 10.15439/2025F2640 | RMSE **0.0419**, MAE 0.0310 | **Normalized scale.** 0.0419 is impossible in mg/dL or mmol/L. Horizon and split not stated. **Non-comparable.** |
| *AutoBiGluNet: transformer-based time series modeling…* Health Inf Sci Syst 2026. DOI 10.1007/s13755-026-00469-4 | BrisT1D RMSE **0.0674 ± 0.0006**; OhioT1DM RMSE 0.88 @30 min | **Normalized scale** (an OhioT1DM RMSE of 0.88 is not mg/dL). **Non-comparable.** |
| *GlucoNet-MM…* Diabetes Obes Metab 2025. DOI 10.1111/dom.70147 | BrisT1D R²=0.94, MAE **0.031** | **Normalized scale**; RMSE not reported. **Non-comparable.** |
| *GAT-BiGRU: explainable multi-task temporal graph learning…* JAMIA 2026. DOI 10.1093/jamia/ocag104 | BrisT1D **RMSE 15.3 mg/dL**, MAE 9.36 mg/dL | Units *are* mg/dL. **BUT:** the paper predicts "at **30 and 60 minute** horizons" and the abstract does **not** say which horizon 15.3 refers to; the **train/test split is not stated in the abstract** and the full text is paywalled. Also unclear whether they used BrisT1D-Open or the Kaggle CSV. **UNVERIFIED — do not cite as a baseline.** |

**Net: there is no trustworthy published RMSE@30 (mg/dL, clean protocol) on BrisT1D.** Our 26.31 is, as far as I can establish, **the first reported zero-shot RMSE@30 on this cohort** — but we must not claim to beat anything.

### 2.3 FLAIR

- **Trial of record:** Bergenstal RM, Nimri R, Beck RW, et al. *A comparison of two hybrid closed-loop systems in adolescents and young adults with type 1 diabetes (FLAIR): a multicentre, randomised, crossover trial.* Lancet. 2021;397(10270):208–219. DOI: 10.1016/S0140-6736(20)32514-9. PMID 33453783.
- **Data:** JAEB, https://public.jaeb.org/dataset/566. Per MetaboNet: **113 participants**, mean age 19.3 ± 4.2 y, 61.9% female, **Guardian 3 CGM**, 12-week periods.
- **Searches run:** Europe PMC (`"FLAIR" AND "glucose prediction"` → 3 hits, all irrelevant — FLAIR MRI sequences; `"FLAIR study" AND CGM AND forecasting` → **0 hits**), arXiv, Google Scholar, Semantic Scholar, papers-with-code.

**Result: ZERO published glucose-forecasting papers report a FLAIR-specific RMSE.** The *only* work that forecasts on FLAIR at all is **MetaboNet-Bench**, and it pools FLAIR into a 13-dataset aggregate with **no per-dataset breakdown**.

⚠️ Additional caveat specific to FLAIR: it is a **hybrid closed-loop (AID) crossover trial** (MiniMed 670G 3.0 vs 4.0). Automated insulin delivery actively regulates glucose, which **compresses glycemic variability** and generally makes forecasting *easier* than in open-loop cohorts. Also note FLAIR is an **adolescent/young-adult** cohort (mean age 19) with a **Guardian 3** sensor, whereas REPLACE-BG is adults (mean age 44) on Dexcom G4. Any cross-cohort claim should acknowledge this.

---

## 3. How our zero-shot numbers compare — honest verdict

### ReplaceBG — **STRONG, CLAIMABLE RESULT** ✅

Line up our zero-shot MLDG (21.34) against models **trained on REPLACE-BG** and tested on **unseen REPLACE-BG patients** (the same by-patient hold-out design, n=46):

| Model | RMSE@30 (mg/dL) | Trained on REPLACE-BG? | Features |
|---|---|---|---|
| GPFormer (Zhu 2024) | **19.2** | ✅ yes | CGM + timestamps |
| GluLLM (Zhu 2026) | **20.6** | ✅ yes | CGM + insulin + EHR |
| Crossformer (Zhu 2026) | 21.1 | ✅ yes | CGM + insulin + EHR |
| N-BEATS (Zhu 2024) | 21.2 | ✅ yes | CGM |
| TCN (Zhu 2026) | 21.3 | ✅ yes | CGM + insulin + EHR |
| **Ours — MLDG (zero-shot)** | **21.34** | ❌ **NO** | (state ours) |
| N-BEATS (Zhu 2026) | 21.4 | ✅ yes | CGM + insulin + EHR |
| **Ours — FedAvg (zero-shot)** | **21.43** | ❌ **NO** | |
| **Ours — FedProx (zero-shot)** | **21.57** | ❌ **NO** | |
| Bi-LSTM (Zhu 2024) | 21.7 | ✅ yes | CGM |
| GRU (Zhu 2026) | 22.1 | ✅ yes | CGM + insulin + EHR |
| ARIMA (Zhu 2024) | 28.1 | ✅ yes | CGM |
| SVR (Zhu 2024) | 37.4 | ✅ yes | CGM |

**Verdict: this is a genuinely strong result and worth stating prominently.** Our zero-shot MLDG (21.34) lands **inside the pack of models that trained on REPLACE-BG** — it beats Bi-LSTM (21.7), GRU (22.1), ARIMA and SVR, and is statistically indistinguishable from N-BEATS (21.2/21.4) and TCN (21.3). It trails only GPFormer (19.2, −2.1 mg/dL) and GluLLM (20.6, −0.7 mg/dL), both of which **trained on the cohort** and, in GluLLM's case, additionally used **insulin dosing and EHR features we do not use**.

**Suggested phrasing (defensible):**
> "Without ever training on REPLACE-BG, our federated MLDG model attains 21.34 mg/dL RMSE at a 30-minute horizon — within 0.7–2.1 mg/dL of models developed directly on that cohort under an identical unseen-patient hold-out protocol (GluLLM 20.6, GPFormer 19.2), and better than several in-distribution deep baselines (Bi-LSTM 21.7, GRU 22.1)."

**Three things to check before publishing that claim:**
1. **Is our 21.34 a point RMSE at PH=30, or a window average over 5–120 min?** GPFormer reports *both*; its Table II value (19.2) is a point RMSE at PH=30, while its ablations use a 5–120-min average. If ours is a window average, **the comparison is invalid.** Confirm.
2. **Sampling grid.** GPFormer/GluLLM/MetaboNet-Bench all use a **5-minute** grid. Confirm ours matches (a 15-min grid, as in Jaloli & Cescon, makes the task much easier).
3. **Test-subject composition.** GPFormer/GluLLM evaluate on **46 hold-out subjects**; we presumably evaluate on **all** REPLACE-BG subjects (every one is unseen to us). Not a fatal difference — arguably ours is the harder/fairer setting — but **say so explicitly** rather than implying identical test sets.

### BrisT1D — **NO COMPARISON POSSIBLE** ⚠️

There is **no** published RMSE@30 in mg/dL on BrisT1D with a verifiable protocol. Everything on offer fails at least one of: wrong horizon (Kaggle = 60 min), wrong units (mmol/L, or normalized 0–1 scale), or unknown split (JAMIA GAT-BiGRU).

**Verdict:** report our 26.31 as a **novel zero-shot result on an unbenchmarked cohort**. Do **not** write "competitive with prior work" — there is no prior work to be competitive with. The most we can honestly say:

> "To our knowledge no prior work reports 30-minute-horizon RMSE in mg/dL on BrisT1D; the associated Kaggle competition targets a 60-minute horizon in mmol/L and is therefore not directly comparable. We report 26.31 mg/dL as a zero-shot reference point."

Optionally add a soft anchor: MetaboNet-Bench (which *does* train on BrisT1D, pooled) reaches ~20–22 mg/dL RMSE@30 *pooled across 13 datasets* — but be explicit that this is **not** a BrisT1D-specific number.

### FLAIR — **NO COMPARISON POSSIBLE** ⚠️

Zero published forecasting baselines. Same treatment as BrisT1D.

> "We are not aware of any published glucose-forecasting benchmark on the FLAIR cohort; we report 25.05 mg/dL as a zero-shot reference point."

⚠️ And add the AID caveat: FLAIR is a **hybrid closed-loop** cohort, so its glycemic variability is suppressed relative to open-loop cohorts — reviewers may (fairly) point out that a lower RMSE here is partly a property of the cohort, not the model. Note it before they do.

### Overall honest framing

The **ReplaceBG** result carries the argument. It is the one cohort where a protocol-matched, in-distribution baseline exists, and our zero-shot number is genuinely in-family with it. **BrisT1D and FLAIR should be presented as new, unbenchmarked OOD evaluations** — valuable as evidence of consistent cross-cohort behaviour (25–26 mg/dL on two cohorts never seen in training), **not** as head-to-head wins. Resist the temptation to frame them as beating anything.

---

## 4. NOT FOUND / UNVERIFIED

| Item | Status |
|---|---|
| Any FLAIR-specific published RMSE at any horizon | ❌ **NOT FOUND.** Europe PMC, arXiv, Semantic Scholar, Google all negative. FLAIR appears in forecasting work *only* inside MetaboNet-Bench's pooled aggregate. |
| Any BrisT1D RMSE@30 in mg/dL with a stated split | ❌ **NOT FOUND** (GAT-BiGRU's 15.3 mg/dL is the sole mg/dL figure but its horizon and split are unstated/paywalled → **UNVERIFIED**). |
| Kaggle BrisT1D leaderboard top RMSE (public/private) | ❌ **UNVERIFIED.** Kaggle serves a JS-only shell; WebFetch and curl both return the SPA skeleton with no scores. The 1st-place writeup ("Sebastian Cuya — Single LGBM model") exists but its score could not be read. *Would need a logged-in browser or the Kaggle API.* |
| Per-dataset RMSE breakdown in MetaboNet-Bench | ❌ **CONFIRMED ABSENT** — I checked the appendix; only pooled metrics are published. |
| REPLACE-BG-specific RMSE in Fang et al. (iScience 2026) | ❌ **CONFIRMED ABSENT** — results reported by diabetes type, not by dataset. |
| Full 15-baseline table in GluLLM | ⚠️ **PARTIAL** — only the top-5 baselines appear in the published table. |
| GPFormer's exact per-model SDs for baselines | ⚠️ **PARTIAL** — Table II gives point RMSEs for baselines; SDs are given in prose for GPFormer only (19.2 ± 3.8). |
| "Meta-transfer learning, RMSE 15.16 mg/dL on REPLACE-BG" (Biomed Signal Process Control, S1746809425009796) | ❌ **UNVERIFIED** — surfaced only in a search-engine summary; ScienceDirect returns 403 and I could not confirm the number, the dataset, or the split from any primary source. **Do not cite this number.** |
| "BrisT1D RMSE 8.5–9.8 mg/dL (risk-sensitive RL)" | ❌ **LIKELY A SEARCH-ENGINE HALLUCINATION** — surfaced in one summary, attributable to no real paper I could locate. **Do not cite.** |
| GlucoBench (arXiv 2410.05780) | ✅ Checked — contains **Colas, Dubosson, Hall, Broll, Weinstock** only. **None of our three datasets.** Not relevant. |
| "From Prediction to Practice" (arXiv 2605.00645) | ✅ Checked — **DCLP3, DCLP5, PEDAP + UVA/Padova simulator**. **None of our three.** Uses patient-level splits (70/10/20); useful only as a protocol citation. |
| Ghimire et al., PLOS One 2024 (cross-dataset generalization) | ✅ Real, but uses **OhioT1DM, DCLP3, DCLP5, RT** — **not REPLACE-BG**. Useful as a *supporting citation* that cross-dataset generalization degrades performance, not as a baseline. |

---

## 5. BibTeX

```bibtex
@article{zhu2024gpformer,
  author  = {Zhu, Taiyu and Afentakis, Ioannis and Li, Kezhi and Armiger, Ryan and
             Hill, Neil and Oliver, Nick and Georgiou, Pantelis},
  title   = {Multi-Horizon Glucose Prediction Across Populations With Deep Domain Generalization},
  journal = {IEEE Journal of Biomedical and Health Informatics},
  year    = {2024},
  doi     = {10.1109/JBHI.2024.3428921},
  note    = {GPFormer; developed on REPLACE-BG (n=226), evaluated on 46 hold-out subjects}
}

@article{zhu2026glullm,
  author  = {Zhu, Taiyu and Howson, Joanna and Nevado-Holgado, Alejo},
  title   = {Empowering digital health management with on-device large language models
             for glucose prediction: a model development and validation study},
  journal = {EBioMedicine},
  volume  = {129},
  pages   = {106343},
  year    = {2026},
  doi     = {10.1016/j.ebiom.2026.106343},
  pmid    = {42349253}
}

@article{jeffries2026metabonetbench,
  author  = {Jeffries, Nathaniel and Wolff, Miriam K. and Royston, Sam and Healey, Elizabeth and
             Mayer, Caleb and Klonoff, David and Snyder, Michael and Wang, Tao},
  title   = {{MetaboNet-Bench}: A Multi-modal Benchmark for Glucose Forecasting in Type 1 Diabetes},
  journal = {arXiv preprint arXiv:2606.18640},
  year    = {2026},
  eprint  = {2606.18640},
  archivePrefix = {arXiv}
}

@article{wolff2026metabonet,
  author  = {Wolff, Miriam K. and Calhoun, Peter and Aiello, Eleonora Maria and
             Qin, Yao and Royston, Sam F.},
  title   = {{MetaboNet}: The Largest Publicly Available Consolidated Dataset for
             Type 1 Diabetes Management},
  journal = {arXiv preprint arXiv:2601.11505},
  year    = {2026},
  eprint  = {2601.11505},
  archivePrefix = {arXiv}
}

@article{aleppo2017replacebg,
  author  = {Aleppo, Grazia and Ruedy, Katrina J. and Riddlesworth, Tonya D. and others},
  title   = {{REPLACE-BG}: A Randomized Trial Comparing Continuous Glucose Monitoring
             With and Without Routine Blood Glucose Monitoring in Adults With Well-Controlled
             Type 1 Diabetes},
  journal = {Diabetes Care},
  volume  = {40},
  number  = {4},
  pages   = {538--545},
  year    = {2017},
  doi     = {10.2337/dc16-2482}
}

@article{james2025brist1d,
  author  = {James, Sam Gordon and Armstrong, Miranda Elaine Glynis and
             O'Kane, Aisling Ann and Emerson, Harry and Abdallah, Zahraa S.},
  title   = {{BrisT1D} Dataset: Young Adults with Type 1 Diabetes in the {UK} using Smartwatches},
  journal = {arXiv preprint arXiv:2507.17757},
  year    = {2025},
  eprint  = {2507.17757},
  archivePrefix = {arXiv}
}

@misc{james2025brist1ddata,
  author       = {James, Sam Gordon},
  title        = {{BrisT1D}-Open Dataset},
  year         = {2025},
  publisher    = {University of Bristol},
  doi          = {10.5523/bris.33z5jc8fa6tob21ptrugzqog08}
}

@misc{kaggle2024brist1d,
  title        = {{BrisT1D} Blood Glucose Prediction Competition},
  author       = {{University of Bristol}},
  year         = {2024},
  howpublished = {\url{https://www.kaggle.com/competitions/brist1d}},
  note         = {Target: blood glucose one hour ahead, in mmol/L; evaluated by RMSE}
}

@article{bergenstal2021flair,
  author  = {Bergenstal, Richard M. and Nimri, Revital and Beck, Roy W. and others},
  title   = {A comparison of two hybrid closed-loop systems in adolescents and young adults
             with type 1 diabetes ({FLAIR}): a multicentre, randomised, crossover trial},
  journal = {The Lancet},
  volume  = {397},
  number  = {10270},
  pages   = {208--219},
  year    = {2021},
  doi     = {10.1016/S0140-6736(20)32514-9},
  pmid    = {33453783}
}

@misc{jaeb2021flairdata,
  title        = {{FLAIR} Public Study Dataset},
  author       = {{Jaeb Center for Health Research}},
  year         = {2021},
  howpublished = {\url{https://public.jaeb.org/dataset/566}}
}

@article{fang2026mthyponet,
  author  = {Fang, S. and Zhang, H. and Hu, D. and others},
  title   = {Glucose forecasting and hypoglycemia forewarning in type 1 and type 2 diabetes
             using deep learning},
  journal = {iScience},
  volume  = {29},
  number  = {4},
  pages   = {115294},
  year    = {2026},
  doi     = {10.1016/j.isci.2026.115294}
}

@article{jaloli2023cnnlstm,
  author  = {Jaloli, Mehrad and Cescon, Marzia},
  title   = {Long-Term Prediction of Blood Glucose Levels in Type 1 Diabetes Using a
             {CNN-LSTM}-Based Deep Neural Network},
  journal = {Journal of Diabetes Science and Technology},
  volume  = {17},
  number  = {6},
  pages   = {1590--1601},
  year    = {2023},
  doi     = {10.1177/19322968221092785},
  note    = {Reports RMSE@30 = 9.28 mg/dL on Replace-BG; NOT protocol-comparable
             (15-min resampling; rolling split re-admits test patients to training)}
}

@article{ghimire2024generalize,
  author  = {Ghimire, Sarala and Celik, Turgay and Gerdes, Martin and Omlin, Christian W.},
  title   = {Deep learning for blood glucose level prediction: How well do models generalize
             across different data sets?},
  journal = {PLOS ONE},
  volume  = {19},
  number  = {9},
  pages   = {e0310801},
  year    = {2024},
  doi     = {10.1371/journal.pone.0310801},
  note    = {Cross-dataset generalization evidence; does NOT use REPLACE-BG}
}

@inproceedings{maqsood2025brist1d,
  author    = {Maqsood, Sarmad and Belousovien{\.e}, Egl{\.e} and Maskeli{\=u}nas, Rytis},
  title     = {Attention-Based Multi-Task Learning and {PPO} Reinforcement Learning for
               Explainable Blood Glucose Prediction},
  booktitle = {Proceedings of the 20th Conference on Computer Science and Intelligence Systems
               (FedCSIS)},
  series    = {Annals of Computer Science and Information Systems},
  volume    = {43},
  year      = {2025},
  doi       = {10.15439/2025F2640},
  note      = {Uses BrisT1D; reports RMSE 0.0419 on a normalized scale -- NOT comparable in mg/dL}
}
```

**Recommended to actually cite:** `zhu2024gpformer` (essential), `zhu2026glullm` (essential), `jeffries2026metabonetbench` + `wolff2026metabonet` (for BrisT1D/FLAIR context), `aleppo2017replacebg`, `james2025brist1d` + `james2025brist1ddata`, `bergenstal2021flair` + `jaeb2021flairdata`, `kaggle2024brist1d` (to explain why it is not comparable), `fang2026mthyponet` (precedent for zero-shot external validation), `ghimire2024generalize` (precedent that cross-dataset transfer degrades). Cite `jaloli2023cnnlstm` **only** with the non-comparability caveat.
