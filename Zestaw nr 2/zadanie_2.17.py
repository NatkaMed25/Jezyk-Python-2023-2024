file = open('line.txt', 'r')
line = file.read()
words = line.split()

alphabetical_order = sorted(words, key=str.lower)
length_order = sorted(words, key=len)

print('Kolejnosc alfabetyczna:', alphabetical_order)
print('Kolejnosc pod wzgledem dlugosci:', length_order)