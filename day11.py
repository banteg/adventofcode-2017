import aoc
from dataclasses import dataclass


@dataclass
class Cube:
    x: int = 0
    y: int = 0
    z: int = 0

    def __add__(self, other):
        return Cube(self.x + other.x, self.y + other.y, self.z + other.z)

    def distance(self):
        return max(abs(self.x), abs(self.y), abs(self.z))


directions = {
    'n':  Cube(0, 1, -1),
    'ne': Cube(1, 0, -1),
    'se': Cube(1, -1, 0),
    's':  Cube(0, -1, 1),
    'sw': Cube(-1, 0, 1),
    'nw': Cube(-1, 1, 0),
}


@aoc.test({
    'ne,ne,ne': 3,
    'ne,ne,sw,sw': 0,
    'ne,ne,s,s': 2,
    'se,sw,se,sw,sw': 3,
})
def part_1(data: aoc.Data):
    steps = data.split(',')
    pos = Coord(0, 0, 0)
    for step in steps:
        pos += directions[step]
    return pos.distance()


@aoc.test({})
def part_2(data: aoc.Data):
    steps = data.split(',')
    pos = Coord(0, 0, 0)
    furthest = 0
    for step in steps:
        pos += directions[step]
        furthest = max(furthest, pos.distance())
    return furthest
