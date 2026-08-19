class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights) - 1
        curMax = 0
        curArea = 0
        curHeight = 0

        while l < r:
            # first get the current height at our indexes
            if heights[l] < heights[r]:
                curHeight = heights[l]
            else:
                curHeight = heights[r]
            
            # then compute area for our current index and update if necessary
            curArea = curHeight * (r - l)
            curMax = max(curArea, curMax)

            # Check whether to increment left or increment right

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
    
        return curMax
        