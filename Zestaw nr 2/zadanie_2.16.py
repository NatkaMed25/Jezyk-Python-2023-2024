file = open('line.txt', 'r')
old_line = file.read()

print(old_line)

new_line = old_line.replace('GvR', 'Guido van Rossum')

print(new_line)