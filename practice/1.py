# fibonacci series using recursion
def fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

# Print first 5 numbers of Fibonacci series
for i in range(1, 6):
    print(fibo(i),end = " ")


# Print numbers from 1 to N using recursion.


