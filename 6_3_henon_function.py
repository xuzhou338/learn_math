from matplotlib import pyplot as plt


def trans(x1, y1):
    x2 = y1 + 1 - 1.4*x1**2
    y2 = 0.3*x1
    return x2, y2

x, y = [1], [0]
for i in range(10000):
    x1, y1 = x[-1], y[-1]
    x2, y2 = trans(x1, y1)
    x.append(x2)
    y.append(y2)

plt.scatter(0, 0, c='red')
plt.scatter(x, y, s=2)
plt.show()