class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

    def __repr__(self):
        return f"Edge {self.u} -> {self.v}: {self.w}"

    def __hash__(self):
        return hash((self.u, self.v, self.w))

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.u == other.u and self.v == other.v and self.w == other.w