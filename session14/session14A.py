def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)

num = 5
fact = factorial(num)
print(fact)