original_lines = [line.replace("\n", "") for line in open("input.txt", "r")]
numbers = original_lines[:-1]
operators = original_lines[-1]

result = 0
curr_operator = "+"
res = 0
for j in range(len(original_lines[0])):
    if operators[j] != " ":
        curr_operator = operators[j]
        result += res
        if curr_operator == "*":
            res = 1
        elif curr_operator == "+":
            res = 0

    curr_number = "0"
    for line_i in range(len(numbers)):
        c = numbers[line_i][j]
        if c != " ":
            curr_number += c
    curr_number = int(curr_number)

    if curr_number == 0:
        continue

    if curr_operator == "*":
        res *= curr_number
    elif curr_operator == "+":
        res += curr_number

result += res

print(result)
