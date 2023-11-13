def make_ruler(n):
    ruler = ''

    for x in range(0, n):
        ruler += '|....'

    ruler += '|\n'

    for y in range(0, n):
        ruler += str(y) + (' ' * (5 - len(str(y+1))))

    ruler += str(n)

    return ruler

def make_grid(rows, cols):
    rect = ''

    for x in range(0, rows):
        rect += (cols * '+---') + '+\n'
        rect += (cols * '|   ') + '|\n'

    rect += (cols * '+---') + '+\n'

    return rect

print(make_ruler(12) + '\n')
print(make_grid(4, 3))