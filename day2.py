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
    depth, hor = 0, 0
    for _ in range(n_lines):
        _dir, step = input().split()
        step = int(step)
        if _dir == "forward":
            hor += step
        elif _dir == "up":
            depth -= step
        elif _dir == "down":
            depth += step

    return depth * hor


def solve_part2():
    n_lines = set_stdin()
    depth, hor, aim = 0, 0, 0
    for _ in range(n_lines):
        _dir, step = input().split()
        step = int(step)
        if _dir == "forward":
            hor += step
            depth += step * aim
        elif _dir == "up":
            aim -= step
        elif _dir == "down":
            aim += step

    return depth * hor


start = perf_counter()

s1 = solve_part1()
print("Solution 1:", s1)

s2 = solve_part2()
print("Solution 2:", s2)

print("Execution took", perf_counter() - start, "s")
