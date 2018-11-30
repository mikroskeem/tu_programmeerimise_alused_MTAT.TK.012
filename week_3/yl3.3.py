import random

täringuid = int(input("Sisesta täringute arv: "))

for number in range(0, täringuid):
    number = random.randint(1, 6)
    print(number)
