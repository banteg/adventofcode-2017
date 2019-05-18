import aoc
from collections import defaultdict, namedtuple
from operator import gt, ge, lt, le, eq, ne, add, sub


example = '''
    b inc 5 if a > 1
    a inc 1 if b < 5
    c dec -10 if a >= 1
    c inc -20 if c == 10
    '''


def maybe_int(s):
    try:
        return int(s)
    except ValueError:
        return s


def load_instructions(data):
    Instruction = namedtuple('Instruction', ['reg', 'op', 'v', 'x', 'a', 'cond', 'b'])
    return [Instruction(*[maybe_int(x) for x in row.split()]) for row in data.splitlines()]


def run_program(instructions):
    conds = {'>': gt, '>=': ge, '<': lt, '<=': le, '==': eq, '!=': ne}
    ops = {'inc': add, 'dec': sub}
    registers = defaultdict(int)

    def pointer(x):
        return x if isinstance(x, int) else registers[x]

    high = 0
    for i in instructions:
        a, b, v = pointer(i.a), pointer(i.b), pointer(i.v)
        if conds[i.cond](a, b):
            registers[i.reg] = ops[i.op](registers[i.reg], v)
        high = max([high] + list(registers.values()))
    return registers, high


@aoc.test({example: 1})
def part_1(data: aoc.Data):
    instructions = load_instructions(data)
    result, _ = run_program(instructions)
    return max(result.values())


@aoc.test({example: 10})
def part_2(data: aoc.Data):
    instructions = load_instructions(data)
    _, high = run_program(instructions)
    return high
