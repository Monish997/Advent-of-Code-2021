from itertools import cycle
from time import perf_counter
from os.path import basename

program_name = basename(__file__).rstrip(".py")
with open(f"./input/{program_name}.in") as f:
    data = f.read().splitlines()
data = cycle(data)


def solve(days):
    timers = [0] * 9
    fishes = map(int, next(data).split(","))
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
