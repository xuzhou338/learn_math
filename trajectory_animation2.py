from matplotlib import pyplot as plt, animation
import numpy as np

g = 9.8

theta = np.pi/4
v = 5

t_total = 2*v*np.sin(theta)/g
t_step = 0.005
x_locs = []
y_locs = []
t = 0

while t < t_total:
    x = t*v*np.cos(theta)
    y = t*v*np.sin(theta) - 1/2*g*t**2
    x_locs.append(x)
    y_locs.append(y)
    t += t_step

def update_loc(i, block, line):

    block.xy = (x_locs[i], y_locs[i])
    if i > 2:
        x_data = x_locs[0:i+1]
        y_data = y_locs[0:i+1]
        line.set_xdata(x_data)
        line.set_ydata(y_data)
    return block, line,

fig = plt.gcf()
x_max = x_locs[-1]*1.2
y_max = y_locs[int(len(y_locs)/2)]*1.2
ax = plt.axes(xlim=(0, x_max), ylim=(0, y_max))
line, = ax.plot(0, 0)
rect_width = 0.05
rect_height = 0.05*y_max/x_max
block = plt.Rectangle((0, 0), rect_width, rect_height, facecolor='red')
ax.add_patch(block)

anim = animation.FuncAnimation(fig, update_loc, fargs=(block, line,),
                               frames=len(x_locs), interval=30, repeat=True)
plt.title('Projectile Motion')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()