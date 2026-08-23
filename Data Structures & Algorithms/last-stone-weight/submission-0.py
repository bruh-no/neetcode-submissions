class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        maxHeap = []

        for stone in stones:
            heapq.heappush(maxHeap, -stone)

        
        while len(maxHeap) > 1:
            stone1 = -(heapq.heappop(maxHeap))
            stone2 = -(heapq.heappop(maxHeap))
            diff = stone1 - stone2

            if diff == 0:
                continue
            elif diff > 0:
                heapq.heappush(maxHeap, -diff)
            else:
                heapq.heappush(maxHeap, diff)
        
        if len(maxHeap) == 1:
            return -maxHeap[0]
        else:
            return 0


        