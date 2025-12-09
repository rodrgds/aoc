coords = [tuple([int(line.split(",")[0]), int(line.split(",")[1])]) for line in open("input.txt", "r").readlines()]

walls = []
for i in range(len(coords) - 1):
    walls.append(tuple([coords[i], coords[i+1]]))
walls.append(tuple([coords[-1], coords[0]]))

max_area = 0
for i in range(len(coords)):
    for j in range(i, len(coords)):
        c1, c2 = coords[i], coords[j]
        c1x, c1y = c1
        c2x, c2y = c2
        min_x, max_x = min(c1x, c2x), max(c1x, c2x)
        min_y, max_y = min(c1y, c2y), max(c1y, c2y)

        outer_break = False

        for wall in walls:
            w1x, w1y = wall[0];
            w2x, w2y = wall[1];

            if w1x == w2x:
                if min_x < w1x < max_x:
                    wall_y_min, wall_y_max = min(w1y, w2y), max(w1y, w2y)

                    if max(min_y, wall_y_min) < min(max_y, wall_y_max):
                        break_outer = True
                        break

            elif w1y == w2y:
                if min_y < w1y < max_y:
                    wall_x_min, wall_x_max = min(w1x, w2x), max(w1x, w2x)

                    if max(min_x, wall_x_min) < min(max_x, wall_x_max):
                        break_outer = True
                        break


        if outer_break:
            continue

        area = (abs(coords[i][0] - coords[j][0])+1) * (abs(coords[i][1] - coords[j][1])+1)
        max_area = max(max_area, area)




print(max_area)
