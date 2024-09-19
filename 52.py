'''
52: Practical Application of Insertion Sort

Identify and describe practical applications where Insertion Sort is an appropriate sorting algorithm. Explain why Insertion Sort's simplicity and predictable behavior make it suitable for scenarios such as sorting small datasets in embedded systems or sorting arrays where elements are continuously added in near real-time. Provide examples of industries or applications where Insertion Sort's characteristics align with specific sorting requirements, highlighting its advantages in terms of implementation simplicity and efficiency for small to medium-sized datasets.
Example Scenarios:
1.	Sorting Small Datasets:
o	Scenario: Insertion Sort is used in embedded systems where sorting small datasets efficiently is critical due to limited computational resources.
o	Input: [4, 3, 5, 1]
o	Output: [1, 3, 4, 5]
2.	Real-Time Data Insertion:
o	Scenario: Insertion Sort is used in financial systems where new transactions are added to a list of sorted transactions, requiring efficient real-time sorting.
o	Input: [10, 20, 15, 25, 30]
o	Output: [10, 15, 20, 25, 30]
3.	Educational Tools:
o	Scenario: Insertion Sort is used in educational tools to teach students the basics of sorting algorithms due to its intuitive approach and simplicity.
o	Input: [7, 3, 9, 1]
o	Output: [1, 3, 7, 9]


'''
transactions = [200, 50, 150, 100]
for i in range(1, len(transactions)):
    key = transactions[i]
    j = i - 1
    while j >= 0 and key < transactions[j]:
        transactions[j + 1] = transactions[j]
        j -= 1
    transactions[j + 1] = key
