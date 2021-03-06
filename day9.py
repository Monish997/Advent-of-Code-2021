from itertools import cycle
from time import perf_counter
from os.path import basename

program_name = basename(__file__).rstrip(".py")
with open(f"./input/{program_name}.in") as f:
    data = f.read().splitlines()
grid = [list(map(int, row)) for row in data]
rows, cols = len(grid), len(grid[0])
data = cycle(data)


def get_adjacent(grid, row, col):
    rows, cols = len(grid), len(grid[0])
    neighbors = []
    if row - 1 >= 0:
        neighbors.append((row - 1, col))
    if row + 1 < rows:
        neighbors.append((row + 1, col))
    if col - 1 >= 0:
        neighbors.append((row, col - 1))
    if col + 1 < cols:
        neighbors.append((row, col + 1))
    return neighbors


def get_basin_size(grid, r, c, explored):
    stack = [(r, c)]
    size = 0
    while stack:
        i, j = stack.pop()
        if (i, j) not in explored and grid[i][j] != 9:
            stack += get_adjacent(grid, i, j)
            explored.add((i, j))
            size += 1
    return size


def solve_part1():
    risk_level = 0
    for row in range(rows):
        for col in range(cols):
            neighbors = get_adjacent(grid, row, col)
            if all(grid[row_][col_] > grid[row][col] for row_, col_ in neighbors):
                risk_level += grid[row][col] + 1
    return risk_level


def solve_part2():
    explored = set()
    basins = []
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 9:
                size = get_basin_size(grid, r, c, explored)
                basins.append(size)
    basins.sort()
    return basins[-1] * basins[-2] * basins[-3]


start = perf_counter()

s1 = solve_part1()
print("Solution 1:", s1)

s2 = solve_part2()
print("Solution 2:", s2)

print("Execution took", perf_counter() - start, "s")
