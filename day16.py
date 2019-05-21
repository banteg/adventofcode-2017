from collections import deque
from string import ascii_lowercase

import aoc


def dance(programs, actions):
    for act in actions:
        action, args = act[0], act[1:].split('/')
        if action == 's':
            a = int(args[0])
            [programs.appendleft(programs.pop()) for i in range(a)]
        elif action == 'x':
            a, b = map(int, args)
            programs[a], programs[b] = programs[b], programs[a]
        elif action == 'p':
            a = programs.index(args[0])
            b = programs.index(args[1])
            programs[a], programs[b] = programs[b], programs[a]
    return programs


@aoc.test({'s1,x3/4,pe/b': 'baedc'})
def part_1(data: aoc.Data):
    size = 5 if data.is_example else 16
    actions = data.split(',')
    programs = deque(ascii_lowercase[:size])
    programs = dance(programs, actions)
    return ''.join(programs)


@aoc.test({})
def part_2(data: aoc.Data):
    seen = []
    actions = data.split(',')
    target = 1_000_000_000
    programs = deque(ascii_lowercase[:16])
    for i in range(target):
        programs = dance(programs, actions)
        prog = ''.join(programs)
        if prog in seen:
            return seen[(target - 1) % i]
        seen.append(prog)
