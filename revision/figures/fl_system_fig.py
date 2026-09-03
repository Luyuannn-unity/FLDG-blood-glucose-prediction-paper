# FL system schematic for the PLOS paper (fig:system).
# Output: paper/revision/figures/fl_system.pdf (+ .png preview).
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# palette (dataviz skill reference, light mode)
BLUE = "#2a78d6"      # global-weights flow (down)
BLUE_100 = "#cde2fb"  # client box fill
ORANGE = "#eb6834"    # client-updates flow (up)
NEUTRAL = "#f0efec"   # server box fill
INK = "#0b0b0b"
INK2 = "#52514e"
MUTED = "#898781"
EDGE_N = "#52514e"

W, H = 5.25, 3.35
fig = plt.figure(figsize=(W, H))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")

def rbox(x, y, w, h, fc, ec, lw=1.0, ls="solid", r=0.06):
    p = FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
                       facecolor=fc, edgecolor=ec, linewidth=lw, linestyle=ls)
    ax.add_patch(p)
    return p

# ---------------- internet band (drawn first, arrows go on top)
band_y0, band_y1 = 1.78, 2.42
rbox(0.06, band_y0, W - 0.12, band_y1 - band_y0, "#f9f9f7", MUTED, lw=0.8, ls=(0, (4, 3)))
ax.text(W - 0.14, (band_y0 + band_y1) / 2, "public internet\nplain HTTP",
        ha="right", va="center", fontsize=6.8, style="italic", color=MUTED)

# ---------------- server box
sx0, sx1 = 1.35, 3.90
sy0, sy1 = 2.55, 3.28
rbox(sx0, sy0, sx1 - sx0, sy1 - sy0, NEUTRAL, EDGE_N, lw=1.1)
scx = (sx0 + sx1) / 2
ax.text(scx, sy1 - 0.13, "Aggregation server", ha="center", va="center",
        fontsize=8, fontweight="bold", color=INK)
ax.text(scx, sy1 - 0.335, "hosted at one of the four sites\nholds global weights only \u2014 never sees raw CGM data",
        ha="center", va="center", fontsize=6.6, color=INK2, linespacing=1.25)
ax.text(scx, sy0 + 0.115, "\u2463 FedAvg aggregation \u2192 next-round global weights",
        ha="center", va="center", fontsize=6.8, color=INK)

# round-loop note, right of server
ax.text(4.02, sy1 - 0.10, "\u27f2 repeat \u2264 25 rounds", ha="left", va="center",
        fontsize=6.8, color=INK2)
ax.text(4.02, sy1 - 0.26, "early stopping on\navg validation MSE", ha="left", va="top",
        fontsize=6.4, color=MUTED, linespacing=1.25)

# ---------------- client boxes
cohorts = [("HUPA-UCM", 22, 876), ("ABC4D", 25, 3093), ("ARISES", 12, 533), ("T1D-UOM", 14, 876)]
bw, gap, x0 = 1.16, 0.13, 0.09
cy0, cy1 = 0.66, 1.58
centers = []
for i, (name, n, pdays) in enumerate(cohorts):
    bx = x0 + i * (bw + gap)
    cx = bx + bw / 2
    centers.append(cx)
    rbox(bx, cy0, bw, cy1 - cy0, BLUE_100, BLUE, lw=1.1)
    ax.text(cx, cy1 - 0.13, f"Client {i+1}", ha="center", va="center",
            fontsize=6.6, color=INK2)
    ax.text(cx, cy1 - 0.30, name, ha="center", va="center",
            fontsize=8, fontweight="bold", color=INK)
    ax.text(cx, cy1 - 0.46, f"{n} patients", ha="center", va="center",
            fontsize=6.4, color=INK2)
    ax.text(cx, cy1 - 0.61, f"{pdays:,} patient-days", ha="center", va="center",
            fontsize=6.4, color=INK2)
    ax.text(cx, cy0 + 0.14, "\u2461 local training\n(1 epoch per round)", ha="center", va="center",
            fontsize=6.4, color=INK, linespacing=1.2)

# ---------------- arrows: server <-> clients (slanted pairs)
anchors = [1.55, 2.25, 2.95, 3.65]  # points along the server's bottom edge
for cx, sxa in zip(centers, anchors):
    ax.add_patch(FancyArrowPatch((sxa - 0.07, sy0), (cx - 0.14, cy1),
                 arrowstyle="-|>", mutation_scale=8, linewidth=1.3,
                 color=BLUE, shrinkA=1, shrinkB=1))
    ax.add_patch(FancyArrowPatch((cx + 0.14, cy1), (sxa + 0.07, sy0),
                 arrowstyle="-|>", mutation_scale=8, linewidth=1.3,
                 color=ORANGE, shrinkA=1, shrinkB=1))

# flow labels (darker steps of the arrow hues, for print contrast)
ax.text(0.08, 2.52, "\u2460 global weights", ha="left", va="center",
        fontsize=7, color="#1c5cab", fontweight="bold")
ax.text(W - 0.10, 2.48, "\u2462 updated weights", ha="right", va="center",
        fontsize=7, color="#d95926", fontweight="bold")

# ---------------- footer
ax.text(W / 2, 0.44, "Four UK institutions \u2014 UCL, Manchester, Newcastle, Oxford \u2014 one client each.",
        ha="center", va="center", fontsize=6.8, color=INK2)
ax.text(W / 2, 0.26, "Raw CGM data never leaves its institution; FedProx and MLDG change only step \u2461.",
        ha="center", va="center", fontsize=6.8, color=INK2)

import os
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fl_system")
fig.savefig(out + ".pdf")
fig.savefig(out + ".png", dpi=200)
print("done")

