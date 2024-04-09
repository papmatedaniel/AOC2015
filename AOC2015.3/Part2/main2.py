with open("Part2/file2.txt", "r", encoding="UTF-8") as file:
    pont, pont2 = (0, 0), (0,0)
    pontok = set()
    for index, i in enumerate(file.read()):
        match i:
            case "^": 
               (pont := (pont[0], pont[1]+1)) if index % 2 == 0 else (pont2 := (pont2[0], pont2[1]+1))
            case "v": 
                (pont := (pont[0], pont[1]-1)) if index % 2 == 0 else (pont2 := (pont2[0], pont2[1]-1))
            case "<":
                (pont := (pont[0]-1, pont[1])) if index % 2 == 0 else (pont2 := (pont2[0]-1, pont2[1]))
            case ">":
                (pont := (pont[0]+1, pont[1])) if index % 2 == 0 else (pont2 := (pont2[0]+1, pont2[1]))

        pontok.add(pont)
        pontok.add(pont2)

print(len(pontok))