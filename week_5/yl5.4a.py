destinations = []

filename = input("Palun sisestage failinimi: ")

with open(filename, 'r', encoding = 'UTF-8') as f:
    for row in f:
        destinations.append(row.strip())

print("Võimalikud sihtkohad:")
for number, destination in enumerate(destinations):
    print("{}. {}".format(number + 1, destination))

choice = int(input("Valige mitmes sihtkoht broneerida: ")) - 1

if choice < 0 or choice > len(destinations) - 1:
    print("Vigane valik")
else:
    destination = destinations[choice]
    print("Reis on broneeritud. Sihtkoht on {}".format(destination))
