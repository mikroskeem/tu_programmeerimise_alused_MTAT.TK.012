def eelarve(guests):
    return 55 + guests * 10

class Guest:
    def __init__(self, name, decision):
        if decision not in ["+", "?"]:
            raise "Invalid decision: " + decision

        self.name = name
        self.decision = decision

guests = []
filename = input("Sisesta failinimi: ")
with open(filename, 'r', encoding = 'UTF-8') as f:
    for row in f:
        decision, name = row.strip().split(" ")
        guests.append(Guest(name, decision))

invited = len(guests)
coming = len([d for d in guests if d.decision == "+"])

print("Kutsutud on {} inimest".format(invited))
print("{} inimest tuleb".format(coming))

print("Maksimaalne eelarve: {} eurot".format(eelarve(invited)))
print("Minimaalne eelarve: {} eurot".format(eelarve(coming)))
