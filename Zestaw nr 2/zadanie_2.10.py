file = open('line.txt', 'r')

line = file.read()

words = line.split()

print('Liczba slow:', len(words))