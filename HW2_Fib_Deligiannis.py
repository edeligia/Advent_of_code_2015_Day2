def Fib(n):
    if not isinstance(n, int) or n == 0:
        print("Please enter a non-zero integer.")
        return
    elif n < 0:
        print("Please enter a non-zero integer.")
        return
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a, b = 1, 2
        for i in range(3, n+1):
            a, b = b, a+b
        return b
    
print(Fib(5))
    