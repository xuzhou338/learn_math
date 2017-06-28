import sympy as sp

x = sp.Symbol('x')
ineq_obj = sp.sin(x) - 0.6 >0
ans = sp.solve_univariate_inequality(ineq_obj, x, relational=False)
print(ans)