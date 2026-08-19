class Solution:
    def search(self, nums: List[int], target: int) -> int:

        res = -1
        n = len(nums)
        l, r = 0, n - 1

        while l <= r:
            if nums[l] == target:
                return l
            
            if nums[r] == target:
                return r
            
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        
        return res