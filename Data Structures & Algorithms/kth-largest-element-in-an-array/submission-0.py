import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # build a max heap
        maxHeap = []

        for num in nums:
            heapq.heappush(maxHeap, num)
            
            while len(maxHeap) > k:
                heapq.heappop(maxHeap)
            
        return maxHeap[0]
        