class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        pairs = sorted(zip(position, speed), reverse=True)

        currLeadTime = (target - pairs[0][0]) / pairs[0][1]
        fleetCount = 1
        
        for i in range(1, len(pairs)):
            currTime = (target - pairs[i][0]) / pairs[i][1]
            if currTime > currLeadTime:
                fleetCount += 1
                currLeadTime = currTime

        return fleetCount
        