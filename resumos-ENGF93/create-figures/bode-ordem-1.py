import control as ct
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 18})

# Constantes de tempo
tau1 = 0.1
tau2 = 1
tau3 = 10

# Zero de primeira ordem
Gz1 = ct.tf([tau1, 1], [1])
Gz2 = ct.tf([tau2, 1], [1])
Gz3 = ct.tf([tau3, 1], [1])

# Polo de primeira ordem
Gp1 = ct.tf([1], [tau1, 1])
Gp2 = ct.tf([1], [tau2, 1])
Gp3 = ct.tf([1], [tau3, 1])

# Frequências
w = np.logspace(-2, 3, 2000)

# Figura
fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(8, 8), dpi=300, sharex=True, layout="constrained"
)

# -------------------------
# Zeros
# -------------------------
for G, tau in [
    (Gz1, tau1),
    (Gz2, tau2),
    (Gz3, tau3),
]:
    mag, phase, omega = ct.frequency_response(G, w)

    ax1.semilogx(omega, 20 * np.log10(mag), label=rf"$(1+s\tau),\ \tau={tau}$")

    ax2.semilogx(omega, np.degrees(phase))

# -------------------------
# Polos
# -------------------------
for G, tau in [
    (Gp1, tau1),
    (Gp2, tau2),
    (Gp3, tau3),
]:
    mag, phase, omega = ct.frequency_response(G, w)

    ax1.semilogx(omega, 20 * np.log10(mag), "--", label=rf"$1/(1+s\tau),\ \tau={tau}$")

    ax2.semilogx(omega, np.degrees(phase), "--")

##########################
Gzp = ct.tf([tau2, 1], [tau3, 1])
mag, phase, omega = ct.frequency_response(Gzp, w)

ax1.semilogx(
    omega, 20 * np.log10(mag), linewidth=3, label=rf"$\frac{{1+{tau2}s}}{{1+{tau3}s}}$"
)

ax2.semilogx(omega, np.degrees(phase), linewidth=3)


# Frequências de canto
for tau in [tau1, tau2, tau3]:
    wc = 1 / tau
    ax1.axvline(wc, color="k", alpha=0.2)
    ax2.axvline(wc, color="k", alpha=0.2)

# Aparência
ax1.set_ylabel("Magnitude / dB")
ax1.grid(True, which="both", alpha=0.2)
ax1.legend(fontsize=12)

ax2.set_ylabel("Fase / °")
ax2.set_xlabel(r"$\omega$ / (rad/s)")
ax2.grid(True, which="both", alpha=0.2)

plt.savefig("../figures/bode_ordem_1.png")
plt.close()
