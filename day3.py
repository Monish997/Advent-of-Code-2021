from io import StringIO
import sys
from time import perf_counter
from os.path import basename
from collections import Counter

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
    bits = [[] for _ in range(12)]
    for _ in range(n_lines):
        line = input().strip()
        for i in range(12):
            bits[i].append(int(line[i]))
    gamma_bits = [Counter(bits[i]).most_common(1)[0][0] for i in range(12)]
    epsilon_bits = [1 - gamma_bits[i] for i in range(12)]

    gamma = int("".join(map(str, gamma_bits)), 2)
    epsilon = int("".join(map(str, epsilon_bits)), 2)
    return gamma * epsilon


def solve_part2():
    def filter_entries(arr, i, ref):
        j = 0
        while j < len(arr[i]):
            if arr[i][j] != ref:
                for k in range(12):
                    del arr[k][j]
            else:
                j += 1

    n_lines = set_stdin()
    bits = [[] for _ in range(12)]
    for _ in range(n_lines):
        line = input().strip()
        for i in range(12):
            bits[i].append(int(line[i]))

    o2_list = [i.copy() for i in bits]
    co2_list = [i.copy() for i in bits]

    for i in range(12):
        common = Counter(o2_list[i]).most_common(2)
        mcb = 1 if common[0][1] == common[1][1] else common[0][0]

        filter_entries(o2_list, i, mcb)
        if len(o2_list[i]) == 1:
            break

    for i in range(12):
        common = Counter(co2_list[i]).most_common(2)
        lcb = 0 if common[0][1] == common[1][1] else common[1][0]

        filter_entries(co2_list, i, lcb)
        if len(co2_list[i]) == 1:
            break

    o2_rate = int("".join(map(lambda x: str(x[0]), o2_list)), 2)
    co2_rate = int("".join(map(lambda x: str(x[0]), co2_list)), 2)

    return o2_rate * co2_rate


start = perf_counter()

s1 = solve_part1()
print("Solution 1:", s1)

s2 = solve_part2()
print("Solution 2:", s2)

print("Execution took", perf_counter() - start, "s")
