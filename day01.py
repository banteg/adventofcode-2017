import aoc


@aoc.test({
    '1122': 3,
    '1111': 4,
    '1234': 0,
    '91212129': 9,
})
def part_1(data: aoc.Data):
    puzzle = [int(x) for x in data] + [int(data[0])]
    return sum(a for a, b in zip(puzzle, puzzle[1:]) if a == b)


@aoc.test({
    '1212': 6,
    '1221': 0,
    '123425': 4,
    '123123': 12,
    '12131415': 4,
})
def part_2(data: aoc.Data):
    puzzle = [int(x) for x in data]
    return sum(a for i, a in enumerate(puzzle) if a == puzzle[(i + len(puzzle) // 2) % len(puzzle)])
