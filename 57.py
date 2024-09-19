'''

Binary Search 
57.  Implement the Binary Search algorithm in a programming language of your choice and test it on the array 5,10,15,20,25,30,35,40,45 to find the position of the element 20.
Execute your code and provide the index of the element 20.  Modify your implementation to count the number of comparisons made during the search process. Print this count along with the result. 
Input : N= 9, a[] = {5,10,15,20,25,30,35,40,45}, search key = 20
Output :4
Test cases
Input : N= 6, a[] = {10,20,30,40,50,60}, search key = 50
Output :5
Input : N= 7, a[] = {21,32,40,54,65,76,87}, search key = 32
Output :2

'''
transactions = [200, 50, 150, 100]
for i in range(1, len(transactions)):
    key = transactions[i]
    j = i - 1
    while j >= 0 and key < transactions[j]:
        transactions[j + 1] = transactions[j]
        j -= 1
    transactions[j + 1] = key
