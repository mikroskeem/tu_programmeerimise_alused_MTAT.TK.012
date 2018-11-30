from datetime import datetime

diaryfile = open('paevik.txt', 'a', encoding = 'UTF-8')
entry = input("Sisesta sissekande tekst: ")

with open('paevik.txt', 'a', encoding = 'UTF-8') as f:
    f.writelines([str(datetime.today()) + "\n", entry + "\n", "\n"])
