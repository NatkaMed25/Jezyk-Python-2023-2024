while(True):
    try:
        height = int(input('Podaj wysokość prostokąta: '))
        width = int(input('Podaj szerokość prostokąta: '))
        
        if height < 1 or width < 1:
            print('Wysokość oraz szerokość muszą być większe lub równe 1')
            continue

        rect = ''

        for x in range(0, height):
            rect += (width * '+---') + '+\n'
            rect += (width * '|   ') + '|\n'

        rect += (width * '+---') + '+\n'

        print(rect)

        break
    except ValueError:
        print('Błąd: Wprowadź liczbę całkowitą')