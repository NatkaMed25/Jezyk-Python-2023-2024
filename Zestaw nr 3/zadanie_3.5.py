while(True):
    try:
        length = int(input('Podaj długość miarki: '))
        
        if length < 1:
            print('Długość miarki musi być większa lub równa 1')
            continue

        ruler = ''

        for x in range(0, length):
            ruler += '|....'

        ruler += '|\n'

        for y in range(0, length):
            ruler += str(y) + (' ' * (5 - len(str(y+1))))

        ruler += str(length)

        print(ruler)

        break
    except ValueError:
        print('Błąd: Wprowadź liczbę całkowitą')