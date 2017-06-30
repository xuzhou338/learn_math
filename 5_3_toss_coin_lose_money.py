import numpy as np
from matplotlib import pyplot as plt
from mpldatacursor import datacursor

def toss_coin(money):
    count = 0
    money_list = [money]
    while money > 0:
        coin = np.random.randint(1,3)
        if coin == 1:
            money += 1
            status = 'Heads!'
        elif coin == 2:
            money -= 1.5
            status = 'Tails!'
        print('{0} Current amount: {1}'.format(status, money))
        count += 1
        money_list.append(money)
    print('Game over :( Current amount: {0}. Coints tossed: {1}'.format(
        money, count))
    plt.plot(money_list, marker='o')
    datacursor(hover=True, display='single', bbox=dict(alpha=1))
    plt.grid()
    plt.show()

if __name__ == '__main__':
    m = input('Enter your starting amount: ')
    toss_coin((int(m)))

