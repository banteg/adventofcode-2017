import aoc


def steps_to_exit(instructions, strange_jumps=False):
    pos = 0
    steps = 0
    while True:
        move = instructions[pos]
        if strange_jumps:
            instructions[pos] += -1 if instructions[pos] >= 3 else 1
        else:
            instructions[pos] += 1
        pos += move
        steps += 1
        if pos < 0 or pos >= len(instructions):
            return steps


@aoc.test({'0\n3\n0\n1\n-3': 5})
def part_1(data: aoc.Data):
    return steps_to_exit(data.int_lines)


@aoc.test({'0\n3\n0\n1\n-3': 10})
def part_2(data: aoc.Data):
    return steps_to_exit(data.int_lines, True)
