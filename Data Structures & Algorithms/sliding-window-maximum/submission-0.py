class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        l, r = 0, k - 1
        res = []
        window = []

        while r < len(nums):
            window = nums[l:r + 1]
            res.append(max(window))
            l += 1
            r += 1
            
        
        return res


