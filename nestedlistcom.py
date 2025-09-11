# transpose rows and columns
matrix = [
    [1, 2, 3, 4],      # row 0
    [5, 6, 7, 8],      # row 1
    [9, 10, 11, 12]    # row 2
]
print([[row[i] for row in matrix] for i in range(4)])

# inbuilt function
print(list(zip(*matrix)))