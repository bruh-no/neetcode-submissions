class Solution:
    def findMin(self, nums: List[int]) -> int:

        stack = []

        for num in nums:

            while stack and stack[-1] > num:
                stack.pop()
            
            stack.append(num)
        
        return stack[0]
        