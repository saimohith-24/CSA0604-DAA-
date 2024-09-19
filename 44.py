'''
44:Given a graph with weights and a potential Minimum Spanning Tree (MST), verify if the given MST is unique. If it is not unique, provide another possible MST.
Test Case 1:
Input:
n = 4
m = 5
edges = [(0, 1, 10),(0, 2, 6),(0, 3, 5),(1, 3, 15),(2, 3, 4)]
given_mst = [(2, 3, 4), (0, 3, 5), (0, 1, 10)]
Output:Is the given MST unique? True
Test Case 2:
Input:
n = 5
m = 6
edges = [(0, 1, 1),(0, 2, 1),(1, 3, 2),(2, 3, 2),(3, 4, 3),(4, 2, 3)]
given_mst = [(0, 1, 1), (0, 2, 1), (1, 3, 2), (3, 4, 3)]
Output:Is the given MST unique? False
Another possible MST: [(0, 1, 1), (0, 2, 1), (2, 3, 2), (3, 4, 3)]
Total weight of MST: 7

'''
def is_unique_mst(edges, given_mst):
    mst_weights = {weight for _, _, weight in given_mst}
    alternative_edges = [edge for edge in edges if edge[2] not in mst_weights]
    
    return len(alternative_edges) > 0

# Test case
edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
given_mst = [(2, 3, 4), (0, 3, 5), (0, 1, 10)]
print(is_unique_mst(edges, given_mst))  # Output: True
