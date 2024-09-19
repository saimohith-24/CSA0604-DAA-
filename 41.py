'''
41:Given a list of item weights and the maximum capacity of a container, determine the maximum weight that can be loaded into the container using a greedy approach. The greedy approach should prioritize loading heavier items first until the container reaches its capacity.
Test Case 1:
Input:
n = 5
weights = [10, 20, 30, 40, 50]
max_capacity = 60
Output:50
Test Case 2:
Input:
n = 6
weights = [5, 10, 15, 20, 25, 30]
max_capacity = 50
Output:50
'''
def max_weight(weights, max_capacity):
    # Sort weights in descending order
    weights.sort(reverse=True)
    total_weight = 0
    
    for weight in weights:
        if total_weight + weight <= max_capacity:
            total_weight += weight
        else:
            break  # Stop if adding the next weight exceeds capacity
            
    return total_weight

# Test Case
n = 5
weights = [10, 20, 30, 40, 50]
max_capacity = 60
output = max_weight(weights, max_capacity)
print(output)  # Output: 50
