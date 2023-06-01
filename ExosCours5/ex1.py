import numpy as np


def dijkstra(adj_matrix, start_node, end_node):
    n = adj_matrix.shape[0]
    visited = np.zeros(n, dtype=bool)
    distances = np.full(n, np.inf)
    distances[start_node] = 0

    while not visited[end_node]:
        min_distance = np.inf
        current_node = -1

        # Find the unvisited node with the smallest distance
        for node in range(n):
            if not visited[node] and distances[node] < min_distance:
                min_distance = distances[node]
                current_node = node

        # Mark the current node as visited
        visited[current_node] = True

        # Update the distances to the neighboring nodes
        for neighbor in range(n):
            if adj_matrix[current_node, neighbor] != 0:
                new_distance = (
                    distances[current_node] + adj_matrix[current_node, neighbor]
                )
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

    return distances[end_node]


# Example usage
adj_matrix = np.array(
    [
        [0, 7, 0, 0, 9, 14, 0, 0, 0],
        [7, 0, 10, 15, 0, 0, 0, 0, 0],
        [0, 10, 0, 11, 0, 2, 0, 0, 0],
        [0, 15, 11, 0, 6, 0, 0, 0, 0],
        [9, 0, 0, 6, 0, 30, 0, 0, 0],
        [14, 0, 2, 0, 30, 0, 18, 0, 0],
        [0, 0, 0, 0, 0, 18, 0, 55, 0],
        [0, 0, 0, 0, 0, 0, 55, 0, 44],
        [0, 0, 0, 0, 0, 0, 0, 44, 0],
    ]
)

start_node = 0
end_node = 8

shortest_distance = dijkstra(adj_matrix, start_node, end_node)
print(
    f"The shortest distance between nodes {start_node} and {end_node} is {shortest_distance}"
)
