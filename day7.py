from io import StringIO
import sys
from time import perf_counter
from os.path import basename
from statistics import mean, median
from math import floor, ceil

input = lambda: sys.stdin.readline()
print = lambda *args: sys.stdout.write(" ".join(map(str, args)) + "\n")


def set_stdin():
    program_name = basename(__file__).rstrip(".py")
    with open(f"./input/{program_name}.in") as f:
        lines = f.readlines()
        sys.stdin = StringIO("".join(lines))
    return len(lines)


def solve_part1():
    _ = set_stdin()
    locs = list(map(int, input().split(",")))
    med = int(median(locs))
    return sum(abs(n - med) for n in locs)


def solve_part2():
    _ = set_stdin()
    locs = list(map(int, input().split(",")))
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
