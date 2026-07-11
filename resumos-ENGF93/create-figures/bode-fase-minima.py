import control as ct
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 18})

# Sistemas
G_z_lhp = ct.tf([1, 1], [1])  # 1 + s
G_z_rhp = ct.tf([-1, 1], [1])  # 1 - s

G_p_lhp = ct.tf([1], [1, 1])  # 1/(1 + s)
G_p_rhp = ct.tf([1], [-1, 1])  # 1/(1 - s)

# Frequências
w = np.logspace(-2, 2, 1000)

# Figura
fig, (ax1, ax2) = plt.subplots(
    2,
    1,
    figsize=(8, 8),
    dpi=300,
    sharex=True,
    layout="constrained",
)

styles = ["-", "--", "-.", ":"]

for i, (G, label) in enumerate(
    [
        (G_z_lhp, r"$G=1+s$"),
        (G_z_rhp, r"$G=1-s$"),
        (G_p_lhp, r"$G=\frac{1}{1+s}$"),
        (G_p_rhp, r"$G=\frac{1}{1-s}$"),
    ]
):
    mag, phase, omega = ct.frequency_response(G, w)

    mag_db = 20 * np.log10(mag)
    phase_deg = np.degrees(phase)

    ax1.semilogx(omega, mag_db, linestyle=styles[i], linewidth=3, label=label)

    ax2.semilogx(omega, phase_deg, linestyle=styles[i], linewidth=3)

ax1.set_ylabel("Magnitude / dB")
ax1.grid(True, which="both")
ax1.legend()

ax2.set_ylabel("Fase / °")
ax2.set_xlabel(r"$\omega$ / (rad/s)")
ax2.grid(True, which="both")

plt.savefig("../figures/bode_fase_minima.png")
plt.close()
