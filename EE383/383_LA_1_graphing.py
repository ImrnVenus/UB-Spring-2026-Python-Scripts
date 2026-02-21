import numpy as np
import matplotlib.pyplot as plt

f0 = 10  # Fundamental frequency in Hz

f = np.linspace(-20, 20, 5000)

#Assigning the signal from 2a to variable X
X = np.sinc(2*f - 2*f0) + np.sinc(2*f + 2*f0)

#Assigning the signal from 2b to variable Y
Y = (1/4)*np.sinc(f/2)+(1/8)*np.sinc((f-f0)/2)+(1/8)*np.sinc((f+f0)/2)

#Assigning the signal from 3 to variable Z
Z = (1/2)*np.sinc((f/2)-(f0/2))+(1/2)*np.sinc((f/2)+(f0/2))

#Finding the Energy Spectral Density for Z
ESD = np.abs(Z)**2

# Magnitude
magnitudeX = np.abs(X)
magnitudeY = np.abs(Y)

# Plotting the magnitude of X(f)
plt.figure()
plt.plot(f, magnitudeX,color = 'blue')
plt.xlabel('Frequency (f)')
plt.ylabel('|X(f)|')
plt.title(f'Graph for 2A with f0 = {f0} Hz')
plt.grid(True)
plt.show()

# Plotting the magnitude of Y(f)
plt.figure()
plt.plot(f, magnitudeY, color = 'red')
plt.xlabel('Frequency (f)')
plt.ylabel('|Y(f)|')
plt.title(f'Graph for 2B with f0 = {f0} Hz')
plt.grid(True)
plt.show()

# Plotting the Energy Spectral Density of Z(f)
plt.figure()
plt.plot(f,ESD,color = 'orange')
plt.xlabel('Frequency (f)')
plt.ylabel('Energy Spectral Density')
plt.title(f'Graph for Question 3 with f0 = {f0} Hz')
plt.grid(True)
plt.show()