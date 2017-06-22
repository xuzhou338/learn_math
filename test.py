import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,10)
y = x**2

plt.plot(x,y,marker='o')

print(plt.axis())
plt.ylim(ymax=100)
plt.savefig('test.svg')