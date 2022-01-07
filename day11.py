from functools import lru_cache
from os.path import basename
from time import perf_counter

import numpy as np

program_name = basename(__file__).rstrip(".py")
with open(f"./input/{program_name}.in") as f:
    data = f.read().splitlines()
grid = np.array([list(map(int, line)) for line in data], dtype=np.uint8)
rows, cols = grid.shape


@lru_cache(maxsize=None)
def neighbors(x, y):
    neighbors = []
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if i == x and j == y:
                continue
            if i < 0 or j < 0 or i >= rows or j >= cols:
                continue
            neighbors.append((i, j))
    return neighbors


def solve_part1():
    grid1, steps = np.copy(grid), 100
    flash = 0
    for _ in range(steps):
        grid1 += np.ones((rows, cols), dtype=np.uint8)
        indices = list(zip(*np.where(grid1 > 9)))
        while indices:
            for x, y in indices:
                flash += 1
                grid1[x, y] = 0
                affected = neighbors(x, y)
                for i, j in affected:
                    grid1[i, j] += 1 if grid1[i, j] else 0
            indices = list(zip(*np.where(grid1 > 9)))
    return flash


def solve_part2():
    grid2 = np.copy(grid)
    step = 0
    while True:
        if not grid2.any():
            return step
        grid2 += np.ones((rows, cols), dtype=np.uint8)
        indices = list(zip(*np.where(grid2 > 9)))
        while indices:
            for x, y in indices:
                grid2[x, y] = 0
                affected = neighbors(x, y)
                for i, j in affected:
                    grid2[i, j] += 1 if grid2[i, j] else 0
            indices = list(zip(*np.where(grid2 > 9)))
        step += 1


start = perf_counter()

s1 = solve_part1()
print("Solution 1:", s1)

s2 = solve_part2()
print("Solution 2:", s2)

print("Execution took", perf_counter() - start, "s")
