liczby = [3, 6, 2.5, 4.20, 9, 4]
suma = 0
wynik = []
dlug = len(liczby)
for x in range(1, dlug, 1):
    suma = liczby[x] + liczby[x-1]
    wynik.append(suma)
    print(wynik)
