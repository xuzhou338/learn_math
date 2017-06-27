from sympy import symbols, init_printing, pprint


def series_print(n, x_val):
    init_printing(order='rev-lex')
    x = symbols('x')
    series = x
    for k in range(2, int(n)+1):
        series = series + x**k/k
    print("\nThe series is:")
    pprint(series)
    print("\nThe value is:")
    print('{0:.4f}'.format(float(series.subs({x:x_val}))))

if __name__ == '__main__':
    n = input("n = ")
    x = input("x = ")
    series_print(n, x)

