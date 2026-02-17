import matplotlib.pyplot as plt
import numpy as np

# Given parameters
f = 60                          # Frequency (Hz)
omega = 2 * np.pi * f           # Angular frequency
T = 1 / f                       # Period

# Time vector from 0 to 2T
t = np.linspace(0, 2*T, 1000)

# Voltage and current
v = 120 * np.sqrt(2) * np.sin(omega * t)
i = 60 * np.sqrt(2) * np.sin(omega * t + np.pi/6)

# Instantaneous power
p = v * i

# ---- Plot 1: Voltage and Current ----
plt.figure()
plt.plot(t, v, label='v(t)')
plt.plot(t, i, label='i(t)')
plt.xlim(0, 2*T)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Voltage and Current vs Time')
plt.legend()
plt.grid(True)

# ---- Plot 2: Instantaneous Power ----
plt.figure()
plt.plot(t, p, label='p(t) = v(t)i(t)')
plt.xlim(0, 2*T)
plt.xlabel('Time (s)')
plt.ylabel('Power (W)')
plt.title('Instantaneous Power vs Time')
plt.legend()
plt.grid(True)

plt.show()
