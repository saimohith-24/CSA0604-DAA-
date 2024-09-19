'''
Bubble Sort

47: Optimizing Bubble Sort
Discuss how your selection_sort function handles edge cases. Specifically, consider and explain the outcomes for the following cases:
o	An empty list
o	A list with one element
o	A list with all identical elements
o	A list with negative numbers
Test Cases:
1.	Input:[]
o	Expected Output:[]
2.	Input:[1]
o	Expected Output:[1]
3.	Input:[7, 7, 7, 7]
o	Expected Output:[7, 7, 7, 7]
4.	Input:[-5, -1, -3, -2, -4]
o	Expected Output:[-5, -4, -3, -2, -1]

'''
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
