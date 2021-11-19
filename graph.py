from Edge import Edge
from subset import Subset
from typing import List


class Graph:
    def __init__(self, vertices: int):
        self.vertices = vertices  # number of the vertices
        self.edges: List[Edge] = []  # a list for edges
        self.adjacent_vertices = {v: [] for v in range(self.vertices)}  # a map for adjacent vertices
        self.adjacent_edges: List[List[Edge]] = []  # a list for adjacent edge

        # initialize the adjacent edge list
        for i in range(self.vertices):
            self.adjacent_edges.append([])
            for j in range(self.vertices):
                self.adjacent_edges[i].append(None)

    def add_edge(self, u: int, v: int, w: int):
        # add vertices and edges
        self.add_vertex(u, v)
        self.add_vertex(v, u)
        self.edges.append(Edge(u, v, w))
        self.adjacent_edges[u][v] = self.edges[-1]
        self.adjacent_edges[v][u] = self.edges[-1]

    def insert_edge(self, edge: Edge):
        # add vertices and edges
        u = edge.u
        v = edge.v
        self.add_vertex(u, v)
        self.add_vertex(v, u)
        self.edges.append(edge)
        self.adjacent_edges[u][v] = self.edges[-1]
        self.adjacent_edges[v][u] = self.edges[-1]

    def add_vertex(self, u: int, v: int):
        self.adjacent_vertices[u].append(v)

    def find(self, subsets: List[Subset], i: int):
        # finding using path compression technique
        if subsets[i].parent != i:
            subsets[i].parent = self.find(subsets, subsets[i].parent)
        return subsets[i].parent

    def union(self, subsets: List[Subset], x: int, y: int):
        parent_x = self.find(subsets, x)
        parent_y = self.find(subsets, y)
        # use union by rank technique
        if subsets[parent_x].rank < subsets[parent_y].rank:
            subsets[parent_x].parent = parent_y

        elif subsets[parent_x].rank < subsets[parent_y].rank:
            subsets[parent_y].parent = parent_x
        else:
            subsets[parent_y].parent = parent_x
            subsets[parent_x].rank += 1

    def minimum_spanning_tree(self):
        result: List[Edge] = []
        i = 0
        e = 0
        # sort edges based on weights
        self.edges = sorted(self.edges, key=lambda edge: edge.w)
        # a subset is set in our union-find structure
        subsets: List[Subset] = []
        # add every vertex to a subset
        for v in range(self.vertices):
            subsets.append(Subset(v, 0))

        while e < self.vertices - 1:
            edge = self.edges[i]
            # find parent of x and y
            x = self.find(subsets, edge.u)
            y = self.find(subsets, edge.v)
            i += 1
            # join this two subsets
            if x != y:
                result.append(edge)
                self.union(subsets, x, y)
                e += 1
        graph = Graph(self.vertices)
        for edge in result:
            graph.insert_edge(edge)
        return graph

    def dfs_paths(self, start, goal):
        # this method is only implemented for tree
        stack = [(start, [start], [], 0)]
        ls = []
        # for optimizing the performance
        lsapp = ls.append
        stackapp = stack.append
        while stack:
            # every time pop the top element of the stack and visit the adjacent vertices if not yet seen
            (vertex, path, edges, cost) = stack.pop()
            vs = self.adjacent_vertices[vertex]
            # loop through vertices that wasn't seen
            for next_vertex in set(vs) - set(path):
                next_edge = self.adjacent_edges[vertex][next_vertex]
                if next_vertex == goal:
                    # reached the goal so we have the minimum path
                    lsapp((edges + [next_edge], cost + next_edge.w))
                    return ls[0]
                else:
                    stackapp((next_vertex, path + [next_vertex], edges + [next_edge], cost + next_edge.w))

        return ls

    def find_cost_efficient_path(self, start, goal):
        # find paths using dfs method
        paths = self.dfs_paths(start, goal)
        # return the only minimum path which
        return paths if paths else ([], 0)

    def show_cost(self):
        cost = 0
        for e in self.edges:
            cost += e.w
        return cost
