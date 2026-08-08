class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:



        def dfs(row: int, col: int, wordIndex: int, visited: set):
            # code here
            if row not in range(len(board)) or col not in range(len(board[0])):
                return
            elif board[row][col] != word[wordIndex] or (row,col) in visited:
                return
            if board[row][col] == word[wordIndex] and wordIndex == len(word) - 1:
                return True

            visited.add((row, col))

            if dfs(row + 1, col, wordIndex+1, visited) or dfs(row - 1, col, wordIndex+1, visited) or dfs(row, col + 1, wordIndex+1, visited) or dfs(row, col - 1, wordIndex+1, visited):
                return True

            visited.remove((row,col))
        
        # loop through every letter in the grid
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    visited = set()
                    if dfs(row, col, 0, visited):
                        return True

        return False



