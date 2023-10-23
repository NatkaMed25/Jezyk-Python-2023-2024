numbers = [561, 8, 2, 978, 12, 32, 9]
filled = []

for num in numbers:
    filled.append(str(num).zfill(3))

print(filled)