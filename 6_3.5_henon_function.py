from matplotlib import pyplot as plt, animation


def trans(x1, y1):
    x2 = y1 + 1 - 1.4*x1**2
    y2 = 0.3*x1
    return x2, y2

fig = plt.gcf()
ax = plt.axes(xlim=(-1.5, 1.5), ylim=(-0.4, 0.4))
x, y = [1], [0]
plt.scatter(0, 0, c='red')


def update_pic(i):
    for i_1 in range(10):
        x1, y1 = x[-1], y[-1]
        x2, y2 = trans(x1, y1)
        x.append(x2)
        y.append(y2)
        ax.scatter(x, y, s=2, c='blue')

anim = animation.FuncAnimation(fig, update_pic, frames=100, interval=10,
                               repeat=False)
plt.show()