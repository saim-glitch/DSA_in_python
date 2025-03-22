import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 100  # Original sampling frequency
t = np.linspace(0, 1, fs, endpoint=False)  # 1-second duration
frequencies = [5, 15, 30]  # Multiple frequency components

# Generate the signal by summing sinusoidal components
signal = np.sum([np.sin(2 * np.pi * f * t) for f in frequencies], axis=0)

# Plot the signal
plt.figure(figsize=(10, 6))
plt.plot(t, signal, label='Signal', color='b')
plt.title('Signal with Multiple Frequency Components')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()