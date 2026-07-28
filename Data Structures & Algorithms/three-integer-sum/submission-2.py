class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        results = []
        nums.sort()

        i = 0
        while i < len(nums):
            left = i + 1
            right = len(nums) - 1

            
            target = nums[i] * -1
            while left < right:
                if nums[left] + nums[right] == target:
                    results.append([nums[left], nums[right], -1 * target])
                    while left+1 < len(nums) and nums[left] == nums[left+1]:
                        left += 1
                    left += 1
                    while right-1 > -1 and nums[right] == nums[right-1]:
                        right -= 1
                    right -= 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
            
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return results

        