with open("Part1/file.txt", "r", encoding="UTF-8") as file:
    szamlalo = 0
    for i in file.read():
        if i == "(":
            szamlalo += 1
        else:
            szamlalo -= 1

print(szamlalo)