import random

def update_traffic(graph):
    """Simulates real time traffic by adjusting road weights."""

    for node in graph.adjacency_list:
        base_weight = graph.base_weight
        for i, (neighbor, weight) in enumerate(graph.adjacency_list[node]):
            traffic_multiplier = random.uniform(0.5, 1.5) # Randomly adjust the traffic by 50% to 150%
            new_weight = round(base_weight * traffic_multiplier, 2)

            # Update the graph with the new traffic weight
            graph.adjacency_list[node][i] = (neighbor, new_weight)

    print("\nTraffic conditions updated.\n")