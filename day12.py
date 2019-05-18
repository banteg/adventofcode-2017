import networkx as nx

import aoc

example = '''
    0 <-> 2
    1 <-> 1
    2 <-> 0, 3, 4
    3 <-> 2, 4
    4 <-> 2, 3, 6
    5 <-> 6
    6 <-> 4, 5
    '''


@aoc.test({example: 6})
def part_1(data: aoc.Data):
    G = nx.Graph()
    for node, *edges in data.ints_lines:
        G.add_edges_from((node, edge) for edge in edges)
    for component in nx.connected_components(G):
        if 0 in component:
            nx.nx_agraph.write_dot(G.subgraph(component), 'pipes_zero.dot')
            return len(component)


@aoc.test({example: 2})
def part_2(data: aoc.Data):
    G = nx.Graph()
    for node, *edges in data.ints_lines:
        G.add_edges_from((node, edge) for edge in edges)
    return len(list(nx.connected_components(G)))
