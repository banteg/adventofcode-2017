import aoc
import re
from statistics import median
from collections import Counter


example = '''
    pbga (66)
    xhth (57)
    ebii (61)
    havc (66)
    ktlj (57)
    fwft (72) -> ktlj, cntj, xhth
    qoyq (66)
    padx (45) -> pbga, havc, qoyq
    tknk (41) -> ugml, padx, fwft
    jptl (61)
    ugml (68) -> gyxo, ebii, jptl
    gyxo (61)
    cntj (57)
    '''


def load_programs(data):
    weights = {}
    children = {}
    for line in data.splitlines():
        program, _, others = line.partition(' -> ')
        program, weight = re.search(r'(.*) \((\d+)\)', program).groups()
        weights[program] = int(weight)
        if others:
            children[program] = others.split(', ')
    return weights, children


def find_bottom_program(weights, children):
    for program in children:
        seen = set()
        todo = {program}
        while todo:
            i = todo.pop()
            seen.add(i)
            if i in children:
                todo.update(children[i])
        if len(seen) == len(weights):
            return program


def get_total_weight(program, weights, children):
    seen = set()
    todo = {program}
    while todo:
        i = todo.pop()
        seen.add(i)
        if i in children:
            todo.update(children[i])
    return sum(weights[i] for i in seen)


@aoc.test({example: 'tknk'})
def part_1(data: aoc.Data):
    weights, children = load_programs(data)
    return find_bottom_program(weights, children)


@aoc.test({example: 60})
def part_2(data: aoc.Data):
    weights, children = load_programs(data)
    todo = {find_bottom_program(weights, children)}
    while todo:
        i = todo.pop()
        if i in children:
            ws = {c: get_total_weight(c, weights, children) for c in children[i]}
            mid = median(ws.values())
            for u in {x for x in ws if ws[x] != mid}:
                unbalanced = weights[u] - ws[u] + mid
            todo.update(children[i])
    return unbalanced
