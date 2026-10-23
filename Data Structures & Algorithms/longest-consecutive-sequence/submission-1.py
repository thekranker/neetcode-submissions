class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        maxCount = 0
        numsSet = set()
        
        # populate numsSet
        for num in nums:
            numsSet.add(num)

        startNums = []
        for num in numsSet:
            if not (num-1) in numsSet:
                startNums.append(num)
            
        for num in startNums:
            count = 1
            curr = num
            while curr+1 in numsSet:
                count+= 1
                curr += 1
            
            maxCount = max(maxCount, count)
        
        return maxCount

        

        