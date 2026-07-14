# Peer review — *PLOS Digital Health*

**Manuscript:** "Federated and meta-learned blood-glucose forecasting across sites: a domain-generalisation benchmark and a cross-site deployment prototype"

**Reviewer:** Fresh reviewer (first look; did not see the previous version)

---

## 1. Recommendation and summary

**Recommendation: Major revision.**

The paper does two things. First (its stated primary contribution), it benchmarks six training strategies — single-cohort local training, FedAvg, FedProx, MLDG, and two personalised-FL methods (APFL, Ditto) — for 30-minute CGM forecasting with a shared encoder–decoder transformer, using four real adult T1D cohorts as federated clients and a fifth (ReplaceBG) held out as an out-of-distribution (OOD) test. The evaluation is done under a strict by-patient split and reports held-in and OOD error separately. Second, it builds and runs a lightweight from-scratch FL system (stateless HTTP server + per-cohort clients, Python standard library only) end-to-end across two physically separate machines over the internet.

Overall this is a careful, honest, and unusually well-calibrated piece of work. The held-in/OOD separation is a genuinely useful framing, the by-patient split is the right (harder) choice, and the central "federation buys reduced tail risk, not a large accuracy gain" message is refreshingly resistant to over-claiming. The prose is clear and the limitations section is exemplary. My reservations are: (a) one concrete internal inconsistency between the text and Table 2 that recurs twice and distorts the finetuning narrative; (b) a missing baseline (centrally pooled training) that leaves the paper's headline causal claim — that *federation* buys reliable transfer — unproven, since the same benefit is more parsimoniously attributed to *training on four diverse cohorts*; (c) a complete absence of figures, including a system diagram the authors' own note flags as missing; (d) a dangling bolus analysis introduced in Methods but never reported in Results; and (e) — importantly for a revision that has clearly softened its language — several places where the hedging has gone far enough to obscure the real, defensible contribution. The paper is close, but these need addressing before acceptance.

The manuscript also still contains author TODO comments in the source (e.g. the citation-check note at lines 282–286 and the "add a public repository/DOI link... add an FL-architecture figure" note at lines 481–482). It is not yet in submission-ready state.

---

## 2. Major concerns

### 2.1 Internal inconsistency: the "FedProx numerically lowest zero-shot" claim contradicts Table 2

This is the clearest case of a stated conclusion not following from what precedes it. Table 2 (`tab:main`) gives zero-shot OOD RMSE on ReplaceBG as FedAvg 21.43, **FedProx 21.57**, MLDG **21.34** (bold, i.e. lowest). FedProx is therefore the *worst* of the three global strategies OOD, and it also has the *highest* held-in average (20.28 vs FedAvg 20.09, MLDG 19.99). Yet the Discussion states:

> "the three global strategies converge once finetuned (FedProx, numerically lowest zero-shot here, is also numerically best after finetuning)"

FedProx is not numerically lowest zero-shot — it is highest. The same slip appears earlier:

> "FedProx was numerically lowest here but was run at a single untuned $\mu$..."

placed in the paragraph arguing the federated strategies are indistinguishable, where the surrounding text has just (correctly) named MLDG as numerically best held-in and OOD. Both sentences read as leftovers from an earlier data version. This matters beyond a typo: the finetuning narrative is built on it. If FedProx actually went from *worst* zero-shot (21.57) to *best* finetuned (20.98), that is a **reversal**, which undercuts the "the three converge / strategy matters less once local data are available" story rather than supporting it. Please reconcile lines 556 and 634 with Table 2 and re-examine whether the finetuning interpretation still holds.

### 2.2 The central claim attributes to "federation" a benefit that the design cannot separate from "more/more-diverse data"

The paper's headline — repeated in the abstract, Results ("Federation's value here is reduced tail risk"), and Discussion ("Federation buys more reliable transfer") — is that *federation* improves OOD reliability. But the only contrast in the main table is federation (4 cohorts) vs single-cohort local training (1 cohort). These differ in **two** ways at once: the training algorithm *and* the amount/diversity of training data. The obvious missing arm is a **centrally pooled model** trained on all four cohorts on one machine. That is the natural upper bound and the decisive control: if pooled-central ≈ FedAvg on OOD, then the OOD reliability gain is a *data-diversity* effect that federation merely preserves under a privacy constraint (federation's real and sufficient selling point), and the "federation buys transfer" phrasing overstates the mechanism. If FedAvg materially trails pooled-central, that gap is itself an important finding. As written, the paper cannot tell these apart, and several sentences claim more than the design supports. Either add the pooled-central baseline (strongly preferred — it is cheap given the code exists) or reframe the claim throughout as "training across multiple diverse cohorts (which federation enables without pooling raw data) buys reliable transfer."

Relatedly, the entire OOD reliability argument rests on **one** failing model (ARISES-only) evaluated on **one** OOD cohort (ReplaceBG). The paper is admirably explicit about this in Limitation (ii), but the abstract and Discussion still lean on it as the paper's main message. Because ARISES is also the smallest cohort, an equally plausible reading is "do not train a deployable model on a tiny single cohort" rather than "federate." A leave-one-cohort-out design (already named as future work) is really needed to license the current framing; short of that, the reliability claim should be stated as a single illustrative instance, not a general property.

### 2.3 No figures at all — including the system diagram the secondary contribution needs

The manuscript contains three tables and zero figures. For a mixed clinical + ML readership this is a real adequacy problem, and it hits the *secondary* contribution hardest: the FL system — a stateless HTTP server, a train→validate→test client state machine, broadcast of initial weights — is described only in prose. The authors' own source note (lines 481–482) says "add an FL-architecture figure"; it is mandatory, not optional. Beyond that, at least one results figure would carry the argument far better than Table 2 alone: the OOD story is fundamentally about a *distribution* (the ARISES-only model's catastrophic, high-variance transfer vs the tight cluster of the others), and a per-seed dot/box plot of OOD RMSE by strategy would make the "one silent collapse" point visually and immediately, which a table of means cannot. An illustrative predicted-vs-actual CGM trace at the 30-min horizon would also orient clinical readers.

### 2.4 The bolus variant is promised in Methods but never reported

The "Bolus input variant" paragraph (lines 374–383) describes a two-channel model and says the effect is "report[ed] as a delta against the CGM-only model." No such delta appears anywhere in Results or Discussion. This is a dangling promise: a reader is told an experiment was run and how it will be reported, then never sees the number. Either report the delta (even one line: "adding bolus changed RMSE@30 by X mg/dL, within seed noise") or remove the Methods paragraph. As-is it reads as an amputated section.

### 2.5 The "meta-learned" framing in the title/positioning is not supported by the results

The title foregrounds "meta-learned" forecasting, and MLDG is presented as a domain-generalisation method. But the paper then (correctly and honestly) concludes MLDG shows no advantage over FedAvg within seed noise, *and* that its meta-split is over patients within a client, so it "simulates cross-patient shift... not the cross-cohort shift the OOD test measures" (lines 646–648). So the one method the title elevates is both statistically indistinguishable from plain averaging and mis-targeted at the evaluated shift. This is a coherence gap between the promise (title, "meta-learned") and the delivery. I would either de-emphasise "meta-learned" in the title or frame MLDG explicitly as a negative/neutral result ("meta-learning as commonly ported to FL does not help here, and here is the mechanistic reason") — which is itself a legitimate and publishable finding, but a different promise than the current title makes.

---

## 3. Minor concerns and writing

- **Patient-count reconciliation (author's own flagged TODO, lines 282–286).** Table 1 counts (HUPA-UCM 22, T1D-UOM 14) differ from the source dataset papers (25 and 17). These match the post-filtering splits in the internal report, so they are presumably usable subsets — but the manuscript must state the filtering/inclusion criterion explicitly rather than leave it as a code comment.
- **Held-in "avg" is unweighted.** The `avg` column is the mean of four cohort means, but cohorts range from ~126k to ~562k windows (Table 1). State that the average is unweighted, or report a window-weighted figure alongside; readers will otherwise assume it is pooled.
- **Table 3 (`tab:prior`) presentation.** The "sd over" column with entries "patients"/"seeds" is awkward; consider folding this into the caption. External RMSE values carry parenthetical SDs but only the HUPA-UCM row of "Ours" does — make the SD reporting consistent or note why. The caveats in the caption are good.
- **Residual source comments.** Remove the REVIEW/NOTE author comments (lines 282–286, 481–482) before submission; confirm the data/code availability statement (currently "available from the authors," which PLOS will require to be a repository/DOI).
- **Seed set.** "seeds (42, 43, 44, 46, 47; seed 45 was not run)" and the 4-vs-5-seed cells are commendably transparent but slightly distracting in the abstract-adjacent prose; the detail belongs in Methods (where it is) and can be trimmed elsewhere.
- **Very long sentences** in the Introduction (e.g. the GDPR/HIPAA sentence, lines 187–190) — readable but could be split for the clinical audience.
- **"Local ARISES... accurate on its own patients (22.04)"** (line 599): 22.04 is in fact the *worst* held-in cohort for every method. "Accurate on its own patients" is true only relative to its OOD collapse; consider rewording to avoid implying ARISES is easy in-domain.

---

## 4. Is the paper now under-selling itself? (over-hedging note)

Yes — in a few specific places the softening has overshot, and the real contribution gets buried. This is worth correcting because an over-hedged paper reads as one with no result.

1. **The strongest evidence in the paper is under-sold in the "Positioning against prior results" subsection.** Matching published RMSE@30 on all four cohorts *under a strictly harder by-patient split*, and on HUPA-UCM/T1D-UOM *with CGM alone against models that also consume insulin and carbohydrate*, is a genuinely positive result. The paper retreats to: *"We therefore do not claim to beat these numbers — a by-patient result is not expected to — but to match them under an evaluation that better reflects deployment."* Matching prior numbers while handicapped on both split and inputs is arguably *better* than beating them under an easier protocol, and can be stated with more confidence. This is the paper's most defensible headline and it is currently phrased as an apology.

2. **The abstract closes on a near-null note.** *"The gains over local training are small relative to CGM sensor error, so the practical value is reduced deployment risk rather than a large accuracy jump; the federated strategies were statistically indistinguishable from one another."* Every clause here is a concession. Nothing in the abstract states plainly that the paper delivers *a clean, reproducible, by-patient, held-in-vs-OOD benchmark across four real cohorts plus a working cross-machine federation* — which is the actual contribution and is not small. A reader could finish the abstract unsure what was accomplished. Lead with the deliverable, then hedge the effect size.

3. **The deployment prototype is repeatedly demoted to "feasibility prototype."** The phrase "we do not claim a production-grade... deployment" is fine once; it appears in the abstract, intro (twice), Methods, and Discussion. A federation that actually trains FedAvg/FedProx/MLDG across two independent machines over the public internet using only the Python standard library is a concrete, reusable artifact and a rare thing in this literature (the paper itself notes almost all prior work is simulated). Say that plainly and once; the current repetition makes a working system sound like a caveat.

4. **"We therefore do not claim MLDG is the best method"** (line 555) and the surrounding paragraph are correctly cautious — this one is well-calibrated, not over-hedged. I flag it only to contrast: the negative results *are* appropriately stated; it is the *positive* results (the benchmark artifact, the prior-work comparison, the running system) that have been over-softened.

Net: the calibration on effect sizes is good and should stay. The calibration on *what was built and demonstrated* has drifted into self-deprecation and should be dialled back so the contribution survives a first read.

---

*End of review.*
