from tqdm import trange
import aoc

example = '''
    Generator A starts with 65
    Generator B starts with 8921
    '''


def generator(value, kind, part=1):
    factor = 16807 if kind == 'a' else 48271
    multiple = 4 if kind == 'a' else 8
    while True:
        value = value * factor % 2147483647
        if part == 1 or value % multiple == 0:
            yield value


def judge(a, b, part=1):
    mod = 2 ** 16
    consider = 40_000_000 if part == 1 else 5_000_000
    total = 0
    for i in trange(consider):
        if next(a) % mod == next(b) % mod:
            total += 1
    return total


@aoc.test({example: 588})
def part_1(data: aoc.Data):
    val_a, val_b = [x[0] for x in data.ints_lines]
    a = generator(val_a, 'a')
    b = generator(val_b, 'b')
    return judge(a, b)


@aoc.test({example: 309})
def part_2(data: aoc.Data):
    val_a, val_b = [x[0] for x in data.ints_lines]
    a = generator(val_a, 'a', part=2)
    b = generator(val_b, 'b', part=2)
    return judge(a, b, part=2)
