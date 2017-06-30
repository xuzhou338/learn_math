import csv, numpy as np
from matplotlib_venn import venn2
from sympy import FiniteSet
from matplotlib import pyplot as plt

filename = "5_1_sports_survey.csv"

data = []

for i in range(1, 21):
    num = np.random.randint(1, 4)

    data.append(str(i))
    if num == 1:
        data.append('1')
        data.append('0')
    elif num == 2:
        data.append('0')
        data.append('1')
    else:
        data.append('1')
        data.append('1')

data = np.array(data).reshape(20, 3)

filename = "5_1_sports_survery.csv"

with open(filename, 'w') as f:
    f_writer = csv.writer(f, delimiter=',')
    f_writer.writerows(data)

with open(filename, 'r') as f:
    data_r = []
    f_reader = csv.reader(f, delimiter=',')
    for line in f_reader:
        if line:
            for elem in line:
                data_r.append(int(elem))
data_r = np.array(data_r).reshape(-1,3)

football = []
others = []
for row in data:
    if row[1] == '1':
        football.append(str(row[0]))
    if row[2] == '1':
        others.append(str(row[0]))


football = FiniteSet(*football)
others = FiniteSet(*others)

print(football)
print(others)

venn2([football, others], set_labels=('football', 'others'))
plt.show()




