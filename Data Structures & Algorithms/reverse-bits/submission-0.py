class Solution:
    def reverseBits(self, n: int) -> int:

        output = 0
        num = n

        for i in range(32):
            if num % 2 == 1:
                output += 2 ** (31-i)
            num = num >> 1

        return output
        