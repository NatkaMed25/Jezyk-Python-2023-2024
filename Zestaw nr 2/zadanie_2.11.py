word = 'kotek'
new_word = ''

letters = list(word)

for i in range(0, len(letters)):
    if i == len(letters) - 1:
        new_word += letters[len(letters) - 1]
    else:
        new_word += letters[i] + '_'

print(new_word)