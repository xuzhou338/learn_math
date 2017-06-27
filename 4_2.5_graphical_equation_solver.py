import sympy as sp, numpy as np
import matplotlib.pyplot as plt

def graphical_equation_solver(expr1, expr2):
    """This function calculates the intersection point of two equations and
    then plot the two lines as well as the intersection point.

    It is a improved version of the 4_2_graphical_equation_solver by plotting
    with Matplotlib instead of the Sympy."""

    # Move y to the other side of the equal sign
    soln = sp.solve((expr1, expr2), dict=True)[0]
    x, y = sp.symbols('x, y')
    intrsc = (soln[x], soln[y])

    # Define the x limit based on the location of the intersection
    x_lim = abs(4/3*intrsc[0])

    x = np.arange(-x_lim,x_lim+1)
    line1 = str(sp.solve(expr1, y)[0])
    line2 = str(sp.solve(expr2, y)[0])
    y1 = eval(line1)
    y2 = eval(line2)

    # Plot everything
    ax = plt.subplot(1, 1, 1)
    plt.plot(x, y1, label='y = ' + line1, zorder=1)
    plt.plot(x, y2, label='y = ' + line2, zorder=2)
    plt.scatter(intrsc[0], intrsc[1], c='red', label=str(intrsc), zorder=3)
    plt.legend()

    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    plt.show()

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