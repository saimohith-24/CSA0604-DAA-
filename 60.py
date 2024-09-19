'''
60. Consider a set of keys 10,12,16,21 with frequencies 4,2,6,3 and the respective probabilities.  Write a Program to construct an OBST in a programming language of your choice. Execute your code and display the resulting OBST, its cost and root matrix.
Input N =4, Keys = {10,12,16,21} Frequencies =  {4,2,6,3}
Output : 26

	0	1	2	3
0	4	80	202	262
1		2	102	162
2			6	12
3				3

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
