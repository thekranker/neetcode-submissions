class Solution:
    def countBits(self, n: int) -> List[int]:

        if n == 0:
            return [0]

        if n == 1:
            return [0, 1]

        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        offset = 2

        for i in range(3, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]

        output = []
        for count in dp:
            output.append(count)
        
        return output




        
        