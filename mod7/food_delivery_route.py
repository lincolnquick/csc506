from graph import Graph
from dijkstra import dijkstra
from traffic import update_traffic

def create_state_college_graph():
    graph = Graph()

    # Define streets (edges) connecting intersections
    # E/W Streets
    graph.add_edge("S Atherton & E College", "S Pugh & E College", "E College Ave", 3)
    graph.add_edge("S Pugh & E College", "S Fraser & E College", "E College Ave", 3)
    graph.add_edge("S Fraser & E College", "S Garner & E College", "E College Ave", 3)
    graph.add_edge("S Garner & E College", "S Gill & E College", "E College Ave", 3)

    graph.add_edge("S Atherton & W College", "S Burrowes & W College", "W College Ave", 2)
    graph.add_edge("S Burrowes & W College", "S Barnard & W College", "W College Ave", 2)
    graph.add_edge("S Barnard & W College", "McCormick & W College", "W College Ave", 2)

    graph.add_edge("S Atherton & W Beaver", "S Burrowes & W Beaver", "W Beaver Ave", 2)
    graph.add_edge("S Burrowes & W Beaver", "S Barnard & W Beaver", "W Beaver Ave", 2)
    graph.add_edge("S Barnard & W Beaver", "McCormick & W Beaver", "W Beaver Ave", 2)

    graph.add_edge("S Atherton & W Nittany", "S Burrowes & W Nittany", "W Nittany Ave", 2)
    graph.add_edge("S Burrowes & W Nittany", "S Barnard & W Nittany", "W Nittany Ave", 2)
    graph.add_edge("S Barnard & W Nittany", "McCormick & W Nittany", "W Nittany Ave", 2)

    graph.add_edge("S Atherton & Hamilton", "S Pugh & E Hamilton", "Hamilton Ave", 3)
    graph.add_edge("S Pugh & E Hamilton", "S Fraser & E Hamilton", "Hamilton Ave", 3)
    graph.add_edge("S Fraser & E Hamilton", "S Garner & E Hamilton", "Hamilton Ave", 3)
    graph.add_edge("S Garner & E Hamilton", "S Gill & E Hamilton", "Hamilton Ave", 3)

    # N/S Streets
    graph.add_edge("S Atherton & E College", "S Atherton & W College", "S Atherton St", 5)
    graph.add_edge("S Atherton & W College", "S Atherton & W Beaver", "S Atherton St", 5)
    graph.add_edge("S Atherton & W Beaver", "S Atherton & W Nittany", "S Atherton St", 5)
    graph.add_edge("S Atherton & W Nittany", "S Atherton & Hamilton", "S Atherton St", 5)

    graph.add_edge("S Pugh & E College", "S Pugh & E Beaver", "S Pugh St", 2)
    graph.add_edge("S Pugh & E Beaver", "S Pugh & E Hamilton", "S Pugh St", 2)

    graph.add_edge("S Fraser & E College", "S Fraser & W Beaver", "S Fraser St", 2)
    graph.add_edge("S Fraser & W Beaver", "S Fraser & W Nittany", "S Fraser St", 2)

    graph.add_edge("S Garner & E College", "S Garner & E Beaver", "S Garner St", 2)
    graph.add_edge("S Garner & E Beaver", "S Garner & E Hamilton", "S Garner St", 2)

    graph.add_edge("S Gill & E College", "S Gill & E Beaver", "S Gill St", 2)
    graph.add_edge("S Gill & E Beaver", "S Gill & E Hamilton", "S Gill St", 2)

    return graph

def display_route(graph, path, distance):
    """
    Displays the shortest path with street names and travel times.
    """
    print("\nOptimized Delivery Route:")
    for i in range(len(path) - 1):
        from_node = path[i]
        to_node = path[i + 1]
        for neighbor, street, weight in graph.adjacency_list[from_node]:
            if neighbor == to_node:
                print(f"  {from_node} ➝ {to_node} ({street}, {weight:.2f} minutes)")
                break
    print(f"Total Estimated Travel Time: {distance:.2f} minutes\n")

def main():
    print("Optimizing Food Delivery Routes in State College, PA\n")

    # Create graph for State College
    graph = create_state_college_graph()

    # Define start and end locations
    source = "McCormick & W College"
    destination = "S Gill & E Hamilton"

    # Check if the destination exists
    if destination not in graph.adjacency_list:
        print(f"Error: The destination {destination} does not exist in the graph.")
        return

    # Find shortest path using Dijkstra’s Algorithm (before traffic update)
    shortest_distance, shortest_path = dijkstra(graph, source, destination)
    print("\n=== Shortest Route BEFORE Traffic Update ===")
    display_route(graph, shortest_path, shortest_distance)

    # Apply real-time traffic updates
    update_traffic(graph)

    # Recalculate shortest path after traffic update
    shortest_distance, shortest_path = dijkstra(graph, source, destination)
    print("\n=== Shortest Route AFTER Traffic Update ===")
    display_route(graph, shortest_path, shortest_distance)

if __name__ == "__main__":
    main()