import aoc
from functools import reduce
from operator import xor


def knot_round(lengths, rope=None, skip=0, pos=0, rope_size=256):
    if rope is None:
        rope = list(range(rope_size))
    for length in lengths:
        if length > len(rope):
            continue
        rope = rope[pos % len(rope):] + rope[:pos % len(rope)]
        rope = list(reversed(rope[:length])) + rope[length:]
        rope = rope[-pos % len(rope):] + rope[:-pos % len(rope)]
        pos += length + skip
        skip += 1
    return rope, skip, pos


def knot_hash(text):
    data = [int(x) for x in text.encode('ascii')]
    iv = [17, 31, 73, 47, 23]
    lengths = data + iv
    rope, skip, pos = None, 0, 0
    for _ in range(64):
        rope, skip, pos = knot_round(lengths, rope, skip, pos)
    dense_hash = [reduce(xor, rope[i:i+16]) for i in range(0, 256, 16)]
    return bytes(dense_hash).hex()


@aoc.test({'3, 4, 1, 5': 12})
def part_1(data: aoc.Data):
    rope_size = 5 if data.is_example else 256
    rope, *_ = knot_round(data.ints_lines[0], rope_size=rope_size)
    return rope[0] * rope[1]


@aoc.test({
    '': 'a2582a3a0e66e6e86e3812dcb672a272',
    'AoC 2017': '33efeb34ea91902bb2f59c9920caa6cd',
    '1,2,3': '3efbe78a8d82f29979031a4aa0b16a9d',
    '1,2,4': '63960835bcdc130f0b66d7ff4f6a5a8e',
})
def part_2(data: aoc.Data):
    return knot_hash(data)
