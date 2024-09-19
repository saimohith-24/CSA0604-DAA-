'''
56. Implement the Quick Sort algorithm in a programming language of your choice and test it on the array 19,72,35,46,58,91,22,31. Choose the middle element as the pivot and partition the array accordingly. Show the array after this partition. Recursively apply Quick Sort on the sub-arrays formed. Display the array after each recursive call until the entire array is sorted. Execute your code and show the sorted array. 
Input :N= 8, a[] = {19,72,35,46,58,91,22,31}
Output : 19,22,31,35,46,58,72,91
Test Cases :
Input : N= 8, a[] = {31,23,35,27,11,21,15,28}
Output : 11,15,21,23,27,28,31,35
Test Cases :
Input : N= 10, a[] = {22,34,25,36,43,67, 52,13,65,17}
Output : 13,17,22,25,34,36,43,52,65,67

'''
transactions = [200, 50, 150, 100]
for i in range(1, len(transactions)):
    key = transactions[i]
    j = i - 1
    while j >= 0 and key < transactions[j]:
        transactions[j + 1] = transactions[j]
        j -= 1
    transactions[j + 1] = key
