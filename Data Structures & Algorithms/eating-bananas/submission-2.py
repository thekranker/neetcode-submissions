import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        
        # use binary search on each number, divide by the hours, if its less than the
        # number, try again hgiher, else try again lower.
        left = 1
        right = max(piles)
        selectedNum = max(piles)

        while left <= right:
            middle = (left + right) // 2
            totalHours = 0
            for pile in piles:
                totalHours += math.ceil(pile / middle)

            if totalHours <= h:
                selectedNum = middle
                right = middle - 1
            
            if totalHours > h:
                left = middle + 1


        # return the selected number
        return selectedNum