import sympy as sp

def sum_series(term, n_num):
    """This function sums the series from 1 to n_num for the nth term
    provided from the input."""
    n = sp.Symbol('n')
    s = sp.summation(term, (n, 1, n_num))
    print(s)

if __name__ == '__main__':
    term = input('nth term :')
    n = input('n = ')

    try:
        term = sp.sympify(term)
    except sp.SympifyError:
        print('Invalid input!')
    else:
        sum_series(term, n)