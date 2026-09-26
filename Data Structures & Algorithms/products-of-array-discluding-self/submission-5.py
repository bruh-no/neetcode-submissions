class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #Initialize Result
        res = [1] * len(nums)

        #First get total product, skipping 0s
        numZeros = 0
        totProduct = 1
        numZeros = 0

        for num in nums:
            if num == 0:
                numZeros += 1
                pass
            else:
                totProduct = totProduct * num
        
        # Early result if number of zeros greater than 2
        if numZeros >= 2:
            return [0] * len(nums)
        
        # If only one zero, the nums[i] where 0 is totProduct and rest 0
        elif numZeros == 1:
            for i, num in enumerate(nums):
                if num == 0:
                    res[i] = totProduct
                else:
                    res[i] = 0
        
        else:
            for i, num in enumerate(nums):
                res[i] = int(totProduct / num)

        
        return res