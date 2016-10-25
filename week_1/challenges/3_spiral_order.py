'''
A matrix is a two-dimensional array of r rows, each with c columns, such that the total number of elements in the matrix is r * c.

The spiral order of such a matrix is the list of all its elements starting at index (0, 0) and proceeding in clockwise order from the outermost values to innermost values.

Write a program that takes an int[][] matrix as its input and returns an int[] of all the input's values in spiral order.

Example: Given the following matrix:

int[][] matrix = {
  { 1, 2, 3 },
  { 4, 5, 6 },
  { 7, 8, 9 }
};
Your program should return {1,2,3,6,9,8,7,4,5}
'''

def spiral(matrix):

    # If matrix is already one dimensional
    if len(matrix) == 1:
        return matrix[0]

    ans = []

    top = 0
    bottom = len(matrix) - 1
    right = len(matrix[0]) - 1
    left = 0

    turn = 0

    while top <= bottom and left <= right:

        if turn == 0:
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1
            turn += 1

        elif turn == 1:
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1
            turn += 1

        elif turn == 2:
            for i in range(right, left - 1, -1):
                ans.append(matrix[bottom][i])
            bottom -= 1
            turn += 1

        elif turn == 3:
            for i in range(bottom, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1
            turn += 1

        turn %= 4


    return ans

matrix_1 = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]
matrix_2 = [[1, 2, 3]]
matrix_3 = [[1], [2], [3], [4]]
matrix_4 = [[1, 2], [3, 4], [5, 6]]
print spiral(matrix_4)
