# iter13 — Paul/Ken comment round (2026-09-03 → 2026-09-09)

Sources: `Comments/Paul Comment.txt` and `Comments/Ken Comment.pdf`. Ken's 8
comments are PDF popup annotations; extract them with pypdf (`/Contents` of
each `/Text` annotation).

## Paul

1. **Table 1 covers all seven cohorts.** Done just before this round (commit
   023a884).
2. **"Federated strategies and baselines" reorganised.** Opening sentence names
   the two baselines. Entries renamed **Local baseline** and **Centralised
   baseline**. A sentence introduces the three global-model strategies, then
   separate FedAvg / FedProx / MLDG entries (the old joint "FedAvg / FedProx"
   paragraph was split). A sentence introduces the two local-model-only
   strategies, then APFL / Ditto entries. "centralised reference" and "pooled
   model" renamed everywhere (results text, three table group headers, two
   captions, Discussion).
3. **MLDG's only ref was the DG paper.** A 17-agent web search found no prior
   use of plain MLDG inside FL. Closest: FedDG (CVPR 2021) — MLDG-style
   episodes inside clients, but meta-test data synthesised from cross-client
   amplitude spectra, on imaging. GPFormer is the same MLDG-over-patients
   objective but centralised. Author chose a bare cite: `liu2021feddg` on
   "adapted to the federated setting". A fuller positioning passage was
   drafted, then reverted on request.

## Ken (all 8 addressed)

1. Abstract ReplaceBG sentence now gives the comparison: ahead of FedAvg
   (21.48) and the mean single-cohort model (21.73).
2. The unclear "10 to 17 patients sufficed" is spelled out: 10% of the
   training patients (17 for ReplaceBG, 10 for Flair) still beat from-scratch
   training.
3. The live-federation sentence moved to the abstract's first paragraph.
4. Patient-days added to the abstract: ~5,400 (clients) and ~63,000 (OOD).
   This clears Ken's 2,000 patient-day npj Digital Medicine bar 34×. Venue
   decision still open.
5. Author block filled (see below).
6. Table 1 gained a patient-days column.
7. Table 1 also gained train/val/test patient counts (from
   `release_bundle/extracted/dataset_from_scratch/metabonet_splits/manifest.json`),
   CGM device, and age median (IQR). Role stays in the group headers. Table
   wrapped in `\resizebox`. Devices/ages verified against primary sources:
   ABC4D = Dexcom G5, age 36 (29–46) (Zhu et al. IEEE TBME 2022; GluGAN IEEE
   JBHI 2023, new bib key `zhu2023glugan`); ARISES = Dexcom G6, age 40 (30–50)
   (npj Digit Med 5:78). The later ABC4D G6 crossover trial (Unsworth 2023) is
   a different study.
8. Fig 1 client boxes show patient-days (876 / 3,093 / 533 / 876). Regenerate
   with `revision/figures/fl_system_fig.py`.

## Patient-days (new numbers)

Definition: real (non-interpolated) CGM samples × 5 min, from
`release_bundle/datasets[_clean]/<cohort>/segments_packed.npy` (cgm_real =
feature 6). HUPA-UCM 876, ABC4D 3,093, ARISES 533, T1D-UOM 876; ReplaceBG
44,891, BrisT1D 2,706, Flair 15,289. Stated in the abstract, Datasets prose,
Table 1, and Fig 1.

MetaboNet's "7.7 patient-years" for T1D-UOM counts empty grid rows: their
release holds 808,328 T1D-UOM rows (= 7.7 y) but only 266,481 with a CGM value
(= 925 days). The source study is 17 participants × 3 months, so 7.7 y is
impossible as wear time. Our 876 = 925 minus segmentation/cleaning.

## Author block (final, 2026-09-09)

Qi¹ (UCL IHI), Taylor¹, Rui Sun² (Newcastle Computing), Taiyu Zhu³ (KCL
Biostatistics & Health Informatics — his confirmation 2026-09-09; Oxford and
NIHR Maudsley removed), Jiahao Sun⁴ (FLock.io, London — matches
arXiv:2410.17933), Georgiou⁵ (Imperial Bio-Inspired Technology), Harper⁶
(Manchester), Kezhi Li¹*. Jiahao Sun and Georgiou were added by the author on
Overleaf.

## Deployment site correction (2026-09-09)

Taiyu's client ran on KCL's CREATE server, not Oxford's. Site lists in the
Introduction, Methods, Discussion, and Fig 1 now read UCL, Manchester,
Newcastle, KCL.

## Abstract

Rewritten for Ken 1–4, then trimmed twice to stay under 300 words (276 on
2026-09-09). One semicolon removed per the no-semicolons style rule.

## Verification

Each batch of edits went through adversarial multi-agent checks: structure vs
the comment text, terminology sweeps, number consistency (abstract ↔ Datasets
prose ↔ Table 1 ↔ Fig 1 ↔ Results), LaTeX integrity, and web verification of
the FedDG / ABC4D / ARISES claims against primary sources.
