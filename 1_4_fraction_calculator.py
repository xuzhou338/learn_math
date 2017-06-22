from fractions import Fraction

def fraction_calculator(a, b, op):
    if op == 'add':
        print("Result of Addition: {0}".format(a + b))

    if op == 'subtract':
        print("Result of Subtraction: {0}".format(a - b))

    if op == 'multiply':
        print("Result of Multiplication: {0}".format(a * b))

    if op == 'divide':
        print("Result of Division: {0}".format(a / b))

if __name__ == '__main__':
    a = input("Enter first fraction:")
    b = input("Enter second fraction:")
    op = input("Operation to perform - add, subtract, divide or multiply:")
    a_1 = int(a[0])
    a_2 = int(a[2])
    a = Fraction(a_1, a_2)
    b_1 = int(b[0])
    b_2 = int(b[2])
    b = Fraction(b_1, b_2)
    fraction_calculator(a, b, op)