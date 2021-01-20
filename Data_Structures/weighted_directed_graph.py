class Node:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


class Edge:
    def __init__(self, src, dst, weight):
        self.src = src
        self.dst = dst
        self.weight = weight


class Graph:
    def __init__(self, edges, verts):
        self.adj_list = [None] * verts

        for i in range(verts):
            self.adj_list[i] = []

        for edge in edges:
            node = Node(edge.dst, edge.weight)
            self.adj_list[edge.src].append(node)


def print_graph(graph):
    for src in range(len(graph.adj_list)):
        for edge in graph.adj_list[src]:
            print(f"({src} -> {edge.value}, {edge.weight})\n", end="")


if __name__ == '__main__':
    edges = [Edge(0, 1, 3), Edge(0, 2, 3), Edge(1, 2, 5), Edge(2, 3, 4),
             Edge(2, 4, 8), Edge(4, 3, 6), Edge(4, 5, 7), Edge(5, 0, 10)]

    nodes = 6

    graph = Graph(edges, nodes)

    print_graph(graph)
