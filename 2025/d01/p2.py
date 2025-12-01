rotations = open("input.txt").read().strip().splitlines()

current = 50
count = 0

for rotation in rotations:
    change = (-1 if rotation[0] == "L" else 1) * int(rotation[1:])
    if (current + change > 100):
        count += ((current + change) - 100) // 100 + 1
    elif (current + change < 0):
        count += abs(current + change) // 100 + 1
        if (current == 0):
            count -= 1
    elif ((current + change) % 100 == 0):
        count += 1

    current = (current + change) % 100

print(count)
