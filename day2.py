from itertools import cycle
from time import perf_counter
from os.path import basename

program_name = basename(__file__).rstrip(".py")
with open(f"./input/{program_name}.in") as f:
    data = f.read().splitlines()
n_lines = len(data)
data = cycle(data)


def solve_part1():
    depth, hor = 0, 0
    for _ in range(n_lines):
        _dir, step = next(data).split()
        step = int(step)
        if _dir == "forward":
            hor += step
        elif _dir == "up":
            depth -= step
        elif _dir == "down":
            depth += step

    return depth * hor


def solve_part2():
    depth, hor, aim = 0, 0, 0
    for _ in range(n_lines):
        _dir, step = next(data).split()
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
