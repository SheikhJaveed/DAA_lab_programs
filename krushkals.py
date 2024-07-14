class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            self.parent[item] = self.find(self.parent[item])
            return self.parent[item]

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1


def kruskal(graph):
    vertices = set()
    for edge in graph:
        vertices.add(edge[0])
        vertices.add(edge[1])

    disjoint_set = DisjointSet(vertices)
    mst = []
    total_cost = 0

    # Sort edges based on their weight
    graph.sort(key=lambda x: x[2])

    for edge in graph:
        u, v, weight = edge
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
            mst.append(edge)
            total_cost += weight

    return mst, total_cost


def main():
    # Take user input for the graph
    n = int(input("Enter the number of edges: "))

    graph = []
    print("Enter the edges with their weights (format: from to weight):")
    for _ in range(n):
        from_location = input("From location: ")
        to_location = input("To location: ")
        weight = int(input("Weight: "))
        graph.append((from_location, to_location, weight))

    # Compute MST using Kruskal's algorithm
    mst, total_cost = kruskal(graph)

    print("Edges in the Minimum Spanning Tree:")
    for edge in mst:
        print(f"{edge[0]} -- {edge[1]} == {edge[2]}")
    print(f"Total cost of Minimum Spanning Tree: {total_cost}")


if __name__ == "__main__":
    main()
