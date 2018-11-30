nimi = input("Sisestage oma nimi: ")
lubatud = int(input("Sisestage lubatud kiirus: "))
tegelik = int(input("Sisestage tegelik kiirus: "))
trahv = min(190, max(0, (tegelik - lubatud) * 3))

print("{}, kiiruse ületamise eest on teie trahv {} eurot.".format(nimi, trahv))
