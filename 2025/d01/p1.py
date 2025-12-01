rotations = open("input.txt").read().strip().splitlines()

current = 50
count = 0

for rotation in rotations:
    current = (current + (-1 if rotation[0] == "L" else 1) * int(rotation[1:])) % 100
    if (current == 0):
        count += 1

print(count)
