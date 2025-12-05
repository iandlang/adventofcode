from collections import deque
import matplotlib.pyplot as plt
from typing import Dict, Tuple
import networkx as nx
from decorators.timer import timer

def load_data(file: str) -> dict:
    bits = {}
    ops = deque([])
    bop = {'AND': '&', 'OR': '|', 'XOR': '^'}
    twisted_wires = {
        'z11': 'vkq',
        'vkq': 'z11',
        'z24': 'mmk',
        'mmk': 'z24',
        'pvb': 'qdq',
        'qdq': 'pvb',
        'z38': 'hqh',
        'hqh': 'z38'
    }

    with open(file) as f:
        for line in f:
            line = line.strip()

            if ":" in line:
                gate, bit = line.split(": ")
                bits[gate] = int(bit)

            if "->" in line:
                (bit1, op, bit2, eq, bit3) = line.split(" ")
                bit3 = twisted_wires.get(bit3, bit3)
                ops.append((bit1, bop[op], bit2, eq, bit3))

    return {'bits': bits, 'ops': ops}


def solve(data: dict) -> str:
    bits = data['bits']
    ops = data['ops']

    G = nx.DiGraph()

    # add x/y/z nodes in order, helps with the graph rendering
    for i in range(45):
        G.add_node(f"x{str(i).zfill(2)}")
        G.add_node(f"y{str(i).zfill(2)}")
        G.add_node(f"z{str(i).zfill(2)}")
    G.add_node('z45')

    # add the edges
    for (bit1,op,bit2,eq,bit3) in ops:
        G.add_edge(bit1,bit3,op=op)
        G.add_edge(bit2,bit3,op=op)

    # calc the gate output values.  Recursion would prob be quicker
    while ops:
        (bit1,op,bit2,eq,bit3) = ops.popleft()
        if bit1 in bits and bit2 in bits:
            bits[bit3] = eval(f"bits['{bit1}'] {op} bits['{bit2}']")
        else:
            ops.append((bit1,op,bit2,eq,bit3))

    # draw the circuit, and examine for crossed wires
    if False:
        pos = nx.nx_pydot.graphviz_layout(G, prog="dot", root="x00")
        labels = nx.get_edge_attributes(G, 'op')
        nx.draw(G, with_labels=True, pos=pos, node_size=300, font_size=5, node_color='lightblue')
        nx.draw_networkx_edge_labels(G, edge_labels=labels, pos=pos, font_size = 5)
        plt.show()

    xbits = sorted([(k,v) for k,v in bits.items() if k.startswith("x")])
    ybits = sorted([(k,v) for k,v in bits.items() if k.startswith("y")])
    zbits = sorted([(k,v) for k,v in bits.items() if k.startswith("z")])

    x = sum(bit * 2**i for i,(gate,bit) in enumerate(xbits))
    y = sum(bit * 2**i for i,(gate,bit) in enumerate(ybits))
    z = sum(bit * 2**i for i,(gate,bit) in enumerate(zbits))

    assert x + y == z

    result = ','.join(sorted(('vkq', 'z11', 'mmk', 'z24', 'pvb', 'qdq', 'z38', 'hqh')))
    return result


@timer
def main() -> None:
    data = load_data("data.txt")
    result = solve(data)
    print(f"result: {result}")

if __name__ == "__main__":
    main()
