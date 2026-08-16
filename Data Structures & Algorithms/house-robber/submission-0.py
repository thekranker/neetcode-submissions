class Solution:
    def rob(self, nums: List[int]) -> int:
        
        cache = {}

        def dp(index: int):
            # base case
            if index >= len(nums):
                return 0
            if index in cache:
                return cache[index]

            result = max(nums[index] + dp(index+2), dp(index+1))
            cache[index] = result

            return result


        return dp(0)
