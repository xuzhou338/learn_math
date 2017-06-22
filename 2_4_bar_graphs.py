from matplotlib import pyplot as plt

data = [23, 12, 12, 32, 9]
positions = range(len(data))
plt.barh(positions, data)
plt.yticks(positions, ('Mon', 'Tue', 'Wed', 'Thur', 'Fri'))
plt.title('Weekday Dinner Expense')
plt.xlabel('Expense ($)')
plt.show()
