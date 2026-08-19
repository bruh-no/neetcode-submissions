class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            curTemp = temperatures[i]
            while stack and temperatures[stack[-1]] < curTemp:
                indice = stack.pop()
                res[indice] = i - indice
            stack.append(i)
        
        return res