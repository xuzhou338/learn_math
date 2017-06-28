import sympy as sp

def isolve(expr):
    """This function solves the inequality."""
    x = sp.Symbol('x')
    if expr.is_polynomial():
        lhs = expr.lhs
        p = sp.Poly(lhs, x)
        rel = expr.rel_op
        ans = sp.solve_poly_inequality(p, rel)
    elif expr.is_rational_function():
        lhs = expr.lhs
        numer, denom = lhs.as_numer_denom()
        p1 = sp.Poly(numer)
        p2 = sp.Poly(denom)
        rel = expr.rel_op
        ans = sp.solve_rational_inequalities([[((p1, p2), rel)]])
    else:
        ans = sp.solve_univariate_inequality(expr, x, relational=False)

    print(ans)

if __name__ == '__main__':
    expr = input("The inequality about x is: ")
    try:
        expr = sp.sympify(expr)
    except sp.SympifyError:
        print('Invalid input!')
    else:
        isolve(expr)