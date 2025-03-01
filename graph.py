import heapq

class Graph:
    def __init__(self):
        """Initialize an empty graph with adjacent list representation, ideal for traversing neighbors."""
        self.adjacency_list = {}
        self.base_weight = 1

    def add_edge(self, start, end, weight):
        """Add a directed edge from start to end with a weight."""

        if start not in self.adjacency_list:
            self.adjacency_list[start] = []
        if end not in self.adjacency_list:
            self.adjacency_list[end] = []

        self.adjacency_list[start].append((end, weight))
        self.adjacency_list[end].append((start, weight))

    def get_neighbors(self, node):
        """Return the neighbors of a node."""
        return self.adjacency_list.get(node, [])
    
    def print_graph(self):
        """Print the graph."""
        for node, edges in self.adjacency_list:
            print(f"{node}: {edges}")