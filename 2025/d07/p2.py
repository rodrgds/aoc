from functools import lru_cache

lines = list(filter(None, [[c for c in line] if i % 2 == 0 else None for i, line in enumerate(open("input.txt", "r").read().strip().splitlines())]))

@lru_cache()
def count_dfs(line_i, pos):
    if line_i == len(lines):
        return 1

    if lines[line_i][pos] == "^":
        return count_dfs(line_i+1, pos-1) + count_dfs(line_i+1, pos+1)
    return count_dfs(line_i+1, pos)

print(count_dfs(0, lines[0].index("S")))
