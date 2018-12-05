import aoc
from itertools import count


def reallocate_memory(memory):
    seen = {}
    for cycles in count():
        if tuple(memory) in seen:
            return cycles, cycles - seen[tuple(memory)]
        seen[tuple(memory)] = cycles
        blocks, bank = max((blocks, -bank) for bank, blocks in enumerate(memory))
        bank = -bank
        memory[bank] = 0
        for pos in range(bank + 1, bank + blocks + 1):
            memory[pos % len(memory)] += 1


@aoc.test({'0 2 7 0': 5})
def part_1(data: aoc.Data):
    return reallocate_memory(data.ints_lines[0])[0]


@aoc.test({'0 2 7 0': 4})
def part_2(data: aoc.Data):
    return reallocate_memory(data.ints_lines[0])[1]
