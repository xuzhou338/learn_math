from matplotlib import pyplot as plt
import random


def transformation_1(x, y):
    x1 = 0.85*x + 0.04*y
    y1 = -0.04*x + 0.85*y + 1.6
    return x1, y1

def transformation_2(x, y):
    x1 = 0.2*x - 0.26*y
    y1 = 0.23*x + 0.22*y + 1.6
    return x1, y1

def transformation_3(x, y):
    x1 = -0.15*x + 0.28*y
    y1 = -0.26*x + 0.24*y + 0.44
    return x1, y1

def transformation_4(x, y):
    x1 = 0
    y1 = 0.16*y
    return x1, y1

def draw_fern(n):
    x1, y1 = 0, 0
    x, y = [0], [0]
    p1 = [0.85, 0.07, 0.07, 0.01]
    p =[]
    ax = plt.gca()
    for p_i in range(len(p1)):
        p.append(sum(p1[0:p_i]))
    for i in range(n):
        r = random.random()
        if r <= p[1]:
            x1, y1 = transformation_1(x1, y1)
        elif r <= p[2]:
            x1, y1 = transformation_2(x1, y1)
        elif r <= p[3]:
            x1, y1 = transformation_3(x1, y1)
        else:
            x1, y1 = transformation_4(x1, y1)
        x.append(x1)
        y.append(y1)
    ax.scatter(x, y, s=2, c=y, cmap=plt.cm.autumn)
    plt.title('Barnsley Fern')
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.show()

if __name__ == '__main__':
    draw_fern(100000)