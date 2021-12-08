from io import StringIO
import sys
from time import perf_counter
from os.path import basename

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
    count = 0
    for i in range(n_lines):
        _, out_digits = [i.split(" ") for i in input().split(" | ")]
        for digit in out_digits:
            if len(digit) in (2, 4, 3, 7):
                count += 1
    return count


def solve_part2():
    n_lines = set_stdin()
    sum_ = 0
    for i in range(n_lines):
        maps = [set() for _ in range(10)]
        signals, out_digits = [list(map(set, i.split(" "))) for i in input().split(" | ")]
        for s in signals:
            if len(s) == 2:
                maps[1] = s
            elif len(s) == 4:
                maps[4] = s
            elif len(s) == 3:
                maps[7] = s
            elif len(s) == 7:
                maps[8] = s
        for s in signals:
            if len(s) == 5:
                if len(s.intersection(maps[1])) == 2:
                    maps[3] = s
                elif len(s.intersection(maps[4])) == 3:
                    maps[5] = s
                else:
                    maps[2] = s
            elif len(s) == 6:
                if len(s.intersection(maps[4])) == 4:
                    maps[9] = s
                elif len(s.intersection(maps[1])) == 2:
                    maps[0] = s
                else:
                    maps[6] = s
        digits = []
        for d in out_digits:
            digits.append(maps.index(d))
        sum_ += int("".join(map(str, digits)))

    return sum_


start = perf_counter()

s1 = solve_part1()
print("Solution 1:", s1)

s2 = solve_part2()
print("Solution 2:", s2)

print("Execution took", perf_counter() - start, "s")
