from matplotlib import pyplot as plt

fs = [1, 1]
fs_ratio = []
for i in range(50):
    fs_ratio.append(fs[-1] / fs[-2])
    fs.append(fs[-1] + fs[-2])

plt.plot(fs_ratio)
plt.xlabel('Length of the Fibonacci Sequence')
plt.ylabel('Ratio between the last value and the previous one')
plt.title('Fibonacci Sequence and the Golden Ratio')
plt.show()