'''
46:Given an undirected graph, implement an approximation algorithm to find a vertex cover using the maximum degree heuristic. The heuristic selects the vertex with the highest degree and includes it in the vertex cover until all edges are covered.
Test Case 1:
Input:
n = 6
m = 7
edges = [(0, 1),(0, 2),(1, 3),(1, 4),(2, 4),(3, 5),(4, 5)]
Output:Vertex Cover: [1, 4, 5]
Test Case 2:
Input:
n = 5
m = 5
edges = [(0, 1),(0, 2),(0, 3),(1, 4),(2, 4)]
Output:Vertex Cover: [0, 4]


'''
def vertex_cover_max_degree(n, edges):
    from collections import defaultdict

    # Create a graph representation
    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    vertex_cover = set()
    uncovered_edges = set(edges)

    while uncovered_edges:
        # Find the vertex with the maximum degree
        degree = {v: len(neighbors) for v, neighbors in graph.items() if v not in vertex_cover}
        max_vertex = max(degree, key=degree.get)

        # Add the vertex to the vertex cover
        vertex_cover.add(max_vertex)

        # Remove all edges incident to this vertex
        uncovered_edges = {edge for edge in uncovered_edges if max_vertex not in edge}

    return list(vertex_cover)

# Test Case
n = 6
m = 7
edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (3, 5), (4, 5)]
print("Vertex Cover:", vertex_cover_max_degree(n, edges))
