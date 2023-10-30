x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;

for i in "axby": if ord(i) < 100: print (i)     # W tej linii mamy bląd składniowy: if powinno się znaleźć w następnej linii po znaku tabulacji

for i in "axby": 
    if ord(i) < 100: print (i)                  # Poprawna wersja

for i in "axby": print (ord(i) if ord(i) < 100 else i)