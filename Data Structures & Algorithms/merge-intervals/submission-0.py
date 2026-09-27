class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Initialize result and sort intervals (makes sure we dont miss anything)
        intervals.sort()
        res = []

        # Iterate through each interval, if it has an existing overlap, we edit the previous interval to update its bounds
        # If theres no overlap, just add the interval 

        for int in intervals:

            if len(res) == 0 or int[0] > res[-1][1]:
                res.append(int)
            else:
                res[-1][1] = max(res[-1][1], int[1])
            
        return res
            


        