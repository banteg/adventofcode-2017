from itertools import permutations
import aoc


@aoc.test({
'''5 1 9 5
7 5 3
2 4 6 8''': 18
})
def part_1(data: aoc.Data):
    return sum(max(row) - min(row) for row in data.ints_lines)


@aoc.test({
'''5 9 2 8
9 4 7 3
3 8 6 5''': 9
})
def part_2(data: aoc.Data):
    return sum(a // b for row in data.ints_lines for a, b in permutations(row, 2) if a % b == 0)
