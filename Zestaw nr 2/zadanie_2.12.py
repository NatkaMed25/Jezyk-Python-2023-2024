file = open('line.txt', 'r')
line = file.read()
words = line.split()

text_from_first_letters = ''
text_from_last_letters = ''

for word in words:
    text_from_first_letters += word[0]

for word in words:
    text_from_last_letters += word[len(word) - 1]

print('Napis stworzony z pierwszych znakow wyrazow:', text_from_first_letters)
print('Napis stworzony z ostatnich znakow wyrazow:', text_from_last_letters)