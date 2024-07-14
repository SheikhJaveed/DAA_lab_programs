class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))

    def bellman_ford(self, src):
        dist = [float("inf")] * self.V
        dist[src] = 0

        for _ in range(self.V - 1):
            for u, v, w in self.edges:
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        for u, v, w in self.edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                print("Graph contains a negative weight cycle")
                return

        self.print_solution(dist)

    def print_solution(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print(f"{i}\t\t{dist[i]}")

def main():
    vertices = int(input("Enter the number of vertices: "))
    graph = Graph(vertices)

    edges = int(input("Enter the number of edges: "))
    print("Enter the edges with their weights (format: u v w):")
    for _ in range(edges):
        u = int(input("From vertex: "))
        v = int(input("To vertex: "))
        w = int(input("Weight: "))
        graph.add_edge(u, v, w)

    src = int(input("Enter the source vertex: "))

    graph.bellman_ford(src)

if __name__ == "__main__":
    main()
