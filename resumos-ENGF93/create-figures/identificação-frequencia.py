import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# Sinal de entrada e saída
# -----------------------------
A_u = 1.0
A_y = 0.6
w = 2 * np.pi  # 1 Hz
phi = np.pi / 4  # defasagem (45°)

t = np.linspace(0, 1.5, 2000)

u = A_u * np.sin(w * t)
y = A_y * np.sin(w * t + phi)

# -----------------------------
# Características
# -----------------------------
T = 2 * np.pi / w

# Pico da entrada
t_u = 1 / (4 * 1)  # T/4
u_peak = A_u

# Pico da saída
t_y = (np.pi / 2 - phi) / w
while t_y < 0:
    t_y += T

y_peak = A_y

# -----------------------------
# Gráfico
# -----------------------------
plt.rcParams.update({"font.size": 18})

plt.figure(dpi=300, layout="constrained")
fig, ax = plt.subplots(figsize=(8, 6))

ax.plot(t, u, label=r"$u(t)$")
ax.plot(
    t,
    y,
    label=r"$y(t)$",
)

# -----------------------------
# Amplitude entrada
# -----------------------------
ax.annotate("", xy=(t_u, 0), xytext=(t_u, A_u), arrowprops=dict(arrowstyle="<->"))

ax.text(t_u + 0.03, A_u / 2, r"$A_u$", va="center")

# -----------------------------
# Amplitude saída
# -----------------------------
ax.annotate("", xy=(t_y, 0), xytext=(t_y, A_y), arrowprops=dict(arrowstyle="<->"))

ax.text(t_y + 0.03, A_y / 2, r"$A_y$", va="center")

# -----------------------------
# Período
# -----------------------------
ax.annotate("", xy=(0, -1.35), xytext=(T, -1.35), arrowprops=dict(arrowstyle="<->"))

ax.text(T / 2, -1.3, r"$T$", ha="center")

# -----------------------------
# Defasagem (distância entre picos)
# -----------------------------
ax.annotate(
    "",
    xy=(t_y, A_y + 0.40),
    xytext=(t_u, A_y + 0.40),
    arrowprops=dict(arrowstyle="<->"),
)

ax.text((t_u + t_y) / 2, A_y + 0.5, r"$\Delta t$", ha="center")

# Marcação dos picos
ax.plot(t_u, u_peak, "o", label="$t_u$")
ax.plot(t_y, y_peak, "o", label="$t_y$")

# -----------------------------
# Aparência
# -----------------------------
ax.set_xlabel("Tempo / s")
ax.set_ylabel("Amplitude")

ax.grid(True)
ax.legend(loc="lower right")

ax.set_ylim(-1.5, 1.5)

plt.savefig("../figures/identificacao_frequencia.png")
plt.close()
