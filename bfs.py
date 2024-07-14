from collections import deque, defaultdict
def bfs(graph, start):
    visited = set()
    queue = deque([start])  #deque - double ended queue
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)



def main():
    # Get the number of edges
    num_edges = int(input("Enter the number of edges: "))

    graph = defaultdict(set)

    # Read each edge
    print("Enter each edge as a pair of nodes (e.g., 'A B'):")
    for _ in range(num_edges):
        u, v = input().split()
        graph[u].add(v)
        graph[v].add(u)

    # Get the start node for BFS
    start_node = input("Enter the start node: ")

    # Perform BFS
    bfs(graph, start_node)




if __name__ == "__main__":
    main()
