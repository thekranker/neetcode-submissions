class Solution:
    def hammingWeight(self, n: int) -> int:
        
        count = 0
        num = n

        while num > 0:
            num = num & (num-1)
            count += 1

        return count

