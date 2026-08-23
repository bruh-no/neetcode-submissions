class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        minHeap = []
        heapq.heapify(minHeap)

        for i, point in enumerate(points):
            dist = (point[0]**2 + point[1]**2)**(0.5)
            heapq.heappush(minHeap, (dist, point))

        res = []

        for i in range(k):
            dist, point = heapq.heappop(minHeap)
            res.append(point)
        
        return res
        
        