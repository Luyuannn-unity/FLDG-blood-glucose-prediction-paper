# FLDG — Federated & Meta-Learned Blood-Glucose Forecasting (paper)

LaTeX source for the PLOS Digital Health manuscript:
**"Federated and meta-learned blood-glucose forecasting across sites:
a cross-country deployment and a domain-generalisation benchmark."**

## Files
- `glucose_fl_paper.tex` — manuscript (PLOS template). Introduction (with prior
  work folded in, PLOS house style) is drafted; Abstract, Author summary,
  Materials and methods, Results, Discussion are marked TODO.
- `references.bib` — bibliography. Entries tagged `%% VERIFY` need author/year
  checks before submission.
- `plos2015.bst` — PLOS Vancouver BibTeX style, committed so the bibliography
  builds out of the box.

## Building
Self-contained: BibTeX with `\bibliographystyle{plos2015}` over `references.bib`.
On Overleaf, set `glucose_fl_paper.tex` as the main document and compile with
pdfLaTeX; references resolve with no extra setup.

`plos2015.bst` is the genuine PLOS Vancouver style. The current PLOS template
package ships an identical file renamed `plos2025.bst`; for final submission you
may swap in that exact file from the official template and change the one
`\bibliographystyle{...}` line to match.
