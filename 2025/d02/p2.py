def is_invalid(number: str):
    n1 = number[0]
    equals = True
    for n in number:
        if n != n1:
            equals = False
    if len(number) > 1 and equals:
        return True

    for i in range(2, len(number)):
        if len(number) % i != 0:
            continue

        numbers = [number[k] for k in range(i)]

        repeats = True
        for j in range(i, len(number), i):
            for k in range(i):
                if numbers[k] != number[j + k]:
                    repeats = False

        if repeats == True:
            return True

    return False

assert(is_invalid("111") == True)
assert(is_invalid("121212") == True)
assert(is_invalid("123123") == True)
assert(is_invalid("32453245") == True)
assert(is_invalid("1") == False)
assert(is_invalid("12345") == False)
assert(is_invalid("424") == False)
assert(is_invalid("1000") == False)
assert(is_invalid("2121212118") == False)

id_ranges = list(map(lambda x: tuple(map(lambda k: str(k), x.split("-"))), open("input.txt").read().strip().split(",")))

count = 0
for id_range in id_ranges:
    for id in range(int(id_range[0]), int(id_range[1])+1):
        if is_invalid(str(id)):
            count += id

print(count)
