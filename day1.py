from io import StringIO
import sys
from time import perf_counter
from os.path import basename

input = lambda: sys.stdin.readline()
print = lambda *args: sys.stdout.write(" ".join(map(str, args)) + "\n")


def set_stdin():
    program_name = basename(__file__).rstrip(".py")
    with open(f"./input/{program_name}.in") as f:
        lines = f.readlines()
        sys.stdin = StringIO("".join(lines))
    return len(lines)


def solve_part1():
    n_lines = set_stdin()
    a = int(input())
    prev = a
    count = 0
    for i in range(n_lines - 1):
        depth = int(input())
        if depth > prev:
            count += 1
        prev = depth
    return count


def solve_part2():
    n_lines = set_stdin()
    a = int(input())
    b = int(input())
    c = int(input())
    prev = a + b + c
    count = 0
    for i in range(n_lines - 3):
        d = int(input())
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
