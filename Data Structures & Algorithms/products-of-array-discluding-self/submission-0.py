class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [None] * len(nums)

        for i in range(len(nums)):
            result = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                result = result * nums[j]
            output[i] = result
        return output
        