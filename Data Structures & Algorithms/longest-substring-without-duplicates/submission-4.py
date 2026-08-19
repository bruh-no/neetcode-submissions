class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0

        maxStr = 0
        seen = set()

        l, r = 0, 0

        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            maxStr = max(maxStr, r - l + 1)
            r += 1

        
        return maxStr


        