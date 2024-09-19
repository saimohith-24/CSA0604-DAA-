'''
51: Handling Duplicates in Insertion Sort

Describe how Insertion Sort manages arrays with duplicate elements during the sorting process. Explain the algorithm's behavior when encountering duplicate values, including whether it preserves the relative order of duplicates and how it affects the overall sorting outcome. Provide specific examples with arrays containing duplicate integers, demonstrating how Insertion Sort sorts the array while ensuring duplicates are correctly positioned, and discuss any considerations or adjustments that might be necessary.
Example Scenarios:
1.	Array with Duplicates:
o	Input: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
o	Output: [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]
2.	All Identical Elements:
o	Input: [5, 5, 5, 5, 5]
o	Output: [5, 5, 5, 5, 5]
3.	Mixed Duplicates:
o	Input: [2, 3, 1, 3, 2, 1, 1, 3]
o	Output: [1, 1, 1, 2, 2, 3, 3, 3]

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
