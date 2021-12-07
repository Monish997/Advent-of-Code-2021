from io import StringIO
import sys
from time import perf_counter
from os.path import basename
from collections import defaultdict

input = lambda: sys.stdin.readline()
print = lambda *args: sys.stdout.write(" ".join(map(str, args)) + "\n")


def set_stdin():
    program_name = basename(__file__).rstrip(".py")
    with open(f"./input/{program_name}.in") as f:
        lines = f.readlines()
        sys.stdin = StringIO("".join(lines))
    return len(lines)


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

    n_lines = set_stdin()
    nums = list(map(int, input().split(",")))
    n_boards = int((n_lines - 1) / 6)
    boards = []
    num_map = defaultdict(list)
    for i in range(n_boards):
        _ = input()
        board = []
        for j in range(5):
            row = list(map(int, input().split()))
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

    n_lines = set_stdin()
    nums = list(map(int, input().split(",")))
    n_boards = int((n_lines - 1) / 6)
    boards = [[["x" for _ in range(5)] for _ in range(5)] for _ in range(n_boards)]

    num_map = defaultdict(list)
    for i in range(n_boards):
        _ = input()
        for j in range(5):
            row = list(map(int, input().split()))
            for k, n in enumerate(row):
                num_map[n].append((i, j, k))

    for num in reversed(nums):
        for loc in num_map[num]:
            i, j, k = loc
            boards[i][j][k] = num
        unwin = check_unwin(boards)
        if unwin:
            print(unwin, num)
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
