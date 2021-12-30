from itertools import cycle
from time import perf_counter
from os.path import basename
from collections import defaultdict

program_name = basename(__file__).rstrip(".py")
with open(f"./input/{program_name}.in") as f:
    data = f.read().splitlines()
n_lines = len(data)
data = cycle(data)


def solve_part1():
    freq = defaultdict(int)
    for _ in range(n_lines):
        p1, p2 = next(data).split(" -> ")
        p1, p2 = tuple(map(int, p1.split(","))), tuple(map(int, p2.split(",")))
        if p1[0] == p2[0]:
            s, e = sorted([p1[1], p2[1]])
            for i in range(s, e + 1):
                freq[(p1[0], i)] += 1
        elif p1[1] == p2[1]:
            s, e = sorted([p1[0], p2[0]])
            for i in range(s, e + 1):
                freq[(i, p1[1])] += 1

    ans = 0
    for _, f in freq.items():
        if f > 1:
            ans += 1
    return ans


def solve_part2():
    freq = defaultdict(int)
    for _ in range(n_lines):
        p1, p2 = map(eval, next(data).split(" -> "))
        if p1[0] == p2[0]:
            s, e = sorted([p1[1], p2[1]])
            for i in range(s, e + 1):
                freq[(p1[0], i)] += 1
        elif p1[1] == p2[1]:
            s, e = sorted([p1[0], p2[0]])
            for i in range(s, e + 1):
                freq[(i, p1[1])] += 1
        else:
            s, e = sorted([p1, p2])
            d = 1 if e[1] > s[1] else -1
            l = e[0] - s[0] + 1
            for i in range(l):
                freq[(s[0] + i, s[1] + d * i)] += 1

    ans = 0
    for _, f in freq.items():
        if f > 1:
            ans += 1
    return ans


start = perf_counter()

s1 = solve_part1()
print("Solution 1:", s1)

s2 = solve_part2()
print("Solution 2:", s2)

print("Execution took", perf_counter() - start, "s")
