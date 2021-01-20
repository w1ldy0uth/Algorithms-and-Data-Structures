# this graph implementation is based on weighted directed graph,
# that's why the code looks so familiar

class Edge:
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst


class Graph:
    def __init__(self, edges, verts):
        self.adj_list = [[] for i in range(verts)]

        for edge in edges:
            self.adj_list[edge.src].append(edge.dst)


def print_graph(graph):
    for src in range(len(graph.adj_list)):
        for dst in graph.adj_list[src]:
            print(f"({src} -> {dst})\n", end="")


if __name__ == '__main__':
    edges = [Edge(0, 1), Edge(0, 2), Edge(1, 2), Edge(2, 3),
             Edge(2, 4), Edge(4, 3), Edge(4, 5), Edge(5, 0)]

    nodes = 6

    graph = Graph(edges, nodes)

    print_graph(graph)
