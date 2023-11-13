def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

print('5! =', factorial(5))
print('8! =', factorial(8))
print('3! =', factorial(3))