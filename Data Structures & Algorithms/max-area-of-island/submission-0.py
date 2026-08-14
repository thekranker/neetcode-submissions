class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # store the max area
        maxArea = 0

        # seen squares are stored here
        visited = set()

        # dfs to find the area of an island
        def dfs(row: int, col: int) -> int:
            
            # base case
            if row not in range(len(grid)) or col not in range(len(grid[0])) or (row,col) in visited or grid[row][col] == 0:
               
                return 0
            
            visited.add((row,col))
            
            return 1 + dfs(row+1, col) + dfs(row-1, col) + dfs(row, col+1) + dfs(row, col-1)


        # loop through every square in the grid
        for row in range(len(grid)):
            for col in range(len(grid[0])):

                # if it's a 1 and hasn't been visited yet, start dfs
                if (row,col) not in visited and grid[row][col] == 1:
                    maxArea = max(maxArea, dfs(row, col))
        
        # return the max area found
        return maxArea
        
        