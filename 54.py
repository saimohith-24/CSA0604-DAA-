'''
N-Queens Problem
54: Generalizing the N-Queens Problem

Discuss the generalization of the N-Queens Problem to other board sizes and shapes, such as rectangular boards or boards with obstacles. Explain how the algorithm can be adapted to handle these variations and the additional constraints they introduce. Provide examples of solving generalized N-Queens Problems for different board configurations, such as an 8×10 board, a 5×5 board with obstacles, and a 6×6 board with restricted positions.

Example Scenarios:
1.	8×10 Board:
o	Input: 8 rows and 10 columns
o	Output: Possible solution [1, 3, 5, 7, 9, 2, 4, 6]
o	Explanation: Adapt the algorithm to place 8 queens on an 8×10 board, ensuring no two queens threaten each other.
2.	5×5 Board with Obstacles:
o	Input: N = 5, Obstacles at positions [(2, 2), (4, 4)]
o	Output: Possible solution [1, 3, 5, 2, 4]
o	Explanation: Modify the algorithm to avoid placing queens on obstacle positions, ensuring a valid solution that respects the constraints.
3.	6×6 Board with Restricted Positions:
o	Input: N = 6, Restricted positions at columns 2 and 4 for the first queen
o	Output: Possible solution [1, 3, 5, 2, 4, 6]
o	Explanation: Adjust the algorithm to handle restricted positions, ensuring the queens are placed without conflicts and within allowed columns.


'''
transactions = [200, 50, 150, 100]
for i in range(1, len(transactions)):
    key = transactions[i]
    j = i - 1
    while j >= 0 and key < transactions[j]:
        transactions[j + 1] = transactions[j]
        j -= 1
    transactions[j + 1] = key
