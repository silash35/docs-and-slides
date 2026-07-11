import matplotlib.pyplot as plt
import numpy as np

# Parâmetros
frequencia_amostragem = 100  # Hz
tempo_total = 100  # s
N = int(frequencia_amostragem * tempo_total)

# Vetor de tempo
tempo = np.linspace(0, tempo_total, N, endpoint=False)

# Definição do sinal
f = 5 * np.sin(0.1 * tempo) + np.sin(10 * tempo)

# FFT
yf = np.fft.fft(f)

# Frequências em Hz
xf = np.fft.fftfreq(N, d=1 / frequencia_amostragem)[: N // 2]

# Conversão para rad/s
xf = 2 * np.pi * xf

# Figura
plt.rcParams.update({"font.size": 18})
plt.figure(figsize=(7, 8), dpi=300, layout="constrained")

# -----------------------------
# Sinal no tempo
# -----------------------------
plt.subplot(2, 1, 1)

plt.plot(tempo, f)

plt.title(r"$f(t)=5 \cdot \sin(0.1t)+\sin(10t)$")

plt.xlabel("Tempo / s")
plt.grid(True)

# -----------------------------
# Espectro de Fourier
# -----------------------------
plt.subplot(2, 1, 2)

plt.plot(xf, 2.0 / N * np.abs(yf[: N // 2]))
plt.xlim(0, 15)

plt.title("Espectro do Sinal após FFT")
plt.xlabel(r"Frequência Angular / (rad/s)")
plt.grid(True)

plt.savefig("../figures/fft.png")
plt.close()
