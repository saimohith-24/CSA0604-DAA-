'''
TRACTABILITY & APPROXIMATION ALGORITHM
45. Approximation Algorithm Vertex Cover
Q1:Given an undirected graph, implement a greedy approximation algorithm to find a vertex cover. A vertex cover of a graph is a set of vertices such that each edge in the graph is incident to at least one vertex in the set.
Test Case 1:
Input:
n = 5
m = 6
edges = [(0, 1),(0, 2),(1, 2),(1, 3),(2, 4),(3, 4)]
Output:Vertex Cover: [1, 2, 3]
Test Case 2:
Input:
n = 4
m = 4
edges = [(0, 1),(0, 2),(1, 2),(2, 3)]
Output:Vertex Cover: [0, 2]

'''
def greedy_vertex_cover(n, edges):
    vertex_cover = set()
    edge_set = set(edges)

    while edge_set:
        # Take an arbitrary edge
        u, v = edge_set.pop()
        vertex_cover.add(u)
        vertex_cover.add(v)

        # Remove all edges incident to u and v
        edge_set = {edge for edge in edge_set if u not in edge and v not in edge}

    return list(vertex_cover)

# Test Case
n = 5
edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 4), (3, 4)]
result = greedy_vertex_cover(n, edges)
print("Vertex Cover:", result)
