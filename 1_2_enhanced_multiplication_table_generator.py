def enhanced_multiplication_table_generator():
    a = int(input("Table of which number?"))
    n = int(input("How many rows in the table?"))

    for i in range(1,n+1):
        print("{0} * {1} = {2}".format(a, i, a*i))

if __name__ == '__main__':
    enhanced_multiplication_table_generator()