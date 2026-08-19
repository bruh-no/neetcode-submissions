class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max = 0

        for i in range(len(heights)):
            dist = 0
            for j in range(i +1, len(heights)):
                dist += 1
                height = 0
                if heights[i] > heights[j]:
                    height = heights[j]
                else:
                    height = heights[i]
                if height * dist > max:
                    max = height * dist
        
        return max
