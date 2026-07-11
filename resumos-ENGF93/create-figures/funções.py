import matplotlib.pyplot as plt
import numpy as np

# =========================
# Figura 16:9 para slides
# =========================


plt.rcParams.update({"font.size": 18})

fig = plt.figure(figsize=(16, 9), dpi=300, layout="constrained")
gs = fig.add_gridspec(2, 3, height_ratios=[1, 1.25])

ax_exp = fig.add_subplot(gs[0, 0])
ax_log10 = fig.add_subplot(gs[0, 1])
ax_ln = fig.add_subplot(gs[0, 2])
ax_trig = fig.add_subplot(gs[1, :])

# =========================
# EXPONENCIAL
# =========================
x_exp = np.linspace(-1, 3, 1000)
y_exp = np.exp(x_exp)

ax_exp.plot(x_exp, y_exp, linewidth=2)

# pontos importantes
ax_exp.scatter(-1, np.exp(-1), s=60, label=rf"$e^{{-1}}={np.exp(-1):.3f}$")
ax_exp.scatter(0, np.exp(0), s=60, label=rf"$e^0={np.exp(0):.0f}$")
ax_exp.scatter(1, np.exp(1), s=60, label=rf"$e^1={np.exp(1):.3f}$")
ax_exp.scatter(np.log(10), 10, s=60, label=r"$e^{\ln(10)}=10$")

ax_exp.legend()

ax_exp.set_title("Função Exponencial")
ax_exp.grid(True, alpha=0.3)

# =========================
# LOG BASE 10
# =========================
x_log = np.linspace(0.001, 12, 1000)
y_log = np.log10(x_log)
ax_log10.plot(x_log, y_log, linewidth=2)

# pontos importantes
ax_log10.scatter([], [], label=r"$x \leq 0$: indefinido")
ax_log10.scatter(0.1, -1, s=60, label=r"$\log_{10}(0.1)=-1$")
ax_log10.scatter(1, 0, s=60, label=r"$\log_{10}(1)=0$")
ax_log10.scatter(10, 1, s=60, label=r"$\log_{10}(10)=1$")

ax_log10.legend()

# espaço vazio para x=-1
ax_log10.axvspan(-1, 0, alpha=0.05)

ax_log10.set_xlim(-1, 12)

ax_log10.set_title("Logaritmo Base 10")
ax_log10.grid(True, alpha=0.3)

# =========================
# LN
# =========================
x_ln = np.linspace(0.001, 12, 1000)
y_ln = np.log(x_ln)

ax_ln.plot(x_ln, y_ln, linewidth=2)

# pontos importantes
ax_ln.scatter([], [], label=r"$x \leq 0$: indefinido")
ax_ln.scatter(1, 0, s=60, label=r"$\ln(1)=0$")
ax_ln.scatter(np.e, 1, s=60, label=r"$\ln(e)=1$")
ax_ln.scatter(10, np.log(10), s=60, label=rf"$\ln(10)={np.log(10):.3f}$")
ax_ln.legend()

# espaço vazio para região inválida
ax_ln.axvspan(-1, 0, alpha=0.05)

ax_ln.set_xlim(-1, 12)

ax_ln.set_title("Logaritmo Natural")
ax_ln.grid(True, alpha=0.3)

# =========================
# SENO E COSSENO
# =========================
x = np.linspace(0, 2 * np.pi, 2000)

# curvas principais
ax_trig.plot(x, np.sin(x), linewidth=2.5, label="sen(x)")
ax_trig.plot(x, np.cos(x), linewidth=2.5, label=r"$\cos(x)=\sin(x+90^\circ)$")

# defasagens do seno
phasings_deg = [-90, -45, 45]

for phi_deg in phasings_deg:
    phi = np.deg2rad(phi_deg)

    ax_trig.plot(
        x, np.sin(x + phi), alpha=0.4, linewidth=2, label=rf"sen(x + φ), φ={phi_deg}°"
    )

ax_trig.set_xticks(
    [0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
    ["0", "π/2 = 90°", "π = 180°", "3π/2 = 270°", "2π = 360°"],
)

ax_trig.set_title("Seno, Cosseno e Defasagens")
ax_trig.grid(True, alpha=0.3)
ax_trig.legend(ncol=3)

plt.savefig("../figures/funções.png")
plt.close()
