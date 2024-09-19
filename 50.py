'''
50: Time Complexity Analysis of Bubble Sort

Discuss the time complexity of Bubble Sort in terms of best-case, worst-case, and average-case scenarios. Explain how Bubble Sort's performance depends on the initial ordering of elements in the array and how it compares to other sorting algorithms like Insertion Sort or Quick Sort in terms of efficiency. Provide insights into why Bubble Sort is generally not preferred for large datasets, highlighting scenarios where its quadratic time complexity is a significant disadvantage.

Example Scenarios:
1.	Worst-Case Scenario:
o	Input: [5, 4, 3, 2, 1]
o	Output: [1, 2, 3, 4, 5]
2.	Best-Case Scenario:
o	Input: [1, 2, 3, 4, 5]
o	Output: [1, 2, 3, 4, 5]
3.	Average-Case Scenario:
o	Input: [3, 1, 4, 2, 5]
o	Output: [1, 2, 3, 4, 5]

'''
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break  # Exit if no swaps occurred
    return arr

# Test case
input_list = [64, 25, 12, 22, 11]
expected_output = [11, 12, 22, 25, 64]
assert bubble_sort(input_list) == expected_output
