import random

tõenäosus = int(input("Sisesta visketabavuse tõenäosus: "))
tõenäosus = tõenäosus / 100

viskeid = 1000
vise = 1
tabatud = 0

while viskeid > 0:
    x = random.random()
    if x < tõenäosus:
        print("{}. vise tabas".format(vise))
        tabatud += 1
    else:
        print("{}. vise mööda".format(vise))
    viskeid -= 1
    vise += 1

print("Tabas {} viset.".format(tabatud))
