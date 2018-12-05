from math import ceil, sqrt
import aoc


def unwind(n):
    n = int(n)
    x = y = ceil(sqrt(n)) // 2
    br = ((2 * x) + 1) ** 2
    step = int(sqrt(br) - 1)
    remaining = br - n
    for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        x += min(remaining, step) * dx
        y += min(remaining, step) * dy
        remaining -= min(remaining, step)
        if remaining == 0:
            return x, y



def neigbours(x, y, coords):
    return sum(
        coords.get((x + dx, y + dy), 0) for dx, dy in
        [(-1, -1), (0, -1), (1, -1),
         (-1, 0), (1, 0),
         (-1, 1), (0, 1), (1, 1)]
    )


@aoc.test({
    '1': 0,
    '12': 3,
    '23': 2,
    '1024': 31,
})
def part_1(data: aoc.Data):
    x, y = unwind(data)
    return abs(x) + abs(y)


@aoc.test({})
def part_2(data: aoc.Data):
    coords = {(0, 0): 1}
    cursor = 1
    while True:
        cursor += 1
        x, y = unwind(cursor)
        num = neigbours(x, y, coords)
        coords[(x, y)] = num
        if num > int(data):
            return num
            break
