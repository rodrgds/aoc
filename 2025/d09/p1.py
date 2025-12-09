coords = [tuple([int(line.split(",")[0]), int(line.split(",")[1])]) for line in open("input.txt", "r").readlines()]

max_area = 0
for i in range(len(coords)):
    for j in range(i, len(coords)):
        c1, c2 = coords[i], coords[j]
        area = (abs(coords[i][0] - coords[j][0])+1) * (abs(coords[i][1] - coords[j][1])+1)
        max_area = max(max_area, area)

print(max_area)
