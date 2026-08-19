class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            temp = temperatures[i]
            daysBeen = 0
            tempRes = 0
            for j in range(i + 1, len(temperatures)):
                daysBeen += 1
                if temperatures[j] > temperatures[i]:
                    tempRes = daysBeen
                    break
            res[i] = tempRes
        
        return res