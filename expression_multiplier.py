'''
Product of two expressions
'''

import sympy as sp

def expression_multiply(expr1, expr2):
    """This function multiplies two expressions"""
    prod = sp.expand(expr1*expr2)
    return prod

if __name__ == '__main__':
    expr1 = input("Expression 1 = ")
    expr2 = input("Expression 2 = ")

    try:
        expr1 = sp.simplify(expr1)
        expr2 = sp.simplify(expr2)
    except SimplifyError:
        print("Invalid input!")
    else:
        prod = expression_multiply(expr1, expr2)
        print(prod)
