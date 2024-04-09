lista = [[0 for i in range(1000)] for j in range(1000)]
with open("Part2/file2.txt", "r", encoding="UTF-8") as file:
    for i in file.readlines():
        szoveg = i.strip().split("through")
        elso, masodik = szoveg
        if "toggle" in i:
            utasitas = "toggle"
        elif "turn on" in i:
            utasitas = "turn on"
        else:
            utasitas = "turn off"

        szam = ""
        for j in elso:
            if not (j.isspace() or j.isalpha()):
                szam += j


        szam = (int(szam.split(",")[0]), int(szam.split(",")[1]))
        masodik = (int(masodik.split(",")[0]), int(masodik.split(",")[1]))

        for x in range(szam[0], masodik[0] + 1):
            for y in range(szam[1], masodik[1] + 1):
                if "turn on" in utasitas:
                    lista[y][x] += 1
                elif "turn off" in utasitas:
                    lista[y][x] = max(0, lista[y][x] - 1)
                else:
                    lista[y][x] += 2


ossszeg = 0
for i in lista:
    for j in i:
        ossszeg += j
print(ossszeg)

#27-ik sor: ez a chatgpt megoldása: max(0, lista[y][x] - 1), az én megoldásom oda az volt, hogy -= 1, nem vettem észre hogy a feladatban megvan szabva
#hogy 0nál nem lehet kisebb a szám