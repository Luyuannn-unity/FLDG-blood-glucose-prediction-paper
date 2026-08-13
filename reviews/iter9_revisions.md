# Iteration 9 — value-case pass (2026-08-13)

Scope: Abstract, Author summary, Results, Discussion. **Materials and methods
untouched** (a concurrent session owns it). No number changed except two
corrections traced to disk.

## Why this pass happened

The author asked: "do we make the case for the value of our paper? would people
read it and go, so you didn't do better than local training, what's the point?"

A five-reader audit (hostile ML reviewer, clinician, skim-only reader, steelman,
structural editor) plus synthesis answered: **partly — and the abstract produced
that exact reaction.** The skim-only reader, given only title/abstract/author
summary/first table/figure, concluded federation does NOT help and said so
unprompted.

Diagnosis: the value case existed but sat below the fold.
- The abstract named only local training as comparator (matching it is not a
  result) and never mentioned the pooled centralised reference at all — first
  mention was Methods L470.
- The abstract's own deflation sentence landed at word ~236 of 425, before the
  reader met the finetuning result or the four-university deployment.
- The two strongest claims (pooling parity; ReplaceBG zero-shot parity) were at
  Results para 5/7 and Discussion para 9/12 respectively, the latter ~87%
  through the body and absent from Results entirely.

## Changes

1. **Abstract rewritten, 425 -> 299 words** (now meets the PLOS 300 cap).
   Leads with federation vs the *pooled* model (19.99 vs 19.90 = 0.09 mg/dL);
   applies the CGM sensor-error yardstick to that gap (under 1% of 12-14
   mg/dL); replaces "beat the mean single-cohort model" with the variance
   framing; adds ReplaceBG zero-shot (21.34); states onboarding in patient
   counts (9-17); hedge moved to the end. Drops "consortium".
2. **Author summary, 280 -> 200 words.** Adds the pooled comparison and the
   onboarding result ("as few as nine patients"), which START_HERE calls the
   headline practical result but which was missing here. No longer ends on a
   caveat.
3. **Results — variance framing + symmetric yardstick.** The mean-of-four
   comparator is dragged up by the ARISES collapse and reads as rigged. tab:ood
   in fact shows the T1D-UOM model beating every federated model AND the pooled
   model on BrisT1D and Flair. Now stated plainly, with the honest and stronger
   point: in-domain accuracy gave no warning (ARISES-only 22.04 vs MLDG 22.30).
   Sensor yardstick, previously used only to shrink our own gain, now also
   applied to the 0.09 mg/dL pooling gap.
4. **Dropped "one cannot know in advance which site's model will fail"** (3
   places). Contradicted by our own caption naming ARISES as the smallest
   cohort; a reviewer would note that a rule against training on 12 patients is
   cheaper than a federation.
5. **New Results paragraph** carrying ReplaceBG zero-shot parity forward.
6. **Concessions stated once.** Significance hedge appeared 6x, sensor-error
   deflation 5x. Both survive in full in Results and Limitations (i)/(iii).
   "On meta-learning" compressed 138 -> 92 words.
7. **Two numeric errors fixed, both traced to disk.** Ditto(mu=0.01) on ARISES
   was 21.98 in the Discussion vs 21.95 in tab:main; raw CSVs give
   21.9474 +- 0.2342, so 21.95 is right. tab:prior reported MLDG on HUPA-UCM as
   18.46 (0.15) — 0.15 is the Local row's sd; MLDG's is 0.28.
8. **tab:finetune cross-reference fixed.** The "even the pooled model transfers
   worse than from-scratch" claim cited a table with no centralised row (they
   are in tab:ood), and the "no amount of other cohorts' data substitutes"
   generalisation is contradicted by MLDG's own 21.34 vs 21.38 on ReplaceBG.

## Still open

- **Uncited novelty claims.** The paper asserts 3x that federated glucose work
  is "almost all simulated" and claims to be first from a real multi-institution
  run, but references.bib has ZERO federated-glucose entries — 55 entries with
  no overlap between the federated ones and the glucose ones. A citation search
  was running when this pass closed; results pending. If no prior real
  multi-site federated glucose study exists the claim stands but needs
  citations for the "almost all simulated" half; if one does exist, claim (c)
  must be narrowed.
- **Deployment reports no deployment-only datum.** FedAvg over HTTP yields the
  same weights as FedAvg in a for-loop, so nothing in Results distinguishes the
  live run from a simulation. Server logs would give wall-clock, bytes/round,
  straggler gap, retried rounds — cheap and would make contribution 3 checkable.
- **No persistence baseline** (author decision, START_HERE). Survivable for the
  *relative* pooling-parity claim; not survivable for any absolute-accuracy
  claim. The abstract as rewritten makes only the relative claim.
- **BrisT1D "just 2 patients"** beats from-scratch on the mean (26.07 vs 26.25)
  but the 0.185 margin sits inside the from-scratch seed band (+-0.33).
  ReplaceBG (17) and Flair (9) clear their noise cleanly, so the abstract says
  9-17 and the 2-patient figure stays in the Discussion with its caveat.
- Snapshot: `revision/glucose_fl_paper_v22.tex`.
