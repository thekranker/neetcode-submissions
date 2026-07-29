class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones.sort()
            smashStones = stones[-1] - stones[-2]
            stones.pop()
            stones[-1] = smashStones

        if stones:
            return stones[0]
        return 0
