sissetulekud = []

with open('konto.txt', 'r', encoding = 'UTF-8') as f:
    for row in f:
        num = float(row)
        if num <= 0.0:
            continue

        sissetulekud.append(row.strip())

for entry in sissetulekud:
    print(entry)
