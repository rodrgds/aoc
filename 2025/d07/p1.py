lines = list(filter(None, [[c for c in line] if i % 2 == 0 else None for i, line in enumerate(open("input.txt", "r").read().strip().splitlines())]))

splitted_count = 0
positions = set()
positions.add(lines[0].index("S"))

for i in range(1, len(lines)):
    initial_pos = positions.copy()
    positions = set()

    for pos in initial_pos:
        if lines[i][pos] == "^":
            positions.add(pos-1)
            positions.add(pos+1)
            splitted_count += 1
        else:
            positions.add(pos)

print(splitted_count)
