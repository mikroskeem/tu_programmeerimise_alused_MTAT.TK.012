def eelarve(guests):
    return 55 + guests * 10

invited = int(input("Mitu inimest on kutsutud? "))
coming = int(input("Mitu inimest tuleb? "))

print("Maksimaalne eelarve: {} eurot".format(eelarve(invited)))
print("Minimaalne eelarve: {} eurot".format(eelarve(coming)))
