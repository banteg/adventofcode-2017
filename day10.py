import aoc


@aoc.test({'3, 4, 1, 5': 12})
def part_1(data: aoc.Data):
    rope_length = 5 if data.is_example else 256
    rope = list(range(rope_length))
    lengths = data.ints_lines[0]
    skip = 0
    pos = 0
    for length in lengths:
        if length > len(rope):
            continue
        rope = rope[pos % len(rope):] + rope[:pos % len(rope)]
        knot = list(reversed(rope[:length]))
        rope = knot + rope[length:]
        rope = rope[-pos % len(rope):] + rope[:-pos % len(rope)]
        pos += length + skip
        skip += 1
    return rope[0] * rope[1]
