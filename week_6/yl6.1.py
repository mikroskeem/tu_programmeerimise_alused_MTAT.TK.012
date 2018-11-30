def banner(sentence):
    return sentence.upper()

howmanytimes = int(input("Mitu korda soovite reklaamlauset kuvada?"))
sentence = banner(input("Sisestage reklaamlause: "))

for i in range(0, howmanytimes + 1):
    print(sentence)
