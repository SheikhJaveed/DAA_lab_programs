import heapq
def dijkstra(graph, start):
    # Number of vertices
    n = len(graph)

    # Initialize distances with infinity and the start node with 0
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Priority queue to store the vertices and their current distances
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # If the distance in the priority queue is greater than the current known distance, skip it
        if current_distance > distances[current_vertex]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def main():
    # Take user input for the graph
    n = int(input("Enter the number of locations: "))

    graph = {}
    print("Enter the distances between locations (format: from to distance):")
    for _ in range(n):
        from_location = input("From location: ")
        to_location = input("To location: ")
        distance = int(input("Distance: "))

        if from_location not in graph:
            graph[from_location] = {}
        if to_location not in graph:
            graph[to_location] = {}

        graph[from_location][to_location] = distance
        graph[to_location][from_location] = distance  # Assuming undirected graph

    start_location = input("Enter the start location: ")

    # Compute the shortest paths
    shortest_paths = dijkstra(graph, start_location)

    print(f"Shortest paths from {start_location}:")
    for location, distance in shortest_paths.items():
        print(f"To {location}: {distance}")


if __name__ == "__main__":
    main()
