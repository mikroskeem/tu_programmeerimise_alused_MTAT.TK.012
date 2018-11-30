def tervitus(num):
    print("Võõrustaja: \"Tere!\"")
    print("Täna {}. kord tervitada, mõtiskleb võõrustaja".format(num))
    print("Külaline: \"Tere, suur tänu kutse eest!\"")

guests = int(input("Sisestage külaliste arv: "))

for i in range(1, guests + 1):
    tervitus(i)
