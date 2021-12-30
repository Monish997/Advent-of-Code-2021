from itertools import cycle
from time import perf_counter
from os.path import basename
from math import floor, ceil
from statistics import mean, median

program_name = basename(__file__).rstrip(".py")
with open(f"./input/{program_name}.in") as f:
    data = f.read().splitlines()
data = cycle(data)


def solve_part1():
    locs = list(map(int, next(data).split(",")))
    med = int(median(locs))
    return sum(abs(n - med) for n in locs)


def solve_part2():
    locs = list(map(int, next(data).split(",")))
    x = mean(locs)
    x1, x2 = floor(x), ceil(x)
    d1 = sum(abs(x1 - n) * (abs(x1 - n) + 1) / 2 for n in locs)
    d2 = sum(abs(x2 - n) * (abs(x2 - n) + 1) / 2 for n in locs)
    return int(min(d1, d2))


start = perf_counter()

s1 = solve_part1()
print("Solution 1:", s1)

s2 = solve_part2()
print("Solution 2:", s2)

print("Execution took", perf_counter() - start, "s")
