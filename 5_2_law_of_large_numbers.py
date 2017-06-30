import numpy as np


def roll_die():
    a = np.random.randint(1,7)
    return a


def trial_average(n):
    point_sum = 0
    for i in range(int(n)):
        point_sum += roll_die()
    avg = point_sum/n
    return avg

if __name__ == '__main__':
    expect_value = sum(range(1,7))/6
    print('Expected value: {0}'.format(expect_value))
    n = [1e2, 1e3, 1e4, 1e5, 5e5]
    print('{0:^10}{1:^10}'.format('Trials', 'Trial average'))
    for n_values in n:
        print('{0:^10}{1:^10.3f}'.format(int(n_values), trial_average(
            n_values)))