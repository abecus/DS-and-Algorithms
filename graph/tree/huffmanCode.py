import itertools
import math
import heapq
import collections
from typing import Dict, Tuple, List


class Node:
    def __init__(self, frequency: int, character: str):
        self.character = character
        self.left = None
        self.right = None
        self.frequency = frequency

    def __eq__(self, other):
        return other != None and other.frequency == self.frequency

    def __lt__(self, other):
        return other != None and other.frequency > self.frequency


def generate_tree(s: str) -> Node:
    # returns root node of tree

    arr = [Node(v, k) for k, v in collections.Counter(s).items()]
    heapq.heapify(arr)

    while len(arr) > 1:
        n1 = heapq.heappop(arr)
        n2 = heapq.heappop(arr)
        new_node = Node(n1.frequency + n2.frequency, '#')
        new_node.left = n1
        new_node.right = n2
        heapq.heappush(arr, new_node)

    root = arr[0]
    if root.character != '#':
        # if there is only one character in string
        # then make a root on top of it
        tmp = Node(1, '#')
        tmp.right = root
        root = tmp

    return root


def get_codes(s: str) -> Tuple[Node, Dict[str, int]]:
    # returns encoding for each character in string

    if not s:
        return Node(0, ''), {}

    def encoder(root, path) -> None:
        # code generator by following edges of tree
        nonlocal codes

        if root.character != '#':
            codes[root.character] = path
            return

        if root.left:
            encoder(root.left, path+"0")
        if root.right:
            encoder(root.right, path+"1")

    root = generate_tree(s)
    codes = {}
    encoder(root, "")

    return root, codes


def encode(s):
    root, codes = get_codes(s)
    print(codes)
    res = ''
    for i in s:
        res += codes[i]
    return root, res


def decode(root: Node, s: str) -> str:

    def foo(i, node, root):
        nonlocal res

        if node.character != '#':
            res += node.character
            return foo(i, root, root)
        if i == len(s):
            return
        elif s[i] == '0':
            return foo(i+1, node.left, root)
        elif s[i] == '1':
            return foo(i+1, node.right, root)

    res = ''
    foo(0, root, root)
    return res


if __name__ == "__main__":
    s = "{'b': '00', 'e': '01', 'a': '10', 'c': '110', 'd': '111'}"
    root, compressed_string = encode(s)
    print(s)
    print(compressed_string)
    print(decode(root, compressed_string))
