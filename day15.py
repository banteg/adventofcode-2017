import aoc

example = '''
    Generator A starts with 65
    Generator B starts with 8921
    '''


def judge(a, b):
    mod = 2 ** 16
    total = 0
    for i in range(40_000_000):
        a = a * 16807 % 2147483647
        b = b * 48271 % 2147483647
        if a % mod == b % mod:
            total += 1
    return total


@aoc.test({example: 588})
def part_1(data: aoc.Data):
    a, b = [x[0] for x in data.ints_lines]
    return judge(a, b)
