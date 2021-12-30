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
    def check_win(boards):
        for board in boards:
            for row in board:
                if all(x == "x" for x in row):
                    return board
            for col in zip(*board):
                if all(x == "x" for x in col):
                    return board
        return

    nums = list(map(int, next(data).split(",")))
    n_boards = int((n_lines - 1) / 6)
    boards = []
    num_map = defaultdict(list)
    for i in range(n_boards):
        _ = next(data)
        board = []
        for j in range(5):
            row = list(map(int, next(data).split()))
            for k, n in enumerate(row):
                num_map[n].append((i, j, k))
            board.append(row)
        boards.append(board)
    for num in nums:
        for loc in num_map[num]:
            i, j, k = loc
            boards[i][j][k] = "x"
        winner = check_win(boards)
        if winner:
            unmarked = [i for row in winner for i in row if i != "x"]
            return sum(unmarked) * num


def solve_part2():
    def check_unwin(boards):
        for board in boards:
            if all(any(x != "x" for x in row) for row in board):
                if all(any(x != "x" for x in col) for col in zip(*board)):
                    return board
        return

    nums = list(map(int, next(data).split(",")))
    n_boards = int((n_lines - 1) / 6)
    boards = [[["x" for _ in range(5)] for _ in range(5)] for _ in range(n_boards)]

    num_map = defaultdict(list)
    for i in range(n_boards):
        _ = next(data)
        for j in range(5):
            row = list(map(int, next(data).split()))
            for k, n in enumerate(row):
                num_map[n].append((i, j, k))

    for num in reversed(nums):
        for loc in num_map[num]:
            i, j, k = loc
            boards[i][j][k] = num
        unwin = check_unwin(boards)
        if unwin:
            for loc in num_map[num]:
                i, j, k = loc
                boards[i][j][k] = "x"
            unmarked = [i for row in unwin for i in row if i != "x"]
            return sum(unmarked) * num
    return


start = perf_counter()

s1 = solve_part1()
print("Solution 1:", s1)

s2 = solve_part2()
print("Solution 2:", s2)

print("Execution took", perf_counter() - start, "s")
