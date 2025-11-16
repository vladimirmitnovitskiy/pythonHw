from heapq import heappush, heappop
from collections import Counter


class Node:
    def __init__(self, char = None, freq = 0, left = None, right = None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
    

    def __lt__(self, other):
        return self.freq < other.freq
    

def build_huffman_tree(msg: str) -> Node:
    freq = Counter(msg)
    heap = []

    for ch, f in freq.items():
        heappush(heap, Node(ch, f))

    while len(heap) > 1:
        a = heappop(heap)
        b = heappop(heap)
        heappush(heap, Node(None, a.freq + b.freq, a, b))

    return heap[0]


def build_codes(node: Node, prefix = "", table = None):
    if table is None:
        table = {}

    if node.char is not None:
        table[node.char] = prefix or "0"
    else:
        build_codes(node.left, prefix + "0", table)
        build_codes(node.right, prefix + "1", table)

    return table

def encode(msg: str) -> tuple[str, dict[str, str]]:
    tree = build_huffman_tree(msg)
    table = build_codes(tree)
    encoded = "".join(table[ch] for ch in msg)
    return encoded, table


def decode(encoded: str, table: dict[str, str]) -> str:
    rev = {v: k for k, v in table.items()}
    result = []
    buf = ""

    for bit in encoded:
        buf += bit
        if buf in rev:
            result.append(rev[buf])
            buf = ""

    return "".join(result)