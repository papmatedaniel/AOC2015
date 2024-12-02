with open("Part1/file.txt", "r", encoding="UTF-8") as file:
    karakterekszama = 0
    memoria = 0
    for i in file.readlines():
        print(i, eval(i))
        print()
        print()
        memoria += len(eval(i))
        karakterekszama += len(i.strip())


print(karakterekszama - memoria)



