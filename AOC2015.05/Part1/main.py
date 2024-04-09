with open("Part1/file.txt", "r", encoding="UTF-8") as file:
    szamlalo = 0
    for i in file.readlines():
        if ("ab" not in i and "cd" not in i and "pq" not in i and "xy" not in i): 
            if sum([1 for k in i if k in "aeiou"]) >= 3:
                for j in range(len(i)-1):
                    if i[j] == i[j+1]:
                        szamlalo += 1
                        break

print(szamlalo)