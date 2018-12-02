def telegramify(line, replacements):
    chars = []
    for c in line:
        c = c.upper()
        repl = replacements.get(c)
        if repl:
            c = repl

        chars.append(c)

    return "".join(chars)

replacements = {
    'Ä': 'AE',
    'Ö': 'OE',
    'Õ': 'OE',
    'Ü': 'UE'
}

filename = input("Sisestage failinimi: ")

with open(filename, 'r', encoding = 'UTF-8') as f:
    for line in f.readlines():
        print(telegramify(line.rstrip(), replacements))
