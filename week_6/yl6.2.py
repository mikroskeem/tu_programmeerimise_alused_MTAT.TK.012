def teleri_diagonaal(distance):
    return round(distance * 100 * 0.39 / 2.5)

distance = float(input("Sisesta kaugus: "))
print(teleri_diagonaal(distance))
