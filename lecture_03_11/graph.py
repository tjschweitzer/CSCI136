import collections
from abc import abstractmethod, ABC


class _Node:
    def __init__(self, label, children):
        self.label = label
        self.children = children


class _Tree:
    def __init__(self, root):
        self.root = root


class Collection(ABC):
    @abstractmethod
    def add(self, other):
        pass

    @abstractmethod
    def remove(self):
        pass

    @abstractmethod
    def __len__(self):
        pass


class Queue(Collection):
    def __init__(self) -> None:
        self.deque = collections.deque()

    def add(self, thing):
        self.deque.appendleft(thing)

    def remove(self):
        return self.deque.pop()

    def __len__(self):
        return len(self.deque)


class Stack(Collection):
    def __init__(self) -> None:
        self.deque = collections.deque()

    def add(self, thing):
        self.deque.append(thing)

    def remove(self):
        return self.deque.pop()

    def __len__(self):
        return len(self.deque)


def traverse(graph, collection):
    collection.add(graph.root)

    while len(collection) > 0:
        node = collection.remove()
        print(f"Visiting {node.label}")
        for c in node.children:
            collection.add(c)


# Graph structure:
#         M
#        / \
#       F   P
#      /\    \
#     C  J    X
#      \  \
#       D  K

a_graph = _Tree(_Node('M',
                      [
                        _Node('F',
                              [_Node('C', [
                                  _Node('D', [])
                              ]),
                               _Node('J', [
                                   _Node('K', [])
                               ])]),
                        _Node('P',
                              [_Node('X', [])
                               ])
                    ]))

print("With a queue:")
traverse(a_graph, Queue())

print("With a stack:")
traverse(a_graph, Stack())


def dfs_recursion(graph):
    dfs_recursion_node(graph.root)


def dfs_recursion_node(node):
    print(f"Visiting {node.label}")
    for c in node.children:
        dfs_recursion_node(c)


print("DFS with recursion")
dfs_recursion(a_graph)