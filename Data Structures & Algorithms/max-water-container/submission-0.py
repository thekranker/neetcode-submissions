class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # define variables
        left = 0
        right = len(heights) - 1
        currMaxArea = 0

        while left < right:
            area = min(heights[left], heights[right]) * (right - left)

            currMaxArea = max(area, currMaxArea)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        
        return currMaxArea


            
            


        