with open("Part1/file.txt", "r", encoding="UTF-8") as f:
    total_paper = 0
    for line in f:
        a, b, c = map(int, line.strip().split("x"))
        total_paper += (2 * (a * b + a * c + b * c)) + min((a*b), (a*c), (b*c))

print(total_paper)
