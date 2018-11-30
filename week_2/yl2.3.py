name = input("Sisestage Leedu perekonnanimi: ")

if name[-2:] == "ne":
    print("Abielus")
elif name[-2:] == "te":
    print("Vallaline")
elif name[-1] == "e":
    print("Määramata")
else:
    print("Pole ilmselt leedulanna perekonnanimi")
