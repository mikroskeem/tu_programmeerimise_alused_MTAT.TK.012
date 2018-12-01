def juurdekasv(area, juurdekasv_ha):
    return round(area * 0.4047 * juurdekasv_ha, 2)

filename = input("Sisestage failinimi: ")
juurdekasv_ha = float(input("Sisestage aastane juurdekasv hektari kohta tihumeetrites: "))
piir = float(input("Sisestage piir, mitmest aakrist suuremad metsatükid arvesse võtta: "))

ncalculated = 0
with open(filename, 'r', encoding = 'UTF-8') as f:
    for row in f:
        area = float(row)

        if area <= piir:
            print("Metsatükki ei võeta arvesse")
            continue

        ncalculated += 1

        print("Metsatüki aastane juurdekasv on {}".format(juurdekasv(area, juurdekasv_ha)))

print("Arvutati {} metsatüki juurdekasv.".format(ncalculated))
