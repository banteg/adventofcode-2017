from collections import deque
from itertools import count
import aoc


example = '''
    0: 3
    1: 2
    4: 4
    6: 4
    '''


def scanner(r):
    scan = list(range(r))
    return deque(scan + scan[-2:0:-1])


@aoc.test({example: 24})
def part_1(data: aoc.Data):
    layers = dict(data.ints_lines)
    scanners = {depth: scanner(layers[depth]) for depth in layers}
    severity = 0
    for depth in range(max(layers) + 1):
        scans = {i: scanners[i][0] for i in scanners}
        [scanners[i].rotate(-1) for i in scanners]
        if scans.get(depth) == 0:
            severity += depth * layers[depth]
    return severity


@aoc.test({example: 10})
def part_2(data: aoc.Data):
    layers = dict(data.ints_lines)
    scanners = {i: layers[i] + max(layers[i] - 2, 0) for i in layers}
    for delay in count():
        # detect which scanners are at the top at delay picoseconds
        if any((i + delay) % scanners[i] == 0 for i in scanners):
            continue
        return delay
