import heapq
def dijkstra(graph, start, end):
    """Implements Dijkstra's algorithm to find the shortest path from start to end in a graph."""

    priority_queue = [(0, start, [])]
    visited = set()

    while priority_queue:
        current_distance, current_node, path = heapq.heappop(priority_queue)

        if current_node in visited:
            continue
        visited.add(current_node)

        path = path + [current_node]
        
        if current_node == end:
            return current_distance, path
        
        for neighbor, weight in graph.get_neighbors(current_node):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (current_distance + weight, neighbor, path))

    return float("inf"), [] # If there is no path from start to end, return infinity and an empty path.