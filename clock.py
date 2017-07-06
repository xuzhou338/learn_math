from matplotlib import pyplot as plt
from matplotlib import animation
from datetime import datetime
import numpy as np

# Set up the clock frame
fig = plt.figure(1, (2,2))
ax = plt.axes(projection='polar')
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
for i in range(12):
    theta = 0 + i*30
    theta = np.radians(theta)
    ax.plot((theta, theta), (0.9, 1))
ax.scatter(0, 0, c='red')

def get_time():
    """This function returns the current time in the form of a dictionary"""
    time = datetime.now().timetuple()
    t = {}
    t['hour'] = time.tm_hour
    t['minute'] = time.tm_min
    t['second'] = time.tm_sec
    return t

def update_time(i):
    """The function updates and plot the time on the clock."""
    t = get_time()

    theta_sec = -t['second'] * np.pi / 30 + np.pi / 2
    second, = ax.plot((theta_sec, theta_sec), (0, 0.7), linewidth=1, c='red')
    theta_min = -t['minute'] * np.pi / 30 + np.pi / 2 - t['second'] * np.pi / 1800
    minute, = ax.plot((theta_min, theta_min), (0, 0.7), linewidth=2, c='black')
    theta_hr = -t['hour'] * np.pi / 6 + np.pi / 2 - t['minute'] * np.pi / 360
    hour, = ax.plot((theta_hr, theta_hr), (0, 0.5), linewidth=2, c='black')

    return second, minute, hour

# Plot the animation
anim = animation.FuncAnimation(fig, update_time, interval=1000, blit=True)
plt.show()