file = open('line.txt', 'r')
line = file.read()
words = line.split()

longest_word = ''

for word in words:
    if len(word) > len(longest_word):
        longest_word = word
        longest_word_length = len(word)

print('Najdluzsze slowo:', longest_word)
print('Jego dlugosc:', longest_word_length)