lista = [1, 2, 3, 4, 5, 6]
for x in lista:
    if (x == 1) | (x == 6):
        print("O"*6)
    else:
        print("O" + ' '* 4 + "O")