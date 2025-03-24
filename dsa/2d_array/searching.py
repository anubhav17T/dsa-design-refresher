class Solution(object):
    def binary(self, arr: list, target: int) -> bool:
        low = 0
        high = len(arr) - 1
        mid = 0
        while low < high:
            mid = (high + low) // 2
            if arr[mid] < target:
                low = mid + 1
            elif arr[mid] > target:
                high = mid - 1
            else:
                return True
        return False

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for arr in matrix:
            start = 0
            end = len(arr) - 1
            while start <= end:
                mid = start + (end - start) // 2
                if target == arr[mid]:
                    return True
                elif target > arr[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        return False


b = Solution()
print(b.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=20))
print(b.searchMatrix(matrix=[[1, 3]], target=3))
print(b.searchMatrix(matrix=[[1]], target=1))
print(b.searchMatrix(matrix=[[1],[3]], target=3))

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
for i in range(len(matrix)):
    print(matrix[i][i])


for i in range(len(matrix[0])):
    for row in range(len(matrix)):
        print(matrix[row][i])



def compare_row_elements(matrix):
    for row_index, row in enumerate(matrix):
        if all(x == row[0] for x in row):  # Checks if all elements are equal in the row
            print(f"Row {row_index} has all equal elements: {row}")
        else:
            print(f"Row {row_index} does not have all equal elements: {row}")

# Example 2D Matrix
matrix = [
    [1, 1, 1],
    [2, 2, 2],
    [3, 4, 5],
    [5, 5, 5]
]

compare_row_elements(matrix)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

num_columns = len(matrix[0])  # This tells us how many columns there are

# Loop through each column
for col in range(num_columns):
    for row in matrix:
        print(row)
        print(row[col])


def is_symmetric(matrix):
    n = len(matrix)

    # Check if the matrix is square
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:  # Check symmetry
                return False
    return True


# Example matrix
matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

if is_symmetric(matrix):
    print("The matrix is symmetric.")
else:
    print("The matrix is not symmetric.")


def matrixSum(nums):
    for row in nums:
        row.sort(reverse=True)
    score = 0
    for col in range(len(nums[0])):
        max_value = nums[0][col]
        for row in range(1, len(nums)):
            if nums[row][col] > max_value:
                max_value = nums[row][col]
        score += max_value

# Example Input
nums = [[7, 2, 1], [6, 4, 2], [6, 5, 3], [3, 2, 1]]
print(matrixSum(nums))