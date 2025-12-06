_lines = [list(filter(None, line.strip().split(" "))) for line in open("input.txt", "r")]
numbers = [[int(x) for x in line] for line in _lines[:-1]]
operators = _lines[-1]

result = 0
for i in range(len(operators)):
    res = 0
    if operators[i] == "*":
        res = 1
    for j in range(len(numbers)):
        if operators[i] == "*":
            res *= numbers[j][i]
        elif operators[i] == "+":
            res += numbers[j][i]
    result += res

print(result)
