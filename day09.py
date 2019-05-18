import aoc


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
    groups = []
    garbage = []
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
        elif char == '>':
            garbage.pop()
    return score
