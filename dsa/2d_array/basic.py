import random

mat = [
    [1, 2, 3, 4],
    [4, 5, 6],
    [7, 8, 9]
]

# num of rows
print(len(mat))

# num cols
print(len(mat[0]))

# user created matrix data

# num_cols = int(input("Enter number of columns"))
# num_rows = int(input("Enter number of rows"))
#
# matrix = []
# print(f"Enter the elements of the {num_rows}x{num_cols} matrix:")
#
# for i in range(num_rows):
#     row = []
#     for j in range(num_cols):
#         value = int(random.random())
#         row.append(value)
#     matrix.append(row)
# print(matrix)
# print("\nThe matrix you created is:")

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in matrix:
    for j in i:
        print(j)
