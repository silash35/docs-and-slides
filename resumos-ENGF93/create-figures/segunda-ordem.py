import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
from scipy import signal

# ── Definição do sistema de segunda ordem ──────────────────────────────────
# G(s) = wn² / (s² + 2·ζ·wn·s + wn²)
wn = 1.2  # frequência natural (rad/s)
zeta = 0.2  # fator de amortecimento (sub-amortecido → overshoot)

num = [wn**2]
den = [1, 2 * zeta * wn, wn**2]

sys = signal.TransferFunction(num, den)

# ── Simulação da resposta ao degrau ────────────────────────────────────────
t = np.linspace(0, 20, 4000)
t_out, y_out = signal.step(sys, T=t)

# ── Cálculo das métricas de desempenho ────────────────────────────────────
yss = 1.0  # valor em regime permanente (degrau unitário)

# td – tempo de atraso (resposta atinge 50 % de yss)
idx_td = np.argmax(y_out >= 0.5 * yss)
td = t_out[idx_td]

# tr – tempo de subida (10 % → 90 %)
idx_tr = np.argmax(y_out >= yss)  # primeira passagem por yss
tr = t_out[idx_tr]

# tp – tempo de pico
idx_tp = np.argmax(y_out)
tp = t_out[idx_tp]
Mp_abs = y_out[idx_tp]  # valor absoluto do pico
Mp = (Mp_abs - yss) / yss * 100  # sobressinal em %

# ts – tempo de assentamento (critério de ±5 %)
tol = 0.05
settled = np.where(np.abs(y_out - yss) > tol * yss)[0]
idx_ts = settled[-1] + 1 if len(settled) else len(t_out) - 1
ts = t_out[idx_ts]

# ── Figura ─────────────────────────────────────────────────────────────────
plt.rcParams.update({"font.size": 20})
fig, ax = plt.subplots(layout="constrained", dpi=300)

ax.plot(t_out, y_out, color="red", linewidth=2.8)

# Linha de regime permanente (tracejada preta)
ax.axhline(yss, color="black", linestyle="--", linewidth=1.2)

# ── Anotação: Mp (seta verde dupla) ───────────────────────────────────────
ax.annotate(
    "",
    xy=(tp, Mp_abs),
    xytext=(tp, yss),
    arrowprops=dict(arrowstyle="<->", color="green", lw=2),
)
ax.text(tp + 0.15, (Mp_abs + yss) / 2, "$M_p$", color="green", va="center")

# ── Anotação: td (linha azul tracejada + rótulo) ──────────────────────────
# ax.plot([td, td], [0, 0.5 * yss], color="blue", linestyle="--", linewidth=1.4)
# ax.plot(
#     [0, td], [0.5 * yss, 0.5 * yss], color="blue", linestyle="--", linewidth=1.4
# )
# ax.text(
#     td,
#     -0.055,
#     "$t_d$",
#     color="blue",
#     ha="center",
#     transform=ax.get_xaxis_transform(),
# )

# ── Anotação: tr (linha preta tracejada + rótulo) ─────────────────────────
ax.plot([tr, tr], [0, yss], color="black", linestyle="--", linewidth=1.4)
ax.text(
    tr + 0.05,
    -0.055,
    "$t_r$",
    color="black",
    ha="center",
    transform=ax.get_xaxis_transform(),
)

# ── Anotação: tp (linha verde tracejada + rótulo) ─────────────────────────
ax.plot([tp, tp], [0, Mp_abs], color="green", linestyle="--", linewidth=1.4)
ax.text(
    tp,
    -0.055,
    "$t_p$",
    color="green",
    ha="center",
    transform=ax.get_xaxis_transform(),
)

# ── Anotação: ts + faixa de tolerância (magenta) ─────────────────────────
ax.plot([ts, ts], [0, 1 + tol], color="magenta", linestyle="--", linewidth=1.4)
ax.plot(
    [ts, max(t_out)], [1 + tol, 1 + tol], color="magenta", linestyle="--", linewidth=1.4
)
ax.plot(
    [ts, max(t_out)], [1 - tol, 1 - tol], color="magenta", linestyle="--", linewidth=1.4
)
ax.text(
    ts,
    -0.055,
    "$t_s$",
    color="magenta",
    ha="center",
    transform=ax.get_xaxis_transform(),
)
ax.text(
    max(t_out) * 0.6, 1 + tol + 0.01, "Tolerância (±5%)", color="magenta", va="bottom"
)

# ── Indicadores de y_f e y_max ────────────────────────────────────────────

# y_f (valor final)
ax.text(max(t_out) * 1.06, yss - 0.05, r"$y_f$", ha="right", va="bottom")

# y_max (valor máximo)
ax.axhline(Mp_abs, color="darkorange", linestyle=":", linewidth=1.5)
ax.text(
    max(t_out) * 1.12,
    Mp_abs - 0.05,
    r"$y_{max}$",
    color="darkorange",
    ha="right",
    va="bottom",
)

# ── Formatação dos eixos ───────────────────────────────────────────────────
ax.set_xlim(0, 20)
ax.set_ylim(-0.02, 1.65)
ax.set_xlabel("Tempo")
ax.set_ylabel("Resposta")
ax.set_yticks([0, 0.5, 1.0, 1.5])
ax.tick_params()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.xaxis.set_major_locator(MultipleLocator(5))

plt.savefig("../figures/identificação-segunda-ordem.png", bbox_inches="tight")
plt.close()
