class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        n = len(heights)

        for i in range(n):
            cur_min = float('inf')
            for j in range(i, n):
                cur_min = min(cur_min, heights[j])
                width = j - i + 1
                maxArea = max(maxArea, cur_min * width)
            
        return maxArea


