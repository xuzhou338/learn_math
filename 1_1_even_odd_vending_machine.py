n = float(input("Enter a number:"))
if n.is_integer():
    n_followed = []
    for i in range(10):
        n_followed.append(n+i*2)
    if n%2 != 0:
        print("Even", n_followed)
    else:
        print("Odd", n_followed)
else:
    print("Please enter an integer!")

