import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import dct, idct
from scipy.optimize import minimize

# Parameters for the sinusoidal signal
f = 5  # Frequency of the sinusoidal signal (Hz)
fs_nyquist = 2 * f  # Nyquist sampling rate
T = 1.0 / f  # Period of the signal
t = np.linspace(0, 2 * T, 1000)  # Time vector for the original signal
t_nyquist = np.linspace(0, 2 * T, int(2 * T * fs_nyquist))  # Time vector for Nyquist sampling

# Generate the original sinusoidal signal
original_signal = np.sin(2 * np.pi * f * t)

# Nyquist sampling
nyquist_signal = np.sin(2 * np.pi * f * t_nyquist)

# Reconstruct the original signal using Nyquist sampling
reconstructed_nyquist = np.interp(t, t_nyquist, nyquist_signal)

# Compressive Sensing
def compressive_sensing(signal, m):
    n = len(signal)
    A = np.random.randn(m, n)  # Random measurement matrix
    y = np.dot(A, signal)  # Compressed measurements
    return y, A

def l1_minimization(y, A):
    n = A.shape[1]
    x0 = np.zeros(n)
    res = minimize(lambda x: np.linalg.norm(np.dot(A, x) - y, 2), x0, method='BFGS')
    return res.x

# Apply compressive sensing
m = 50  # Number of measurements
y, A = compressive_sensing(original_signal, m)
reconstructed_cs = l1_minimization(y, A)

# Plotting
plt.figure(figsize=(14, 10))

# Original Signal
plt.subplot(4, 1, 1)
plt.plot(t, original_signal, label='Original Signal')
plt.title('Original Sinusoidal Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()

# Nyquist Sampled Signal
plt.subplot(4, 1, 2)
plt.stem(t_nyquist, nyquist_signal, label='Nyquist Sampled Signal', basefmt=" ")
plt.title('Nyquist Sampled Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()

# Reconstructed Signal using Nyquist Sampling
plt.subplot(4, 1, 3)
plt.plot(t, reconstructed_nyquist, label='Reconstructed Signal (Nyquist)')
plt.title('Reconstructed Signal using Nyquist Sampling')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()

# Reconstructed Signal using Compressive Sensing
plt.subplot(4, 1, 4)
plt.plot(t, reconstructed_cs, label='Reconstructed Signal (Compressive Sensing)')
plt.title('Reconstructed Signal using Compressive Sensing')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()

plt.tight_layout()
plt.show()