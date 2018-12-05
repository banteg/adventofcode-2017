import aoc


@aoc.test({
'''aa bb cc dd ee
aa bb cc dd aa
aa bb cc dd aaa''': 2
})
def part_1(data: aoc.Data):
    return len([
        x for x in data.splitlines()
        if len(x.split()) == len(set(x.split()))
    ])


@aoc.test({
'''abcde fghij
abcde xyz ecdab
a ab abc abd abf abj
iiii oiii ooii oooi oooo
oiii ioii iioi iiio''': 3
})
def part_2(data: aoc.Data):
    return len([
        x for x in data.splitlines()
        if len(x.split()) == len([
            w for w in x.split()
            if ''.join(sorted(w)) not in {''.join(sorted(w2)) for w2 in set(x.split()) - {w}}
        ])
    ])
