matrix = [[c for c in line] for line in open("input.txt").read().strip().splitlines()]

adjacent_matrix = []

for i in range(len(matrix)):
    line = matrix[i]
    new_adjacencies = []
    for j in range(len(line)):
        char = line[j]
        count = -1
        if char == "@":
            count = 0
            directions = [(-1, -1), (1, 1), (1, -1), (-1, 1), (0, 1), (0, -1), (1, 0), (-1, 0)]
            for dir in directions:
                new_y = i + dir[0]
                new_x = j + dir[1]
                if new_y < 0 or new_y >= len(matrix) \
                or new_x < 0 or new_x >= len(matrix[i]):
                    continue
                if matrix[new_y][new_x] == "@":
                    count += 1
        new_adjacencies.append(count)
    adjacent_matrix.append(new_adjacencies)

count = 0
for line in adjacent_matrix:
    for c in line:
        if c < 4 and c != -1:
            count += 1

print(count)
