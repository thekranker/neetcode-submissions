import math

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        # transpose the matrix
        for row in range(0, len(matrix), 1):
            for col in range(row + 1, len(matrix[0])):

                # swap values
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp

        # reverse each row
        for row in range(0, len(matrix), 1):
            matrix[row].reverse()




        