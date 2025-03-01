from graph import Graph
from dijkstra import dijkstra
from traffic import update_traffic

def create_state_college_graph():
    graph = Graph()

    # Define intersections (nodes) by connecting streets
    intersections = [
        # Main N/S Streets
        "S Atherton & E College", "S Atherton & W College", "S Atherton & W Beaver", "S Atherton & W Nittany", "S Atherton & W Fairmont",
        "S Atherton & W Prospect", "S Atherton & Hamilton",
        "S Pugh & E College", "S Pugh & E Beaver", "S Pugh & E Hamilton",
        "S Burrowes & W College", "S Burrowes & W Beaver", "S Burrowes & W Nittany",
        "S Fraser & E College", "S Fraser & W Beaver", "S Fraser & W Nittany",
        "S Garner & E College", "S Garner & E Beaver", "S Garner & E Hamilton",
        "S Barnard & W College", "S Barnard & W Beaver", "S Barnard & W Nittany",
        "S Gill & E College", "S Gill & E Beaver", "S Gill & E Hamilton",
        "McCormick & W College", "McCormick & W Beaver", "McCormick & W Nittany",
    ]

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

    graph.add_edge("S Atherton & W Fairmont", "S Burrowes & W Fairmont", "W Fairmont Ave", 2)

    graph.add_edge("S Atherton & W Prospect", "S Burrowes & W Prospect", "W Prospect Ave", 2)

    graph.add_edge("S Atherton & Hamilton", "S Pugh & E Hamilton", "Hamilton Ave", 3)
    graph.add_edge("S Pugh & E Hamilton", "S Fraser & E Hamilton", "Hamilton Ave", 3)
    graph.add_edge("S Fraser & E Hamilton", "S Garner & E Hamilton", "Hamilton Ave", 3)
    graph.add_edge("S Garner & E Hamilton", "S Gill & E Hamilton", "Hamilton Ave", 3)

    # N/S Streets
    graph.add_edge("S Atherton & E College", "S Atherton & W College", "S Atherton St", 5)
    graph.add_edge("S Atherton & W College", "S Atherton & W Beaver", "S Atherton St", 5)
    graph.add_edge("S Atherton & W Beaver", "S Atherton & W Nittany", "S Atherton St", 5)
    graph.add_edge("S Atherton & W Nittany", "S Atherton & W Fairmont", "S Atherton St", 5)
    graph.add_edge("S Atherton & W Fairmont", "S Atherton & W Prospect", "S Atherton St", 5)
    graph.add_edge("S Atherton & W Prospect", "S Atherton & Hamilton", "S Atherton St", 5)

    graph.add_edge("S Pugh & E College", "S Pugh & E Beaver", "S Pugh St", 2)
    graph.add_edge("S Pugh & E Beaver", "S Pugh & E Hamilton", "S Pugh St", 2)

    graph.add_edge("S Fraser & E College", "S Fraser & W Beaver", "S Fraser St", 2)
    graph.add_edge("S Fraser & W Beaver", "S Fraser & W Nittany", "S Fraser St", 2)

    graph.add_edge("S Garner & E College", "S Garner & E Beaver", "S Garner St", 2)
    graph.add_edge("S Garner & E Beaver", "S Garner & E Hamilton", "S Garner St", 2)

    graph.add_edge("S Barnard & W College", "S Barnard & W Beaver", "S Barnard St", 2)
    graph.add_edge("S Barnard & W Beaver", "S Barnard & W Nittany", "S Barnard St", 2)

    graph.add_edge("S Gill & E College", "S Gill & E Beaver", "S Gill St", 2)
    graph.add_edge("S Gill & E Beaver", "S Gill & E Hamilton", "S Gill St", 2)

    return graph

def main():
    print("Optimizing Food Delivery Routes in State College, PA\n")

    # Create graph for State College
    graph = create_state_college_graph()

    # Get all streets in the graph
    all_streets = graph.get_edges()
    print("\nStreets in the City Graph:")
    print(", ".join(all_streets))

    # Check if two streets connect
    street1 = "E College Ave"
    street2 = "S Pugh St"
    connects = graph.has_connection(street1, street2)
    print(f"\nDo {street1} and {street2} connect? {'Yes' if connects else 'No'}")

    # Define start and end locations
    source = "S Pugh & E College"
    destination = "S Atherton & W Beaver"

    # Apply real-time traffic updates
    update_traffic(graph)

    # Find shortest path using Dijkstra’s Algorithm
    shortest_distance, shortest_path = dijkstra(graph, source, destination)

    # Display results
    print(f"\nShortest Route from {source} to {destination}:")
    for i in range(len(shortest_path) - 1):
        print(f"  {shortest_path[i]} ➝ {shortest_path[i + 1]} ({graph.adjacency_list[shortest_path[i]][0][1]})")
    print(f"Estimated Travel Time: {round(shortest_distance, 2)} minutes\n")

if __name__ == "__main__":
    main()