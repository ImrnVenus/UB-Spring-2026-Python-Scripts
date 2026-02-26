import matplotlib.pyplot as plt
import numpy as np

#Voltage is 10 V, Current is 10 A
V = 10
I = 10
#Theta I need to graph for: pi/2, pi/4, and 0
theta = 0
freq = 60

T = 1/freq   #The period of the signal
omega = 2*np.pi*freq  #Angular frequency 2*pi*f
t = np.linspace(0, 2*T, 1000)

p_a = V*I*(np.cos(theta)-np.cos(2*omega*t+theta)) #Power for A
p_b = V*I*(np.cos(theta)-np.cos(2*omega*t-(4*np.pi/3)+theta)) #Power for B
p_c = V*I*(np.cos(theta)-np.cos(2*omega*t+(4*np.pi/3)+theta)) #Power for C

P = 3*V*I*np.cos(theta) * np.ones_like(t) #Total Power

#Constructing a proper plot
plt.figure(figsize=(10, 6))
plt.plot(t, p_a, label='Phase A Power', color = 'red')
plt.plot(t, p_b, label='Phase B Power', color = 'blue')
plt.plot(t, p_c, label='Phase C Power', color='green')
plt.plot(t, P, label='Total Power', linestyle='--')

plt.title('Instantaneous Power in a Three-Phase System')
plt.xlabel('Time (seconds)')
plt.ylabel('Power (Watts)')
plt.legend()
plt.grid()

plt.show()
