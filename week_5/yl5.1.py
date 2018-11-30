mopeedid = []
with open('mopeedid.txt', 'r', encoding = 'UTF-8') as f:
    for row in f:
        mopeedid.append(int(row))

month = int(input("Palun sisestage mitmes kuu: "))

if month < 13 and month > 0:
    print("{}. kuul registreeriti {} uut mopeedi.".format(month, mopeedid[month -1]))
else:
    print("Vigane kuu")
