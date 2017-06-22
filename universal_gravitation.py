from matplotlib import pyplot as plt
import numpy as np

m_1 = 0.5
m_2 = 1.5
G = 6.674*10**-11

r = np.arange(100, 1000, 50)
F = G*m_1*m_2/r**2

plt.plot(r,F,marker='o')
plt.xlabel("Distance in meters")
plt.ylabel("Gravitational force in newtons")
plt.title("Gravitational force and distance")
plt.show()
