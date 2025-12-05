ranges = [list(int(x) for x in range.split("-")) for range in [x.splitlines() for x in open("input.txt", "r").read().strip().split("\n\n")][0]]

ranges.sort(key=lambda x: x[0])

merged = [ranges[0]]

for range in ranges[1:]:
    last_merged = merged[-1]

    if last_merged[1] < range[0]:
        merged.append(range)
        continue

    if last_merged[1] >= range[1]:
        continue

    merged[-1][1] = range[1]


count = sum([range[1] - range[0] + 1 for range in merged])

print(count)
