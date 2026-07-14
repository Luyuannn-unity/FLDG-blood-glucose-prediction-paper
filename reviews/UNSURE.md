# Open questions / things I'm unsure about

> **UPDATE (after you pointed me to `output_arises_bolus/cgm`):** items #1, #2, #3 below
> are now **RESOLVED**. I aggregated the CGM-only 5-seed outputs and they reproduce
> Table 1 essentially exactly, including the ARISES collapse **28.51 ± 6.85** (verified).
> The directory also contains **two extra OOD cohorts (BrisT1D, Flair)** and TIR/time-lag
> columns, which I have now incorporated (see `iter3_revisions.md`). One tiny residual:
> the Local-OOD-mean on ReplaceBG computes to ~23.45–23.74 depending on how missing
> single-model seeds are averaged, vs the table's 23.54 — a <0.1 mg/dL bookkeeping
> difference, not an error. Persistence and pooled-central baselines are **not** in the
> outputs, so they still can't be produced without a new training run.


Running list of things I could not resolve from the files and need you to confirm.
Grouped by severity. (Reviewer agents may add more; I'll consolidate at the end.)

## A. Data provenance for the main results table (IMPORTANT)

1. **Which experiment backs Table 1 (`tab:main`)?** The manuscript labels Table 1
   as *CGM-only, 5 seeds*. But the only 5-seed results file in the repo
   (`RESULTS_arises_bolus.md`) is the **bolus** variant, and `FLockit_GPFormer/REPORT.md`
   is **CGM-only but only 3 seeds**. The numbers in Table 1 match *neither* file
   exactly (e.g. Table 1 FedAvg HUPA-UCM = 18.64; bolus file = 18.75; 3-seed report
   differs again). **Where do the Table 1 numbers come from?** Is there a CGM-only
   5-seed export I haven't been given? I did **not** change any Table 1 numbers —
   I kept your values as-is.

2. **ARISES single-cohort OOD collapse number.** The text says single_ARISES
   collapses on ReplaceBG at **28.51 ± 6.85**. The bolus file says **26.86 ± 3.45**;
   the 3-seed CGM report says **31.8 ± 5.95**. Three different numbers for the same
   concept. Which is the correct CGM-only 5-seed value? (I left 28.51 ± 6.85 in place.)

3. **Are the finetuning numbers CGM-only or bolus?** The finetuning results
   (fedprox→finetune 20.98, fedavg→finetune 21.04, mldg→finetune 21.04,
   from-scratch 21.38) come from the bottom of `RESULTS_arises_bolus.md`. It's not
   stated whether these are CGM-only or the bolus variant. I wrote them into Results
   and Discussion as if they are consistent with the CGM-only main table — please
   confirm they belong to the same experimental setting as Table 1.

## B. Cohort / dataset details

4. **Patient counts vs source papers.** Table 1 lists HUPA-UCM = 22 patients and
   T1D-UOM = 14, but the dataset papers report 25 (Hidalgo 2024) and ~17 enrolled
   / 21 (Alsuhaymi 2025). REPORT.md implies post-filter subsets
   (HUPA 18/2/2 = 22; T1D-UOM 10/2/2 = 14). Is the difference just your
   post-filtering, and if so what was the filtering criterion? (A reviewer flags this;
   I left the numbers and the existing REVIEW comment in the source.)

5. **ABC4D and ARISES dataset citations.** These two cohorts currently have no
   dataset citation in the manuscript (only HUPA-UCM, T1D-UOM, ReplaceBG do). They
   are Imperial College datasets (ABC4D ≈ NCT02053051; ARISES ≈ NCT03643692). Do you
   have canonical dataset/registry citations you want to use, or should we cite the
   Zhu et al. FCNN paper as the data source?

6. **T1D-UOM vs "T1D-UOM2".** The source files call the cohort `T1D-UOM2`; the
   manuscript uses `T1D-UOM`. Assuming these are the same cohort — confirm.

## C. Manuscript content decisions

7. **Physical deployment locations.** The methods TODO asked to "add details about
   where training takes place physically." I removed the TODO and kept the generic
   "two physically separate machines over the public internet." If you want specific
   sites/cities/institutions named, tell me.

8. **Bolus variant — keep or cut?** You wrote "Not quite sure if I should include
   this. It is somewhat irrelevant?" I kept it as a brief *preliminary secondary
   analysis* (framed as within-seed-noise per REPORT.md). Keep, cut, or expand?

9. **Author / affiliation / corresponding email** are still template placeholders
   ("Name1 Surname", "correspondingauthor@institute.edu"). I did not invent these.

10. **Code/data availability statement** currently says "available from the authors"
    with a placeholder note to add a repo/DOI. Provide the repository link if you
    have one.

11. **60-minute horizon.** Table 1 and the text are 30-min only. In v2 I removed
    the "we report 60-min" claim and kept 60-min as future work. Do you have the
    60-min numbers to add back?

## D. Additional items surfaced by the reviewer agents (iteration 1)

12. **Title / "cross-country".** All three reviewers flagged that a two-machine
    demo is not a "cross-country deployment." In v2 I changed the title to
    "...a cross-site deployment prototype." Confirm, or restore your original title.
    Also: were the two machines actually in different countries? If so, say where.

13. **Exact MLDG update.** Reviewer 2 says "second-order meta-gradient (inner step
    reuses the outer Adam state)" is non-standard and not reproducible as written
    (Is the second-order term actually computed? What is the inner learning rate?
    Does the inner step advance Adam's moment buffers?). In v2 I softened the text
    and pointed to "the released code." Please give me the exact inner/outer update
    (or point me to the code) so we can state it precisely.

14. **APFL frozen-α.** REPORT.md notes APFL's α may be stuck at its 0.25 init
    (α-lr = model lr), which contradicts the "α learning rate 0.1" the draft stated.
    In v2 I removed the "α-lr 0.1" claim and added a caveat that APFL may be
    under-tuned. **Was α actually frozen?** If so, the APFL row is really a fixed
    25/75 mixture, not APFL — we should either re-run or relabel it. Which is it?

15. **Clinical metrics (error grid / MARD / hypo detection).** Reviewer 1 (clinical)
    considers RMSE-only insufficient for a clinical venue and notes every comparator
    reports a Clarke/Parkes grid or MARD. **Do you already have** error-grid / MARD /
    hypo-hyper detection numbers for the main models? If yes, we should add them; if
    no, it's flagged as a limitation + future work in v2.

16. **Persistence / simple baseline.** Reviewer 2 wants a persistence (last-value)
    and/or simple-LSTM baseline in Table 1, per client, held-in and OOD. **Do our
    runs already log a persistence baseline?** If yes, add it; currently flagged as
    a limitation.

17. **Global-normalisation scope.** I wrote in v2 that the global mean/sd
    ($154.04 \pm 61.00$) is computed **from the four training cohorts only** (so no
    OOD leakage). Please confirm this is true (i.e. ReplaceBG did not contribute to
    the normalisation constant).

18. **Leave-one-cohort-out (LOCO).** Both ML and clinical reviewers say this is the
    single highest-value additional experiment (4 extra OOD folds, nearly free) and
    would turn the single-cohort robustness claim into real evidence. **Do you want
    to run LOCO?** If yes, that's a substantive experiment, not a text edit.

19. **Finetuning variant + protocol.** Reviewer 3 confirmed the finetuning numbers
    match the **bolus** file exactly (see item #3). Also: the from-scratch comparator's
    protocol (lr, rounds, which layers finetuned) is unspecified — please provide it,
    and confirm whether finetuning is CGM-only or bolus.

20. **Data availability specifics.** For PLOS: a public code repo/DOI, and per-dataset
    access route / licence / accession (Zenodo/NCT) for all five cohorts, plus an
    IRB/ethics/consent-provenance statement for the secondary use. Provide these.

## E. Items surfaced in iteration 2

21. **Centrally-pooled baseline.** The fresh reviewer notes that comparing federation
    only against single-cohort training conflates "the federated algorithm" with
    "more/more-diverse data." The clean control is a model trained on all four cohorts
    **pooled on one machine**. In v3 I added a limitation stating the mechanism is
    "more diverse data under a privacy constraint." **Do you have (or can you run) a
    pooled-central model?** It's cheap given the code and would strengthen the paper.

22. **"Meta-learned" in the title.** The fresh reviewer points out the title
    foregrounds "meta-learned," yet the paper honestly concludes MLDG shows no
    advantage over FedAvg (within seed noise) and its meta-split targets cross-patient
    rather than cross-cohort shift. Options: (a) keep the title and frame MLDG as a
    clean neutral result, (b) de-emphasise "meta-learned" in the title. Your call —
    I did not change the title beyond "cross-country"→"cross-site prototype" (#12).

23. **Per-single-model OOD numbers.** Reviewers want the four single-cohort models'
    individual OOD RMSEs in the main table (not just the mean 23.54), since the reframe
    hinges on them. I only have the **bolus** per-single values (22.01/21.85/26.86/21.67);
    I did not insert them because Table 1 is CGM-only. Please provide the CGM-only
    per-single OOD numbers and I'll add them (ties to #1–#2).

## F. Reference verification — residual items (three agents web-checked all 43 refs)

Full reports: `refcheck_group_a_clinical_models.md`, `refcheck_group_b_fl_dg.md`,
`refcheck_group_c_datasets_benchmarks.md`. **Good news:** every reference exists, all
method descriptions (FedProx/SCAFFOLD/APFL/Ditto/MLDG/MOON) are faithful, and all four
external RMSE@30 numbers in the comparison table matched the source PDFs exactly. I
applied all confirmed fixes to `references.bib` (completed the 5 placeholder author
lists; corrected the Zhu et al. DOI `.3187033`→`.3187703`; fixed Manchanda number/title,
Kolev number, added issue/pages to several). Remaining things to confirm at submission:

24. **ARISES citation author list.** I added `zhu2022arises` (npj Digital Medicine 2022,
    DOI 10.1038/s41746-022-00626-5, NCT03643692) as the ARISES source. The DOI/trial are
    confirmed but the **full author order was not line-by-line verified** — please confirm.

25. **ABC4D citation.** I cited the trial registry (NCT02053051) as the safe ABC4D source
    because the exact originating journal paper for the n=25 phase-4 cohort couldn't be
    pinned down. If you prefer a journal citation, tell me which Reddy et al. ABC4D paper
    matches the cohort you used.

26. **Deliberate "and others" author truncations** remain in a few long author lists
    (vaswani2017, zhou2021informer, battelino2019, rieke2020, sheller2020), per the bib
    header's plan to expand at submission. Expand these before submitting.

27. **Minor:** `sergazinov2023gluformer` pages field (`1--5`) could be normalised to the
    single ICASSP page number; not urgent.

## G. New items from incorporating the extra OOD cohorts (iteration 3)

28. **BrisT1D and Flair need citations.** I added these two OOD cohorts (from
    `output_arises_bolus/cgm`) to the paper but they currently have **no `\cite`** ---
    I described them as obtained via MetaboNet. Please provide the proper dataset
    citations (BrisT1D is likely the Bristol T1D challenge/dataset; Flair likely the
    FLAIR T1D trial). Until then they read as "via MetaboNet."

29. **Local-OOD mean for BrisT1D/Flair.** In the new OOD table I gave the Local (mean
    of 4 singles) as "≈28.1 / ≈26.8" (and ≈23.5 for ReplaceBG to match Table 1),
    because the exact value shifts <0.3 mg/dL with how missing single-model seeds are
    averaged. If you want exact figures, tell me the averaging convention and I'll set
    them precisely. The single-ARISES collapse values are exact.

30. **Time-lag / TIR metrics interpretation.** I added a short paragraph reporting
    predicted-vs-actual time-in-range agreement (~2-4 pts) and forecast lag (~20 min).
    The ~20-min lag on a 30-min forecast is worth a sanity check from you — it means
    the model leans on recent values. Confirm you're comfortable stating this.

## H. Iteration 4 — new open items (IMPORTANT)

32. **ReplaceBG OOD evaluation subset.** For the new zero-shot comparison table
    (`tab:oodprior`) I need to know exactly which ReplaceBG patients we evaluate on.
    `REPORT.md` lists ReplaceBG as 166/21/21 patients with 984,447 test windows. Since
    we never train on ReplaceBG, is our OOD score computed over **all ~208 patients**, or
    only the **21 test-split patients**? The published comparators (GPFormer, GluLLM)
    evaluate on a **46-subject hold-out**. Either way all our test patients are unseen —
    but I want the sentence in the paper to be exactly right. Please confirm.

33. **Novelty framing vs GPFormer — please read.** GPFormer (Zhu et al., IEEE JBHI 2024)
    already did Transformer + MLDG + zero-shot glucose domain generalisation on
    REPLACE-BG, CGM-only. Our model *is* that architecture. I have rewritten the intro to
    credit it and reposition our contribution as "the same objective, but optimised
    **without pooling**, across institutions." **Please sanity-check that framing** — it
    is the single most important positioning decision in the paper, and if we get it wrong
    a reviewer will read the work as re-doing GPFormer.

34. **Do we want to cite MetaboNet-Bench?** (Jeffries et al., arXiv 2606.18640.) It
    benchmarks all three of our OOD cohorts — but only as a **pooled 13-dataset aggregate**
    with no per-dataset breakdown, and **its training pool includes HUPA-UCM and T1D-UOM**
    (two of our four training cohorts), so it is *not* an independent comparator. I added
    the bib entry but did not cite it. Say the word and I'll add it with that caveat.

35. **GPFormer's reciprocal data point.** GPFormer reports zero-shot RMSE@30 = **22.9 on
    ABC4D** — one of *our training* cohorts (we get 19.68 held-in there). That's a nice
    symmetric comparison (they transfer into our cohort; we transfer into theirs). Want it
    in the paper?

31. **Bolus is now a full rerun, not preliminary.** Given `output_arises_bolus/bolus`
    has all methods/seeds, I upgraded the bolus text from "preliminary 2-seed" to a
    full sensitivity analysis with the synthesis that **bolus damps the single-ARISES
    OOD collapse (mean and variance) but is redundant with federation.** Confirm you
    like this framing (my recommendation: keep it — it's a genuine, coherent micro-finding).
