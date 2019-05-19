from itertools import cycle
import aoc


def scanner(r):
    scan = list(range(r))
    return cycle(scan + scan[-2:0:-1])


@aoc.test({
    '''
    0: 3
    1: 2
    4: 4
    6: 4
    ''': 24
})
def part_1(data: aoc.Data):
    layers = dict(data.ints_lines)
    scanners = {depth: scanner(layers[depth]) for depth in layers}
    severity = 0
    for i in range(max(layers) + 1):
        for depth in scanners:
            scan = next(scanners[depth])
            if depth == i and scan == 0:
                severity += depth * layers[depth]
    return severity
