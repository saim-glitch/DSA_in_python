import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
from sklearn.linear_model import Lasso

# ---------------- STEP 1: Generate a Sinusoidal Signal ----------------
fs = 100  # Original sampling frequency
t = np.linspace(0, 1, fs, endpoint=False)  # 1-second duration
frequencies = [5, 15, 30]  # Multiple frequency components
signal = np.sum([np.sin(2 * np.pi * f * t) for f in frequencies], axis=0)

# ---------------- STEP 2: Nyquist Sampling ----------------
fs_nyquist = 2 * max(frequencies)  # Nyquist rate
t_nyquist = np.linspace(0, 1, fs_nyquist, endpoint=False)
signal_nyquist = np.sum([np.sin(2 * np.pi * f * t_nyquist) for f in frequencies], axis=0)

# ---------------- STEP 3: Compressive Sampling ----------------
n = len(signal)  # Full signal length
m = int(n * 0.3)  # 30% compressed measurements
num_frequencies = 10  # Number of dominant frequency components

# Compute FFT to find dominant frequency components
fft_signal = fft(signal)
magnitude = np.abs(fft_signal)
indices = np.argsort(magnitude)[-num_frequencies:]  # Top dominant frequency indices

# Create a measurement matrix based on dominant frequencies
phi = np.zeros((m, n))
for i, idx in enumerate(indices[:m]):
    phi[i, idx] = 1  # Sampling only dominant frequency locations

# Measure the signal
y = phi @ signal

# ---------------- STEP 4: Signal Reconstruction Using LASSO ----------------
lasso = Lasso(alpha=0.01, max_iter=1000)
lasso.fit(phi, y)
x_recovered = lasso.coef_

# Inverse FFT to reconstruct the signal
signal_reconstructed = np.real(ifft(x_recovered))

# ---------------- PLOTTING ----------------

# FIGURE 1: Original Signal, Nyquist Sampled Signal, and Compressive Sensing Sampled Signal
plt.figure(figsize=(12, 6))
plt.plot(t, signal, label="Original Signal", color='k', linewidth=1)
plt.scatter(t_nyquist, signal_nyquist, color='b', label="Nyquist Sampled Signal", marker='o')
plt.scatter(t[indices], signal[indices], color='r', label="Compressive Sensing Sampled Signal", marker='x')
plt.legend()
plt.title("Original Signal vs Nyquist vs Compressive Sensing Samples")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

# FIGURE 2: Nyquist Sampled Signal vs Reconstructed Signal
plt.figure(figsize=(12, 6))
plt.plot(t, signal, label="Original Signal", color='k', linewidth=1)
plt.scatter(t_nyquist, signal_nyquist, color='b', label="Nyquist Sampled Signal", marker='o')
plt.plot(t_nyquist, signal_nyquist, color='g', linestyle='dashed', label="Reconstructed from Nyquist Samples")
plt.legend()
plt.title("Nyquist Sampling & Reconstruction")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

# FIGURE 3: Compressive Sensing Sampled Signal vs Reconstructed Signal
plt.figure(figsize=(12, 6))
plt.plot(t, signal, label="Original Signal", color='k', linewidth=1)
plt.scatter(t[indices], signal[indices], color='r', label="Compressive Sensing Sampled Signal", marker='x')
plt.plot(t, signal_reconstructed, color='m', linestyle='dashed', label="Reconstructed from Compressive Sensing")
plt.legend()
plt.title("Compressive Sensing & Reconstruction using LASSO")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()
