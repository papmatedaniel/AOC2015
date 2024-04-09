with open("Part2/file2.txt", "r", encoding="UTF-8") as file:
    szamlalo = 0
    for i in file.readlines():
        valasz,valasz2 = False, False
        for j in range(len(i)-1):
            karakterek = i[j] + i[j+1]
            if i.count(karakterek) > 1:
                valasz = True

            if j != len(i)-2:
                if i[j] == i[j+2]:
                    valasz2 = True
        if valasz and valasz2:
            szamlalo += 1

print(szamlalo)