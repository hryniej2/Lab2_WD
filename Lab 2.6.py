a = input("Podaj 1 liczbę: ")
b = input("Podaj 2 liczbę: ")
c = input("Podaj 3 liczbę: ")
a = int(a)
b = int(b)
c = int(c)
if (a % 2 == 0) | b > c:
    print("Parzysta i b>c")
else:
    if (a % 2 == 0) | b < c:
        print("Parzysta i b<c")
    else:
        if (a % 2 > 0) | b > c:
            print("Nieparzysta i b>c")
        else:
            if (a % 2 > 0) | b < c:
                print("Nieparzysta i b<c")