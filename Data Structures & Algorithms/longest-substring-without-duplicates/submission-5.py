class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #Check for a string
        if not s:
            return 0

        if len(s) == 1:
            return 1
        
        #Initialize left and right pointers and result and set for seen
        maxLen = 0
        l, r = 0, 1
        seen = set()
        seen.add(s[l])


        #Loop through string while r is valid and if a letter has been seen, move l over 1
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            maxLen = max(maxLen, r - l + 1)
            seen.add(s[r])
            r += 1
        
        return maxLen





        