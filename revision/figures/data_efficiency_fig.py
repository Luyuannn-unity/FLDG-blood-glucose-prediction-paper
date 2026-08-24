# Data-efficiency figure for the PLOS paper (fig:dataeff).
# Source: clean-retrain follow-up runs (E10 + E8), 5 seeds (42-46), RMSE@30 on
# each target cohort's held-out test patients.
# Output: paper/revision/figures/data_efficiency.pdf (+ .png preview).
import csv
import statistics as st
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

FU = Path(r"C:/Users/luyua/Desktop/release_bundle/output_clean_retrain/pod_results/followup")
OUT = Path(__file__).resolve().parent
SEEDS = [42, 43, 44, 45, 46]
TARGETS = [("ReplaceBG", 166), ("Flair", 91), ("BrisT1D", 15)]
FRACS = [10, 20, 30, 50, 70]

BLUE = "#2a78d6"
BLUE_FILL = "#cde2fb"
GREY = "#52514e"
GREY_FILL = "#e6e5e2"


def irt(job, seed, target):
    p = FU / job / f"seed_{seed}" / "best_model_local_test_irt.csv"
    for r in csv.DictReader(open(p)):
        if r["client"].startswith(target):
            return float(r["rmse_mgdl_30min"])
    raise KeyError(f"{target} not in {p}")


def ms(v):
    return st.mean(v), st.stdev(v)


fig, axes = plt.subplots(1, 3, figsize=(7.0, 2.75))
for ax, (tg, n) in zip(axes, TARGETS):
    scratch = [irt(f"single_{tg}", s, tg) for s in SEEDS]
    sm, ssd = ms(scratch)
    xs = FRACS + [100]
    ys, es = [], []
    for f in FRACS:
        m, sd = ms([irt(f"mldg_frac{f}_{tg}", s, tg) for s in SEEDS])
        ys.append(m)
        es.append(sd)
    m, sd = ms([irt(f"mldg_ft_{tg}", s, tg) for s in SEEDS])
    ys.append(m)
    es.append(sd)

    ax.axhspan(sm - ssd, sm + ssd, color=GREY_FILL, lw=0, zorder=0)
    ax.axhline(sm, color=GREY, ls="--", lw=1.3, zorder=1,
               label="train from scratch (100% local data)")
    ax.fill_between(xs, ys, [sm] * len(xs), where=[y < sm for y in ys],
                    color=BLUE_FILL, alpha=0.6, lw=0, interpolate=True, zorder=1)
    ax.errorbar(xs, ys, yerr=es, color=BLUE, marker="o", ms=4, lw=1.5,
                capsize=2.5, zorder=3, label="FL pre-train \u2192 fine-tune (MLDG)")
    ax.set_title(f"{tg}  (n={n} patients)", fontsize=9)
    ax.set_xticks(xs)
    ax.set_xticklabels([str(x) for x in xs], fontsize=8)
    ax.tick_params(axis="y", labelsize=8)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    print(f"{tg}: scratch {sm:.2f}+/-{ssd:.2f}; ft " +
          ", ".join(f"{x}%={y:.2f}" for x, y in zip(xs, ys)))

axes[0].set_ylabel("RMSE @ 30 min (mg/dL)", fontsize=9)
fig.supxlabel("target patients used for fine-tuning (%)", fontsize=9, y=0.02)
handles, labels = axes[0].get_legend_handles_labels()
fig.legend(handles[::-1], labels[::-1], loc="upper center", ncol=2, frameon=False,
           fontsize=8.5, bbox_to_anchor=(0.5, 1.02))
fig.tight_layout(rect=(0, 0.04, 1, 0.92))
fig.savefig(OUT / "data_efficiency.pdf")
fig.savefig(OUT / "data_efficiency.png", dpi=200)
print("wrote", OUT / "data_efficiency.pdf")
