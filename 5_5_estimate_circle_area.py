import numpy as np
import random


def cal_circ_area(r, n):
    success = 0
    for i in range(n):
        x = r*2*(random.random()-0.5)
        y = r*2*(random.random()-0.5)
        loc = np.sqrt(x**2+y**2)

        if loc < r:
            success += 1
    area = (2*r)**2*success/n
    pi = 4*success/n
    return area, pi

if __name__ == '__main__':
    r = 2
    n = [1e3, 1e5, 1e6]
    area = np.pi*r**2
    area_est_list = []
    print('Radius: {0}'.format(r))
    for n_value in n:
        area_est, pi = cal_circ_area(r, int(n_value))
        area_est_list.append(area_est)
        print('\nArea: {0:.4f}, Estimated ({1} darts): {2:4f}'.format(area,
                                             int(n_value), area_est))
        print('pi = {0}'.format(pi))

