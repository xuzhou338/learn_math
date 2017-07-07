from matplotlib import pyplot as plt
import random

from del_spines import del_spines


def trans(x1, y1):
    rd = random.randint(1, 3)
    if rd == 1:
        x2 = 0.5*x1
        y2 = 0.5*y1
    elif rd == 2:
        x2 = 0.5*x1 + 0.5
        y2 = 0.5*y1 + 0.5
    else:
        x2 = 0.5*x1 + 1
        y2 = 0.5*y1
    return x2, y2

x, y = [0], [0]
for i in range(10000):
    x1, y1 = x[-1], y[-1]
    x2, y2 = trans(x1, y1)
    x.append(x2)
    y.append(y2)

ax = del_spines(plt.gca())
ax.scatter(x, y, s=1, c=y, cmap=plt.cm.spring)
plt.show()
