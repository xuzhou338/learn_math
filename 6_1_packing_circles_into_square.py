from matplotlib import pyplot as plt


ax = plt.axes(xlim=(1, 5), ylim=(1, 5), aspect='equal')
square = plt.Rectangle((1, 1), 5, 5)
ax.add_patch(square)
circ_locs = []
for i_1 in range(4):
    for i_2 in range(4):
        circ_loc = (i_1 + 1.5, i_2 + 1.5)
        circ_locs.append(circ_loc)

for circ_loc in circ_locs:
    circle = plt.Circle(circ_loc, 0.5, color='white')
    ax.add_patch(circle)

plt.show()