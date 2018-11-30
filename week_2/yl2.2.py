def user_boolean(text):
    return text.lower() == "jah"

size = float(input("Sisesta kirja suurus: "))
topic = input("Sisesta kirja teema pealkiri: ")
inc_file = user_boolean(input("Kas kirjaga on kaasas fail? "))

if len(topic) < 1 or (inc_file and size > 1.0):
    print("Kiri on spämm")
else:
    print("Kiri ei ole spämm")
