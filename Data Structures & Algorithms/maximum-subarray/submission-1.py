class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        output = float('-inf')
        curSum = 0

        for num in nums:
            curSum = max(curSum + num, num)
            output = max(output, curSum)

        return output
        