import math
from matplotlib import pyplot as plt
import numpy as np

def trajectory(v, theta):
    """By inputting the initial speed v and angle theta, this function plots
    the trajectory motion of the object till it falls back onto the ground."""
    g = 9.8
    v_x = v * math.cos(theta)
    v_y = v * math.sin(theta)
    t_tot = 2 * v * math.sin(theta) / g
    d_x = v_x * t_tot
    x_list = np.arange(0, d_x, 0.01)
    y_list = []
    for x in x_list:
        t = x / v_x
        y_list.append(v_y * t - 1/2 * g * t**2)
    y_list = np.array(y_list)
    plt.plot(x_list, y_list)
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.title("Trajectory Motion with initial speed of {0} m/s".format(v))
    #plt.title("Trajectory Motion with initial speed of {0} m/s and angle of {"
              #"1:.1f}\N{degree sign}".format(v, theta/math.pi*180))


if __name__ == '__main__':
    trajectory(5, math.pi / 10)
    trajectory(5, math.pi / 7)
    trajectory(5, math.pi / 5)
    trajectory(5, math.pi / 4)
    trajectory(5, math.pi / 3)
    trajectory(5, math.pi / 2.5)
    plt.legend(('v = 5, a pi/10', 'v = 5, a pi/7','v = 5, a pi/5', 'v = 5, '
                'a pi/4', 'v = 5, a pi/3', 'v = 5, a pi/2.5'))
    plt.show()