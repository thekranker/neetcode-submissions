class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:


        minCost = 0
        cache = {}

        def dfs(pos: int):
            if pos >= len(cost):
                return 0
            if pos in cache:
                return cache[pos]
            result = cost[pos] + min(dfs(pos+1), dfs(pos+2))
            cache[pos] = result
            return result
        
        return min(dfs(0), dfs(1))