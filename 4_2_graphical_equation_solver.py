import sympy as sp

def graphical_equation_solver(expr1, expr2):
    """This function solves the two expressions and then plot the two
    expressions on the graph."""
    x, y = sp.symbols('x, y')
    ans = sp.solve((expr1, expr2), dict=True)
    soln = ans[0]
    print(soln[x], soln[y])
    line1 = sp.solve(expr1, y)
    line2 = sp.solve(expr2, y)
    fig = sp.plotting.plot(line1[0], line2[0],
                           legend=True, show=False)
    fig[0].line_color = 'b'
    fig[1].line_color = 'r'
    fig.show()

if __name__ == '__main__':
    expr1 = input("Expression 1:")
    expr2 = input("Expression 2:")
    try:
        expr1 = sp.sympify(expr1)
        expr2 = sp.sympify(expr2)
    except sp.SympifyError:
        print('Invalid input!')
    else:
        graphical_equation_solver(expr1, expr2)