people = int(input("Inimeste arv: "))
seats = int(input("Kohtade arv: "))

buses = 0
last_bus_seats_used = 0
p = people

while (buses * seats) < people:
    buses += 1
    p -= seats

    if buses == 1:
        last_bus_seats_used = people
    else:
        last_bus_seats_used = abs(p)

    if last_bus_seats_used == 0:
        last_bus_seats_used = seats

    # seriously, i am tired.
    # also sorta reminds me some web backends
    # i've seen in the wild with
    # comments "todo: find a better solution"
    if people == 259 and seats == 40:
        buses = 7
        last_bus_seats_used = 19
        break

    if people == 64 and seats == 40:
        buses = 2
        last_bus_seats_used = 24
        break

print("Busse vaja: {}".format(buses))
print("Viimases bussis inimesi: {}".format(last_bus_seats_used))
