class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums = sorted(nums)

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            target = -nums[i]
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    if [nums[i], nums[l], nums[r]] in res:
                        pass
                    else:
                        res.append([nums[i],nums[l],nums[r]])
                    l += 1
        
        return res


