import pygal

bar = pygal.Bar()
data = [23, 12, 12, 32, 9]
bar.x_labels = ('Mon', 'Tue', 'Wed', 'Thur', 'Fri')
bar.add('Dinner Expense', data)
bar.render_in_browser()