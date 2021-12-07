from io import StringIO
import sys
from time import perf_counter
from os.path import basename
from collections import OrderedDict

input = lambda: sys.stdin.readline()
print = lambda *args: sys.stdout.write(" ".join(map(str, args)) + "\n")


def set_stdin():
    program_name = basename(__file__).rstrip(".py")
    with open(f"./input/{program_name}.in") as f:
        lines = f.readlines()
        sys.stdin = StringIO("".join(lines))
    return len(lines)


def solve(days):
    _ = set_stdin()
    timers = [0] * 9
    fishes = list(map(int, input().split(",")))
    for fish in fishes:
        timers[fish] += 1
    for _ in range(days):
        n0 = timers[0]
        timers[:8] = timers[1:]
        timers[8] = n0
        timers[6] += n0

    return sum(timers)


start = perf_counter()

s1 = solve(80)
print("Solution 1:", s1)

s2 = solve(256)
print("Solution 2:", s2)

print("Execution took", perf_counter() - start, "s")
