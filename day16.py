from collections import deque
from string import ascii_lowercase

import aoc


@aoc.test({'s1,x3/4,pe/b': 'baedc'})
def part_1(data: aoc.Data):
    size = 5 if data.is_example else 16
    programs = deque(ascii_lowercase[:size])
    for act in data.split(','):
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
    return ''.join(programs)
