'''
Optimal Binary Search Trees

59. Implement the Optimal Binary Search Tree algorithm for the keys A,B,C,D with frequencies 0.1,0.2,0.4,0.3 Write the code using any programming language to construct the OBST for the given keys and frequencies. Execute your code and display the resulting OBST and its cost. Print the cost and root  matrix. 
Input N =4, Keys = {A,B,C,D} Frequencies =  {01.02.,0.3,0.4}
Output : 1.7
Cost Table
	0	1	2	3	4
1	0	0.1	0.4	1.1	1.7
2		0	0.2	0.8	0.4
3			0	0.4	1.0
4				0	0.3
5					0
Root table
	1	2	3	4
1	1	2	3	3
2		2	3	3
3			3	3
4				4

a)	Test cases
Input:  keys[] = {10, 12}, freq[] = {34, 50}
Output = 118
b)	Input:  keys[] = {10, 12, 20}, freq[] = {34, 8, 50}
Output = 142

'''
transactions = [200, 50, 150, 100]
for i in range(1, len(transactions)):
    key = transactions[i]
    j = i - 1
    while j >= 0 and key < transactions[j]:
        transactions[j + 1] = transactions[j]
        j -= 1
    transactions[j + 1] = key
