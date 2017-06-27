import sympy as sp

def factor_finder(expr):
    """This function finds the factors of the input expression."""
    factors = sp.factor(expr)
    sp.pprint(factors)

if __name__ == '__main__':
    expr = input("Expression = ")
    try:
        expr = sp.sympify(expr)
    except sp.SympifyError:
        print("Invalid input!")
    else:
        factor_finder(expr)