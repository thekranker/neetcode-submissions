class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        def matrixToIndex(row: int, col: int) -> int:
            return row * len(matrix[0]) + col

        def indexToMatrix(index: int) -> List[int]:
            rowNum = index // len(matrix[0])
            colNum = index % len(matrix[0])
            return [rowNum, colNum]


        left = 0
        right = matrixToIndex(len(matrix) - 1, len(matrix[0]) - 1)

        # 1 3 4 4 7 8 9
        while left <= right:

            middleMatrix = indexToMatrix((left + right) // 2)
            middleIndex = (left + right) // 2

            # target = middle
            if target == matrix[middleMatrix[0]][middleMatrix[1]]:
                return True
            
            # target < middle
            if target < matrix[middleMatrix[0]][middleMatrix[1]]:
                right = middleIndex - 1

            # target > middle
            if target > matrix[middleMatrix[0]][middleMatrix[1]]:
                left = middleIndex + 1


        return False


        




