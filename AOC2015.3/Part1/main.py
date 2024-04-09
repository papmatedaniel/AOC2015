with open("Part1/adat.txt", "r", encoding="UTF-8") as file:
    pont = (0,0)
    pontok = set() 
    for karakter in file.read():
        match karakter:
            case "<" :
                pont = pont[0]-1,pont[1]
            case ">": 
                pont = pont[0]+1,pont[1]
            case "^" :
                pont = pont[0],pont[1]+1
            case "v" :
                pont = pont[0],pont[1]-1
        pontok.add(pont)


print(len(pontok))