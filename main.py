from dataset_handler import DatasetHandler
from graph import Graph

# g = Graph(4)
# g.add_edge(0, 1, 10)
# g.add_edge(0, 2, 6)
# g.add_edge(0, 3, 5)
# g.add_edge(1, 3, 15)
# g.add_edge(2, 3, 4)
#
# print(g.find_cost_efficient_path(1, 3))
# g.minimum_spanning_tree()

data_handler = DatasetHandler("PUC\\cc3-4u.stp")
graph, terminals = data_handler.handle()
graph.minimum_steiner_tree()

from run_program import run_whole_dataset, run_single_dataset

# run_whole_dataset("PUC")
# run_single_dataset("PUC", "cc3-4p.stp")

