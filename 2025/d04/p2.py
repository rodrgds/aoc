import copy

matrix = [[c for c in line] for line in open("input.txt").read().strip().splitlines()]

adjacent_matrix = []

directions = [(-1, -1), (1, 1), (1, -1), (-1, 1), (0, 1), (0, -1), (1, 0), (-1, 0)]

for i in range(len(matrix)):
    line = matrix[i]
    new_adjacencies = []
    for j in range(len(line)):
        char = line[j]
        count = -1
        if char == "@":
            count = 0
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

total_count = 0
count = -1
while count != 0:
    count = 0
    for line in adjacent_matrix:
        for c in line:
            if c < 4 and c > -1:
                count += 1

    initial_adjacency_matrix = copy.deepcopy(adjacent_matrix)
    for i in range(len(adjacent_matrix)):
        line = adjacent_matrix[i]
        for j in range(len(line)):
            c = line[j]
            initial_c = initial_adjacency_matrix[i][j]
            if initial_c < 4 and initial_c > -1:
                adjacent_matrix[i][j] = -1
                matrix[i][j] = "x"
                for dir in directions:
                    new_y = i + dir[0]
                    new_x = j + dir[1]
                    if new_y < 0 or new_y >= len(matrix) \
                    or new_x < 0 or new_x >= len(matrix[i]):
                        continue
                    if matrix[new_y][new_x] == "@":
                        adjacent_matrix[new_y][new_x] -= 1

    total_count += count

print(total_count)
