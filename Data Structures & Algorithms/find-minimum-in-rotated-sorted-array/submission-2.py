class Solution:
    def findMin(self, nums: List[int]) -> int:

        # find the minimum
        # [3,4,5,6,1,2]
        # find the middle '5'
        # if left pos is greater than five, search the left side including mid
        # if right is smaller than five, search right side
        # if left == right, return

        # [5, 6, 7, 1, 2, 3, 4]
        left = 0
        right = len(nums) - 1
        while left != right:
            mid = (left + right) // 2
            if nums[left] > nums[mid]:
                right = mid
            elif nums[right] < nums[mid]:
                left = mid + 1
            else:
                return nums[left]
            
        return nums[left]

        