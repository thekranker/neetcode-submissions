class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # base case
        if not nums:
            return []

        results = []

        if nums[0] == target:
            results.append([nums[0]])

        if nums[0] < target:
            lists = self.combinationSum(nums, target - nums[0])
            for list in lists:
                list.append(nums[0])
            results.extend(lists)

        results.extend(self.combinationSum(nums[1:], target))

        return results
            
        



