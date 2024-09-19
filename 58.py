'''
58. You are given a sorted array 3,9,14,19,25,31,42,47,53 and asked to find the position of the element 31 using Binary Search.Show the mid-point calculations and the steps involved in finding the element. Display, what would happen if the array was not sorted, how would this impact the performance and correctness of the Binary Search algorithm?  
Input : N= 9, a[] = {3,9,14,19,25,31,42,47,53}, search key = 31
Output :6
Test cases
Input : N= 7, a[] = {13,19,24,29,35,41,42}, search key = 42
Output :7
Test cases
Input : N= 6, a[] = {20,40,60,80,100,120}, search key = 60
Output :3

'''
transactions = [200, 50, 150, 100]
for i in range(1, len(transactions)):
    key = transactions[i]
    j = i - 1
    while j >= 0 and key < transactions[j]:
        transactions[j + 1] = transactions[j]
        j -= 1
    transactions[j + 1] = key
