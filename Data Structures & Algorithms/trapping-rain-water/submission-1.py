class Solution:
    def trap(self, height: List[int]) -> int:

        left = 0
        right = 1

        totalWater = 0

        # find the maxHeightIndex
        maxHeightIndex = 0
        currMax = 0
        for i, h in enumerate(height):
            if h >= currMax:
                currMax = h
                maxHeightIndex = i
        
        currHeight = height[left]

        while right in range(maxHeightIndex):
            if height[right] >= currHeight:
                currHeight = height[right]
                left = right
                right += 1
            
            elif currHeight - height[right] > 0:
                totalWater += currHeight - height[right]
                right += 1

        left = len(height) - 2
        right = len(height) - 1
        currHeight = height[right]
        while left in range(len(height)-1, maxHeightIndex, -1):
            if height[left] >= currHeight:
                currHeight = height[left]
                right = left
                left -= 1
            
            elif currHeight - height[left] > 0:
                totalWater += currHeight - height[left]
                left -= 1
        
        return totalWater

        