import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # create the max heap
        maxHeap = []
        output = []
        
        # loop through the points list
        for point in points:

            # use the distance formula and populate the max heap
            heapq.heappush(maxHeap, (-1 * math.sqrt(point[0] ** 2 + point[1] ** 2), point))

        # remove the max element when the size fo the heap exceeds k
        while len(maxHeap) > k:
            heapq.heappop(maxHeap)

        # return all the values in the heap in an List[List[int]]
        for val in maxHeap:
            output.append(val[1])
        
        return output