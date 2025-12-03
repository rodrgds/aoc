banks = [[int(c) for c in line] for line in open("input.txt").read().strip().splitlines()]

def get_result(bank, og_sorted_bank, sorted_bank, curr):
    if len(curr) == 12:
        return int("".join([str(x) for x in curr]))

    sorted_bank = sorted(list(set(og_sorted_bank)), reverse=True)

    while len(sorted_bank) != 0:
        m = sorted_bank.pop(0)
        try:
            idx = bank.index(m)
        except ValueError:
            continue

        old_bank = list(bank)
        bank = bank[idx+1:len(bank)]
        res = get_result(bank, og_sorted_bank, sorted_bank, curr + [m])
        if res != False:
            return res
        bank = list(old_bank)

    return False

_sum = 0

for i in range(len(banks)):
    _max = 0
    mlist = list()
    sorted_bank = sorted(banks[i], reverse=True)
    og_sorted_bank = list(sorted_bank)

    _sum += get_result(banks[i], og_sorted_bank, sorted_bank, mlist)

print(_sum)
