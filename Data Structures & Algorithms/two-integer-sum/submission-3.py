class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        numsMap = {}

        for index, num in enumerate(nums):
            if target - num in numsMap:
                return [numsMap[target-num], index]
            numsMap[num] = index