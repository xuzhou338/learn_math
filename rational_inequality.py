import sympy as sp

x = sp.Symbol('x')
ineq_obj = ((x-1)/(x+2))> 0
lhs = ineq_obj.lhs
numer, denom = lhs.as_numer_denom()
p1 = sp.Poly(numer)
p2 = sp.Poly(denom)
rel = ineq_obj.rel_op
ans = sp.solve_rational_inequalities([[((p1, p2),rel)]])
print(ans)