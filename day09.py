import aoc


def process_stream(data, part=1):
    groups = []
    garbage = []
    collected = []
    score = 0
    ignore = False
    for char in data:
        if ignore:
            ignore = False
            continue
        if char == '!':
            ignore = True
            continue
        if not garbage:
            if char == '<':
                garbage.append(char)
            if char == '{':
                groups.append(len(groups) + 1)
            if char == '}':
                score += groups.pop()
        else:
            if char == '>':
                garbage.pop()
            else:
                collected.append(char)
    return {1: score, 2: len(collected)}[part]


@aoc.test({
    r'{}': 1,
    r'{{{}}}': 6,
    r'{{},{}}': 5,
    r'{{{},{},{{}}}}': 16,
    r'{<a>,<a>,<a>,<a>}': 1,
    r'{{<ab>},{<ab>},{<ab>},{<ab>}}': 9,
    r'{{<!!>},{<!!>},{<!!>},{<!!>}}': 9,
    r'{{<a!>},{<a!>},{<a!>},{<ab>}}': 3,
})
def part_1(data: aoc.Data):
    return process_stream(data, part=1)


@aoc.test({
    r'<>': 0,
    r'<random characters>': 17,
    r'<<<<>': 3,
    r'<{!>}>': 2,
    r'<!!>': 0,
    r'<!!!>>': 0,
    r'<{o"i!a,<{i<a>': 10,
})
def part_2(data: aoc.Data):
    return process_stream(data, part=2)
