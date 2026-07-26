class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # - Brainstorming -
        # My solution must run in O(logn) time.
        # The idea I have is to divide the sorted array in half and pick higher or lower
        # until eventually the target is reached or the array contains only one element
        # that isn't the target.
        # One issue that i'm thinking of as i'm doing this is wondering how I will handle
        # cases where there is no direct middle. My instinct is to round down for this case.


        low = 0
        high = len(nums) - 1
        middle = (low + high) // 2


        while (low <= high):
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                high = middle -1
                middle = (low + high) // 2
            else:
                low = middle + 1
                middle = (low + high) // 2

        return -1
            
        