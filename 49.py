'''
49.Modify your bubble_sort function to stop early if the list becomes sorted before all passes are completed. Explain why this optimization improves performance and how it affects the time complexity in the best case.
Test Cases:
•	Test your optimized function with the following lists:
1.	Input:[64, 25, 12, 22, 11]
	Expected Output:[11, 12, 22, 25, 64]
2.	Input:[29, 10, 14, 37, 13]
	Expected Output:[10, 13, 14, 29, 37]
3.	Input:[3, 5, 2, 1, 4]
	Expected Output:[1, 2, 3, 4, 5]
4.	Input:[1, 2, 3, 4, 5] (Already sorted list)
	Expected Output:[1, 2, 3, 4, 5]
5.	Input:[5, 4, 3, 2, 1] (Reverse sorted list)
	Expected Output:[1, 2, 3, 4, 5]

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
