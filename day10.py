from io import StringIO
import sys
from time import perf_counter
from os.path import basename
from statistics import median

input = lambda: sys.stdin.readline().rstrip("\n")
print = lambda *args: sys.stdout.write(" ".join(map(str, args)) + "\n")


def set_stdin():
    program_name = basename(__file__).rstrip(".py")
    with open(f"./input/{program_name}.in") as f:
        lines = f.readlines()
        sys.stdin = StringIO("".join(lines))
    return len(lines)


def solve_part1():
    n_lines = set_stdin()
    open_chars = ["(", "[", "{", "<"]
    close_chars = [")", "]", "}", ">"]
    open2close = dict(zip(open_chars, close_chars))
    score_dict = dict(zip(close_chars, [3, 57, 1197, 25137]))
    score = 0
    for _ in range(n_lines):
        line = input()
        opened = [line[0]]
        for char in line[1:]:
            if char in open_chars:
                opened.append(char)
            elif open2close[opened[-1]] == char:
                opened.pop()
            else:
                score += score_dict[char]
                break
    return score


def solve_part2():
    n_lines = set_stdin()
    lines = [input() for _ in range(n_lines)]
    open_chars = ["(", "[", "{", "<"]
    close_chars = [")", "]", "}", ">"]
    open2close = dict(zip(open_chars, close_chars))
    incomplete = []
    for line in lines:
        opened = [line[0]]
        for char in line[1:]:
            if char in open_chars:
                opened.append(char)
            elif open2close[opened[-1]] == char:
                opened.pop()
            else:
                break
        else:
            rem = map(open2close.get, reversed(opened))
            incomplete.append(rem)

    score_dict = dict(zip(close_chars, [1, 2, 3, 4]))
    scores = []
    for rem in incomplete:
        score = 0
        for char in rem:
            score *= 5
            score += score_dict[char]
        scores.append(score)

    return median(scores)


start = perf_counter()

s1 = solve_part1()
print("Solution 1:", s1)

s2 = solve_part2()
print("Solution 2:", s2)

print("Execution took", perf_counter() - start, "s")
