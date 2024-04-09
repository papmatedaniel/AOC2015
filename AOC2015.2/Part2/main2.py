with open("Part2/file2.txt", "r", encoding="UTF-8") as file:
    masni = 0
    for i in file.readlines():
        a, b, c = map(int, i.split("x"))
        terfogat = a * b * c
        loterulet = min([2*(a+b), 2*(a+c), 2*(c+b)])
        masni += terfogat + loterulet

print(masni)