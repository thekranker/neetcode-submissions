class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows,cols = len(grid), len(grid[0])
        
        queue = []
        visited = set()
        currLevel = 0

        # populate the queue will all the treasure locations
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append([row,col])
                    visited.add((row,col))
        
        # run bfs to populate land
        while queue:
            row, col = queue.pop(0)

            if row not in range(rows) or col not in range(cols) or grid[row][col] == -1:
                continue
        

            for incRow, incCol in [(1,0), (-1,0), (0,1), (0,-1)]:
                r, c = row + incRow, col + incCol
                if r in range(rows) and c in range(cols) and (r,c) not in visited and grid[r][c] != -1:
                    grid[r][c] = grid[row][col] + 1
                    queue.append([r,c])
                    visited.add((r,c))      






