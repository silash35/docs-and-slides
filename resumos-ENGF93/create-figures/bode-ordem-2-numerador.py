import control as ct
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 18})

# Frequência natural
wn = 1

# Amortecimentos
ksi_values = [0.2, 0.8, 5.0]

# Frequências
w = np.logspace(-2, 2, 2000)

# Figura
fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(8, 8), dpi=300, sharex=True, layout="constrained"
)

for ksi in ksi_values:
    # Numerador de segunda ordem
    G = ct.tf(
        [1, 2 * ksi * wn, wn**2],
        [wn**2],
    )

    mag, phase, omega = ct.frequency_response(G, w)

    if ksi > 1:
        wz1 = wn * (ksi - np.sqrt(ksi**2 - 1))
        wz2 = wn * (ksi + np.sqrt(ksi**2 - 1))

        label = (
            rf"$\xi={ksi}$"
            + "\n"
            + rf"$\omega_{{z1}}={wz1:.2f}$"
            + ", "
            + rf"$\omega_{{z2}}={wz2:.2f}$"
        )
    else:
        label = rf"$\xi={ksi},\ \omega_n={wn}$"

    ax1.semilogx(
        omega,
        20 * np.log10(mag),
        label=label,
    )

    ax2.semilogx(
        omega,
        np.degrees(phase),
    )

# Frequência natural
ax1.axvline(wn, color="k", alpha=0.2)
ax2.axvline(wn, color="k", alpha=0.2)

# Aparência
ax1.set_ylabel("Magnitude / dB")
ax1.grid(True, which="both", alpha=0.2)
ax1.legend()

ax2.set_ylabel("Fase / °")
ax2.set_xlabel(r"$\omega$ / (rad/s)")
ax2.grid(True, which="both", alpha=0.2)

plt.savefig("../figures/bode_ordem_2_numerador.png")
plt.close()
