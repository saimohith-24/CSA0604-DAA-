'''
N-Queens Problem
53: Visualizing Solutions for the N-Queens Problem

Discuss the importance of visualizing the solutions of the N-Queens Problem to understand the placement of queens better. Use a graphical representation to show how queens are placed on the board for different values of N. Explain how visual tools can help in debugging the algorithm and gaining insights into the problem's complexity. Provide examples of visual representations for N = 4, N = 5, and N = 8, showing different valid solutions.

Example Scenarios:
1.	Visualization for 4-Queens:
o	Input: N = 4
o	Output:
 
o	Explanation: Each 'Q' represents a queen, and '.' represents an empty space. 


2.	Visualization for 5-Queens:
o	Input: N = 5
o	Output:
 

3.	Visualization for 8-Queens:
o	Input: N = 8
o	Output:
 

'''
transactions = [200, 50, 150, 100]
for i in range(1, len(transactions)):
    key = transactions[i]
    j = i - 1
    while j >= 0 and key < transactions[j]:
        transactions[j + 1] = transactions[j]
        j -= 1
    transactions[j + 1] = key
