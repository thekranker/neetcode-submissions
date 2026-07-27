class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        # base case
        if not nums:
            return [[]]

        results = []

        for i in range(0, len(nums), 1):
            temp = nums[0]
            nums[0] = nums[i]
            nums[i] = temp

            lists = self.permute(nums[1:])
            for list in lists:
                list.insert(0, nums[0])
                results.append(list)

        return results