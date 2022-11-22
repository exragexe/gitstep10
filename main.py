


try:

    n = int(input("Enter num: "))

    res = {1: lambda n: all(n % i != 0 for i in range(2, int(n**.5)+1))}
    print(res[1](n))



except Exception as e:
    print(e)

