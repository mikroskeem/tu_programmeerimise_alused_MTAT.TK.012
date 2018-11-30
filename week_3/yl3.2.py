kliente = int(input("Sisestage klientide arv: "))

lilled = 0
a = 1

while a <= kliente:
    if a % 2 != 0:
        lilled += a
    a += 1

print("Lillede koguarv on {}".format(lilled))
