def fact(n):
    """This function calculates the factorial of the input number n."""
    fac = 1
    for i in range(1, n+1):
        fac = fac*i
    return fac

if __name__ == '__main__':
    n = input("n = ?")
    f = fact(int(n))
    print("The factorial of {0} is {1}.".format(n, f))