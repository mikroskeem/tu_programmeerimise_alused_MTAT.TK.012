ostjad = int(input("Sisesta ostjate arv: "))

total = 0
for n in range(1, ostjad + 1, 2):
    total += n

print("Lillede koguarv on {}".format(total))
