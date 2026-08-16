class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows, cols = len(board), len(board[0])

        for row in range(rows):
            numSet = set()
            for col in range(cols):
                if board[row][col] == '.':
                    continue
                currNum = int(board[row][col])
                if currNum > 9 or currNum < 1 or currNum in numSet:
                    return False
                numSet.add(currNum)

        for col in range(cols):
            numSet = set()
            for row in range(rows):
                if board[row][col] == '.':
                    continue
                currNum = int(board[row][col])
                if currNum > 9 or currNum < 1 or currNum in numSet:
                    return False
                numSet.add(currNum)

        for row in range(0, rows - 3, 3):
            for col in range(0, cols - 3, 3):
                numSet = set()
                for r in range(row, row+3):
                    for c in range(col, col+3):
                        if board[r][c] == '.':
                            continue
                        currNum = int(board[r][c])
                        if currNum > 9 or currNum < 1 or currNum in numSet:
                            return False
                        numSet.add(currNum)

        return True

        