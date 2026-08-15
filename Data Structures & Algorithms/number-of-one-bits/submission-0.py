class Solution:
    def hammingWeight(self, n: int) -> int:

        val = n
        count = 0

        while val >= 1:
            if val % 2 == 1:
                count += 1
            val = val // 2


        return count
        