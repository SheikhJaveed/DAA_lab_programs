import heapq


def get_graph_from_user():
    graph = {}
    num_edges = int(input("Enter the number of edges: "))

    for _ in range(num_edges):
        edge = input("Enter the edge and its weight (format: node1 node2 weight): ").split()
        node1, node2, weight = edge[0], edge[1], int(edge[2])

        if node1 not in graph:
            graph[node1] = []
        if node2 not in graph:
            graph[node2] = []

        graph[node1].append((node2, weight))
        graph[node2].append((node1, weight))

    return graph


def prim(graph: dict, start: str):
    mst = []
    visited = set()
    pq = [(0, start, None)]
    total_cost = 0

    while pq:
        weight, curr_node, prev_node = heapq.heappop(pq)
        if curr_node in visited:
            continue

        visited.add(curr_node)
        total_cost += weight

        if prev_node is not None:
            mst.append((prev_node, curr_node, weight))

        for neighbor, edge_weight in graph[curr_node]:
            if neighbor not in visited:
                heapq.heappush(pq, (edge_weight, neighbor, curr_node))

    return mst, total_cost


def main():
    graph = get_graph_from_user()
    start_node = input("Enter the starting node: ")
    mst, cost = prim(graph, start_node)

    print("Minimum Spanning Tree (MST):")
    for edge in mst:
        print(f"{edge[0]} - {edge[1]} with weight {edge[2]}")
    print(f"Total cost of MST: {cost}")


if __name__ == "__main__":
    main()
