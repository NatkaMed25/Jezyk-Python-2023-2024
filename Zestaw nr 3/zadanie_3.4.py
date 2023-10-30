while(True):
    x  = input('Podaj liczbę rzeczywistą (lub \'stop\' aby zakończyć): ')

    if x.lower() == 'stop':
        break

    try:
        number = float(x)
    except:
        print('Nie została podana liczba rzeczywista')
        continue

    else:
        num = float(x)
        print('x =', num)
        print('x^3 =', num**3)