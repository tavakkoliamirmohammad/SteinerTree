from typing import List

from graph import Graph


class SteinerTree(Graph):
    def __init__(self, vertices: int, terminals: List[int]):
        Graph.__init__(self, vertices)
        self.terminals: List[int] = terminals

    def minimum_steiner_tree(self):
        # first find minimum spanning tree
        spanning_tree: Graph = self.minimum_spanning_tree()
        print(spanning_tree.show_cost())
        temp = []
        for i in range(len(self.terminals)):
            for j in range(i, len(self.terminals)):
                temp += spanning_tree.find_cost_efficient_path(self.terminals[i], self.terminals[j])[0]
        steiner_edge = set(temp)
        steiner = Graph(self.vertices)
        for e in steiner_edge:
            if e is not None:
                steiner.add_edge(e.u, e.v, e.w)
        print(steiner.show_cost())
        return steiner


