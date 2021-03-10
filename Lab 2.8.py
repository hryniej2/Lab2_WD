lista = []
a = 1
print(type(a))
while a <= 10:
    x = float(input("Podaj liczbe: "))
    a = a+1
    if(x- int(x)==0):
        lista.append(x)
        print(lista)
