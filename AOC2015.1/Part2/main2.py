with open("Part2/file2.txt", "r", encoding="UTF-8") as file:
    szamlalo = 0

    for index, i in enumerate(file.read(), start=1):
        if i == "(":
            szamlalo += 1
        else:
            szamlalo -= 1
        if szamlalo == -1:
            print(index)
            break



