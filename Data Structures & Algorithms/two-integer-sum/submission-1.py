class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashset = {}
        output = []

        for index, num in enumerate(nums):
            if target - num in hashset:
                output.append(hashset[target-num])
                output.append(index)
            hashset[num] = hashset.get(num, index)
        return output
        