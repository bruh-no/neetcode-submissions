class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures) # Initialize result
        stack = [] # Initialize stack

        # Iterate through temperatures
        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]] < temp:
                    index = stack.pop()
                    res[index] = i - index
                
                stack.append(i)
        
        return res
