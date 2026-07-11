import control as ct
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 18})

# Sistemas
Gk_10 = ct.tf([10], [1])  # K=10
Gk_1 = ct.tf([1], [1])  # K=1
Gk_0_1 = ct.tf([0.1], [1])  # K=0.1
Gk_minus = ct.tf([-5], [1])  # K=-5

Gi = ct.tf([1], [1, 0])  # 1/s
Gd = ct.tf([1, 0], [1])  # s

# Frequências
w = np.logspace(-1, 1, 1000)

# Figura
fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(8, 8), dpi=300, sharex=True, layout="constrained"
)


styles = ["-", "--", ":"]

for i, (G, label) in enumerate(
    [
        (Gk_10, r"$K=10$"),
        (Gk_1, r"$K=1$"),
        (Gk_0_1, r"$K=0.1$"),
        (Gk_minus, r"$K=-5$"),
        (Gi, r"$1/s$"),
        (Gd, r"$s$"),
    ]
):
    mag, phase, omega = ct.frequency_response(G, w)

    mag_db = 20 * np.log10(mag)
    phase_deg = np.degrees(phase)

    ax1.semilogx(
        omega, mag_db, label=label, linestyle=styles[i % len(styles)], linewidth=3
    )
    ax2.semilogx(omega, phase_deg, linestyle=styles[i % len(styles)], linewidth=3)

ax1.set_ylabel("Magnitude / dB")
ax1.grid(True, which="both")
ax1.legend()

ax2.set_ylabel("Fase / °")
ax2.set_xlabel(r"$\omega$ / (rad/s)")
ax2.grid(True, which="both")

plt.savefig("../figures/bode_basicos.png")
plt.close()
