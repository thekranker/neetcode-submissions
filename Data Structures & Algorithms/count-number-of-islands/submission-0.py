class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # visited set
        visited = set()

        # island count
        islandCount = 0

        # out of bounds check
        def bounds(row: int, col: int):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return True
            return False

        # island dfs
        def exploreIsland(row: int, col: int):
                # base case
                if bounds(row,col) or (row,col) in visited or grid[row][col] == "0":
                    return

                visited.add((row, col))

                exploreIsland(row + 1, col) # down
                exploreIsland(row - 1, col) # up
                exploreIsland(row, col + 1) # right
                exploreIsland(row, col - 1) # left


        # loop through the entire grid
        for row in range(0, len(grid), 1):
            for col in range(0, len(grid[0]), 1):

                if not (row, col) in visited and grid[row][col] == "1":
                    islandCount += 1
                
                exploreIsland(row, col)


        return islandCount

        






        