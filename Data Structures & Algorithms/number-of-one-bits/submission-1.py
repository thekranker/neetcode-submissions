class Solution:
    def hammingWeight(self, n: int) -> int:
        
        count = 0
        num = n

        while num > 0:
            count += num % 2
            num = num // 2

        return count
