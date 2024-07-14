def tsp_backtracking(graph, curr_pos, n, count, cost, visited, min_cost):
    if count == n and graph[curr_pos][0] > 0:
        min_cost[0] = min(min_cost[0], cost + graph[curr_pos][0])
        return

    for i in range(n):
        if visited[i] == False and graph[curr_pos][i] > 0:
            visited[i] = True
            tsp_backtracking(graph, i, n, count + 1, cost + graph[curr_pos][i], visited, min_cost)
            visited[i] = False


def main():
    n = int(input("Enter the number of cities: "))
    graph = []
    print("Enter the adjacency matrix (row-wise, space-separated):")
    for i in range(n):
        row = list(map(int, input().split()))
        graph.append(row)

    visited = [False] * n
    visited[0] = True
    min_cost = [float('inf')]
    tsp_backtracking(graph, 0, n, 1, 0, visited, min_cost)

    if min_cost[0] == float('inf'):
        print("No solution exists")
    else:
        print(f"The minimum cost of the tour is: {min_cost[0]}")


if __name__ == "__main__":
    main()
