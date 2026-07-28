class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        perimeterCount = 0

        for row in range(0, len(grid), 1):
            for col in range(0, len(grid[0]), 1):
                square = grid[row][col]

                # check if square is land
                if square == 1:
                    # calculate perimeter
                    if row-1 < 0:
                        perimeterCount += 1     # bounded north
                    elif grid[row-1][col] == 0:
                        perimeterCount += 1     # water north
                    if row+1 > len(grid) - 1:
                        perimeterCount += 1     # bounded south
                    elif grid[row+1][col] == 0:
                        perimeterCount += 1     #  water south
                    if col-1 < 0:
                        perimeterCount += 1     # bounded west
                    elif grid[row][col-1] == 0:
                        perimeterCount += 1     # water west
                    if col+1 > len(grid[0]) - 1:
                        perimeterCount += 1     # bounded east
                    elif grid[row][col+1] == 0:
                        perimeterCount += 1     # water east

        return perimeterCount

                
