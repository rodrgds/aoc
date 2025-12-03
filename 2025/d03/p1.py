banks = [[int(c) for c in line] for line in open("input.txt").read().strip().splitlines()]

_sum = 0

for i in range(len(banks)):
    _max = 0
    for j in range(len(banks[0])):
        for k in range(j+1, len(banks[0])):
            _max = max(int(str(banks[i][j]) + str(banks[i][k])), _max)
    _sum += _max


print(_sum)
