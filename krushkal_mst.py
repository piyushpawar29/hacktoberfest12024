def kruskal_mst(graph):
    """Finds the Minimum Spanning Tree (MST) of a graph using Kruskal's algorithm.

    Args:
        graph: A dictionary representing the graph, where keys are nodes and values
            are lists of tuples (neighbor, weight).

    Returns:
        A list of tuples representing the edges of the MST.
    """

    num_vertices = len(graph)
    mst = []

    # Sort edges in ascending order of weight
    edges = []
    for node in graph:
        for neighbor, weight in graph[node]:
            edges.append((weight, node, neighbor))
    edges.sort()

    # Create a disjoint set to track connected components
    parent = [i for i in range(num_vertices)]

    def find_parent(node):
        if parent[node] != node:
            parent[node] = find_parent(parent[node])
        return parent[node]

    def union(node1, node2):
        parent1 = find_parent(node1)
        parent2 = find_parent(node2)
        if parent1 != parent2:
            parent[parent1] = parent2

    # Iterate through sorted edges and add them to the MST if they don't form a cycle
    for weight, node1, node2 in edges:
        if find_parent(node1) != find_parent(node2):
            mst.append((node1, node2, weight))
            union(node1, node2)

    return mst

# Example usage
graph = {
    'A': [('B', 4), ('C', 3)],
    'B': [('A', 4), ('C', 2), ('D', 5)],
    'C': [('A', 3), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

mst = kruskal_mst(graph)
print(mst)
