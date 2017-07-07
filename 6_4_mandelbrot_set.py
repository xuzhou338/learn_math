from matplotlib import pyplot as plt
import numpy as np
from del_spines import del_spines


image = np.zeros((400, 400), dtype=np.int)

def determine_value(i_1, i_2, max_ite=100):
    xi = i_1*3.5/400-2.5
    yi = i_2*2/400-1
    j = 1j
    z = 0 + 0j
    c = xi + yi*j
    iteration = 0
    while iteration <= max_ite and abs(z) < 2:
        z = z**2 + c
        iteration += 1
    return iteration
ax = del_spines(plt.gca())
for i_1 in range(400):
    for i_2 in range(400):
        iteration = determine_value(i_1, i_2, 50)
        image[i_2][i_1] = iteration
plt.imshow(image, origin='lower', extent=(-2.5, 1, -1, 1), cmap=plt.cm.gray)
plt.show()
