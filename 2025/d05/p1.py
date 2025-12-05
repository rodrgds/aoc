unformatted_sections = [x.splitlines() for x in open("input.txt", "r").read().strip().split("\n\n")]

ranges = [tuple(int(x) for x in range.split("-")) for range in unformatted_sections[0]]

numbers = [int(x) for x in unformatted_sections[1]]

def num_in_range(number, range):
    return range[0] <= number <= range[1]

count = 0

for number in numbers:
    for range in ranges:
        if num_in_range(number, range):
            count += 1
            break

print(count)
