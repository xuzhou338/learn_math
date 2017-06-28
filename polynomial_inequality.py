import sympy as sp

x = sp.symbols('x')
ineq_obj = -x**2 + 4 < 0
lhs = ineq_obj.lhs
p = sp.Poly(lhs, x)
rel = ineq_obj.rel_op
ans = sp.solve_poly_inequality(p, rel)
print(ans)