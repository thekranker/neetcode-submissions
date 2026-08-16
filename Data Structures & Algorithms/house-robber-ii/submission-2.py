class Solution:
    def rob(self, nums: List[int]) -> int:

        cache = {}

        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]
        
        incFirst = nums[0:len(nums) - 1]
        incLast = nums[1: len(nums)]

        def dp(index: int, arr: List[int]):
            if index not in range(len(arr)):
                return 0
            if index in cache:
                return cache[index]
            
            result = max(arr[index] + dp(index+2, arr), dp(index+1, arr))
            cache[index] = result
            return result
        
        result1 = dp(0, incFirst)
        cache = {}
        result2 = dp(0, incLast)

        return max(result1, result2)
