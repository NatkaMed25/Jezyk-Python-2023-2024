file = open('line.txt', 'r')
line = file.read()
words = line.split()

lengths = []

for word in words:
    lengths.append(len(word))

print('Laczna dlugosc wyrazow:', sum(lengths))