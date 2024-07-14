from collections import defaultdict
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    dfs_order = [start]

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_order.extend(dfs(graph, neighbor, visited))

    return dfs_order


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

    # Get the start node for DFS
    start_node = input("Enter the start node: ")

    # Perform DFS
    dfs_result = dfs(graph, start_node)

    # Print the result
    print("DFS Order:", dfs_result)


if __name__ == "__main__":
    main()
