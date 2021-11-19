from steiner_tree import SteinerTree


class DatasetHandler:
    def __init__(self, file_name):
        self.file_name = file_name

    def handle(self):
        file = open(self.file_name, "r")
        file.readline()
        section = list(file.readline().split())[1]
        graph = None
        terminals = []
        if section == "Comment":
            line = file.readline().rstrip('\n')
            while line != "End":
                line = file.readline().rstrip('\n')
            line = file.readline().rstrip('\n')
            while line == "":
                line = file.readline().rstrip('\n')
            section = list(line.split())[1]
        if section == "Graph":
            nv = int(file.readline().rstrip('\n').split()[1])
            ne = int(file.readline().rstrip('\n').split()[1])
            graph = SteinerTree(nv, [])
            for i in range(ne):
                u, v, w = map(int, file.readline().rstrip('\n').split()[1:])
                graph.add_edge(u - 1, v - 1, w)
            line = file.readline().rstrip('\n')
            while line == "" or line == "End":
                line = file.readline().rstrip('\n')
            section = list(line.split())[1]
        if section == "Terminals":
            nt = int(file.readline().rstrip('\n').split()[1])
            for i in range(nt):
                terminals.append(int(file.readline().rstrip('\n').split()[1]) - 1)
            graph.terminals = terminals
        file.close()
        return graph, terminals
