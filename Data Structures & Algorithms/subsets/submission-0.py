class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # - Brainstorming -
        # Could attempt this recursively, find all subsets of smaller list
        # Issue with this is that repeat subsets could be something that occurs
        # Another option would be to find all the subsets going up to n length
        # aka find all the 0 len subsets, then the 1 len subsets, etc
        # Recursive could work as long as it checked that it didn't repeat, but then
        # if it's doing all the subsets why even do it recursively, just do it all in one
        # pass.
        # 
        
        subsetList = []

        if not nums:
            return [[]]


        for subset in self.subsets(nums[1:]):
            subset += [nums[0]]
            subsetList.append(subset)
        
        
        subsetList.extend(
            self.subsets(nums[1:])
        )
        
        return subsetList
        