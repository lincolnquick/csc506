class Graph:
    def __init__(self):
        self.adjacency_list = {}  # Stores nodes and their connections
        self.edges = {}  # Stores edges as connections between nodes
        self.base_weight = 1  # Default edge weight

    def add_edge(self, node1, node2, edge_name, weight):
        """
        Adds an edge to the graph.

        :param node1: First node.
        :param node2: Second node.
        :param edge_name: Name of the edge.
        :param weight: Weight of the edge (e.g., travel time).
        """
        if node1 not in self.adjacency_list:
            self.adjacency_list[node1] = []
        if node2 not in self.adjacency_list:
            self.adjacency_list[node2] = []

        # Add connections to adjacency list (bidirectional)
        self.adjacency_list[node1].append((node2, edge_name, weight))
        self.adjacency_list[node2].append((node1, edge_name, weight))

        # Store edges separately
        if edge_name not in self.edges:
            self.edges[edge_name] = []
        self.edges[edge_name].append((node1, node2))

    def get_neighbors(self, node):
        """Returns the neighboring nodes of a given node."""
        return self.adjacency_list.get(node, [])

    def get_edges(self):
        """Returns a list of all unique edges in the graph."""
        return list(self.edges.keys())

    def has_connection(self, edge1, edge2):
        """
        Checks if two edges share a node.
        """
        if edge1 not in self.edges or edge2 not in self.edges:
            return False

        # Get all nodes connected to both edges
        edge1_nodes = set(sum(self.edges[edge1], ()))
        edge2_nodes = set(sum(self.edges[edge2], ()))

        # Find common nodes (shared connection)
        return bool(edge1_nodes & edge2_nodes)  # Returns True if they connect