def is_invalid(number: str):
    if (len(number) % 2 == 1):
        return False

    return number[0:len(number)//2] == number[len(number)//2:len(number)]

id_ranges = list(map(lambda x: tuple(map(lambda k: str(k), x.split("-"))), open("input.txt").read().strip().split(",")))

count = 0
for id_range in id_ranges:
    for id in range(int(id_range[0]), int(id_range[1])+1):
        if is_invalid(str(id)):
            count += id

print(count)
