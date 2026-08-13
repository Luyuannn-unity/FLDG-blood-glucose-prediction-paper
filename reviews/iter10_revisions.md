# Iteration 10 — Introduction rewording pass (2026-08-13)

Scope: **Introduction only.** No other section touched. No number changed
anywhere; numbers were only *removed* (from the contribution paragraphs).

## Why this pass happened

Part of the agreed full rewording pass (Results → Discussion → Methods →
Intro → Abstract). The author's diagnosis of the intro: happy with what it
says, but "too many words with nothing in between" — no signposting. Offered
three treatments (plain topic sentences / bolded lead sentences on every
paragraph / subsections); the author picked **plain topic sentences**, with
bold kept only where it already was (the ¶7 gap sentence and the three
contribution leads). Second author decision this pass: **no results in the
Introduction** — result claims stay qualitative there; numbers live in the
abstract and Results.

## Changes

1. **Every paragraph now opens with its point.** Reading first sentences
   alone gives the whole argument. New/changed openers:
   - ¶1: "A reliable forecast of where blood glucose will be in 30--60
     minutes is clinically valuable in type~1 diabetes" (was: T1D
     prevalence stats; the clinical payoff sat at the paragraph's end).
   - ¶2: "Glucose forecasters are now accurate on the cohort they were
     trained on; how well they transfer to cohorts they never saw is the
     open question" (was: history of model families; the transfer turn sat
     two-thirds in). `ghimire2024generalize` moved onto this sentence.
   - ¶4: "Federation removes the need to pool data, but it does not remove
     domain shift."
   - ¶5: "These ideas have reached glucose forecasting only in the
     *centralised* setting."
   - ¶6: "...our benchmark covers two of its method families, meta-learning
     and personalisation" now stated up front; the representation-alignment
     family folded into the closing sentence (all citations kept).
   - ¶8: "A second, more practical gap..." (was "observation"; now parallels
     ¶7's gap).
   - ¶3, ¶7, ¶9–13 already led with their point; light trims only.
2. **Results removed from the contribution paragraphs:**
   - Contribution 1: cut the ReplaceBG zero-shot parity sentence ("sits
     inside the field of models developed *on* ReplaceBG... holds at 30
     minutes and not at 60"). The claim survives in the abstract and
     Results/Discussion.
   - Contribution 2: cut "$0.3$--$0.7$ mg/dL", "$10\%$", and "seventeen
     individuals... two on the smallest". Kept one qualitative clause
     ("finetuning... on a small fraction of a new cohort's own patients
     beats training there from scratch") so the contribution still says
     what is shown — flagged to the author as a judgment call.
   - Contribution 3: cut the initial-weights-broadcast sentence (system
     detail, repeated in Methods). No numbers were in this paragraph.
3. **Small fixes riding along:** ¶3's "The data that improve generalisation
   and the data that exist are thus mismatched: large, heterogeneous corpora
   are what is needed..." tightened to "What is needed is a large,
   heterogeneous corpus; what is available is many small, governed silos."
   ¶1 merged the CGM/TIR sentence into an em-dash aside.

## Validation

- Intro word count 1661 → 1537.
- All `\cite` keys resolve in `references.bib`; no citation dropped
  (checked: the full intro citation set is unchanged).
- Env balance OK (document/table/tabular/figure all matched); no
  labels/refs touched.
- Locked facts respected: GPFormer stays an unnamed citation
  (`zhu2024gpformer`), `sun2025multicontinental` still cited, no numbers
  invented.

Snapshot: `revision/glucose_fl_paper_v25.tex`.
