#Feladat megvalósítás
#1. 1000x1000-es mátrix létrehozása
#2Olyan programot írni, amely a mátrixban egy téglalap/négyzet alakzatban megtudja változtatni a mátrix pontjat
#   : A téglalap/négyzetnek az egymással átlós pontja vannak megadva. A pontoknak x és y koordinátájuk van

#Feladat lebontása
#Írj egy programot, ami egy 10x10 mátrixba letud kapcsolni egy fényt
#Írj egy programot, ami egy 10x10 mátrixba letud kapcsolni egy sorban vagy oszlopban összetartozó fényeket
#Írj egy programot, ami egy 10x10 mátrixba letud kapcsoni egy sor és egy másik sor között lévő fényeket, vagy egy oszlop és egy mási sor közötti fényeket.
#további részletek.

lista = [[i for i in (1000*"F")] for j in range(1000)]

with open("Part1/file.txt", "r", encoding="UTF-8") as file:
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
                    lista[y][x] = "N"
                elif "turn off" in utasitas:
                    lista[y][x] = "F"
                else:
                    if lista[y][x] == "N":
                        lista[y][x] = "F"
                    elif lista[y][x] == "F":
                        lista[y][x] = "N"

szamlalo = 0
for i in lista:
    for j in i:
        if j == "N":
            szamlalo += 1


print(szamlalo)

#A kódom működése kezdetben nem jó eredményt adott vissza, de a chatgpt-vel valamennyire sikerült ki debuggolnom
#ott hibáztam, hogy a matrix létrehozásánál az elemek default értéke "." volt, és amikor toggle, azaz cserélni kellett a lámpa állapotát, akkor 
#a defaultat nem cserélte, pedig azt is kellett volna, hiszen az volt a szövegben, hogy kezdetben minden lámpának kikapcsolva kell lennie