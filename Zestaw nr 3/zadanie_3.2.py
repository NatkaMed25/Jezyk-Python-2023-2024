L = [3, 5, 4] ; L = L.sort()

x, y = 1, 2, 3               # błąd: Próbujemy przypisać trzy wartości a mamy tylko dwie zmienne

X = 1, 2, 3 ; X[1] = 4       # błąd: Nie można zmieniać wartości w tupli

X = [1, 2, 3] ; X[3] = 4     # bląd: Brak pozycji z indeksem 3 na liście

X = "abc" ; X.append("d")    # błąd: Brak funkcji append() dla stringów

L = list(map(pow, range(8))) # bład: W funkcji pow() brakuje argumentow