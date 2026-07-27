import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        # declare the heap & k
        self.heap = []
        self.k = k

        # populate the heap
        for num in nums:
            heapq.heappush(self.heap, num)

        # keep only the largest k nums in the heap
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        
        # push to the heap
        heapq.heappush(self.heap, val)

        # if the heap's length exceeds k, pop the smallest from the heap
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]
        
