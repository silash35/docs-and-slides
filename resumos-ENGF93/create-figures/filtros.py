import control as ct
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 18})

# Frequências
w = np.logspace(-3, 3, 2000)

# -----------------------------
# Filtros de 1ª ordem
# -----------------------------

LPF = ct.tf([1], [1, 1])  # 1/(1+s)
HPF = ct.tf([1, 0], [1, 1])  # s/(1+s)

# Respostas
mag_lpf, _, omega = ct.frequency_response(LPF, w)
mag_hpf, _, _ = ct.frequency_response(HPF, w)

# -----------------------------
# Figura
# -----------------------------
fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(8, 8), dpi=300, sharex=True, layout="constrained"
)

# -----------------------------
# Passa-baixa
# -----------------------------
ax1.semilogx(
    omega,
    20 * np.log10(mag_lpf),
    linewidth=3,
    label=r"$G(s)=\frac{1}{1+s}$",
)

ax1.set_title("Filtro Passa-Baixa (LPF)")
ax1.set_ylabel("Magnitude / dB")
ax1.grid(True, which="both", alpha=0.3)
ax1.legend()

# -----------------------------
# Passa-alta
# -----------------------------
ax2.semilogx(
    omega,
    20 * np.log10(mag_hpf),
    linewidth=3,
    label=r"$G(s)=\frac{s}{1+s}$",
)

ax2.set_title("Filtro Passa-Alta (HPF)")
ax2.set_ylabel("Magnitude / dB")
ax2.set_xlabel(r"$\omega$ / (rad/s)")
ax2.grid(True, which="both", alpha=0.3)
ax2.legend()

# Frequência de corte
for ax in [ax1, ax2]:
    ax.axvline(1, color="k", alpha=0.2)

plt.savefig("../figures/filtros.png")
plt.close()
