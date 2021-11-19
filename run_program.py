import os

from dataset_handler import DatasetHandler


def run_single_dataset(dataset_path: str, name: str):
    output_folder = os.path.join(os.getcwd(), "out")
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    dataset = os.path.join(dataset_path, name)
    with open(os.path.join(output_folder, "".join(name.split('.')[:-1]) + ".out"), 'w') as out_file:
        data_handler = DatasetHandler(dataset)
        graph, terminals = data_handler.handle()
        steiner = graph.minimum_steiner_tree()
        out_file.write(f"Cost {steiner.show_cost()}\n")
        edge_len = len(steiner.edges)
        out_file.write(f"Edges {edge_len}\n")
        for i in range(edge_len):
            out_file.write(f"E {steiner.edges[i].u + 1} {steiner.edges[i].v + 1}\n")


def run_whole_dataset(dataset_path: str):
    for dataset in os.listdir(dataset_path):
        run_single_dataset(dataset_path, dataset)
