from itertools import cycle, islice
from time import perf_counter
from os.path import basename

program_name = basename(__file__).rstrip(".py")
with open(f"./input/{program_name}.in") as f:
    data = f.read().splitlines()
n_lines = len(data)
data = cycle(data)


def solve_part1():
    a = int(next(data))
    prev, count = a, 0
    for _ in range(n_lines - 1):
        depth = int(next(data))
        if depth > prev:
            count += 1
        prev = depth
    return count


def solve_part2():
    a, b, c = map(int, islice(data, 3))
    prev = a + b + c
    count = 0
    for _ in range(n_lines - 3):
        d = int(next(data))
        depth = b + c + d
        if depth > prev:
            count += 1
        prev = depth
        b, c = c, d
    return count


start = perf_counter()

s1 = solve_part1()
print("Solution 1:", s1)

s2 = solve_part2()
print("Solution 2:", s2)

print("Execution took", perf_counter() - start, "s")
