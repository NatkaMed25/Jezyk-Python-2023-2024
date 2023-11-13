def fibonacci(n):
    prev = 0
    curr = 1

    for x in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr

print('5 wyraz ciągu to', fibonacci(5))
print('7 wyraz ciągu to', fibonacci(7))
print('12 wyraz ciągu to', fibonacci(12))