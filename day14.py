from itertools import product
from collections import deque

import aoc
from day10 import knot_hash


@aoc.test({'flqrgnkx': 8108})
def part_1(data: aoc.Data):
    data = data.rstrip()
    blocks = ''
    for i in range(128):
        row = knot_hash(f'{data}-{i}')
        blocks += ''.join([bin(int(x, 16))[2:].zfill(4) for x in row])
    return blocks.count('1')


@aoc.test({'flqrgnkx': 1242})
def part_2(data: aoc.Data):
    data = data.rstrip()
    blocks = []
    for i in range(128):
        row = knot_hash(f'{data}-{i}')
        blocks.append(''.join([bin(int(x, 16))[2:].zfill(4) for x in row]))

    processed = set()
    components = []
    for x, y in product(range(128), range(128)):
        if (x, y) in processed or blocks[y][x] == '0':
            continue
        frontier = deque([(x, y)])
        seen = set()
        while frontier:
            x, y = frontier.popleft()
            if (x, y) in seen:
                continue
            seen.add((x, y))
            neighbours = [
                (dx, dy)
                for (dx, dy) in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
                if (dx, dy) not in seen
                and 0 <= dx < 128
                and 0 <= dy < 128
                and blocks[dy][dx] == '1'
            ]
            frontier.extend(neighbours)
        components.append(seen)
        processed.update(seen)

    return len(components)
