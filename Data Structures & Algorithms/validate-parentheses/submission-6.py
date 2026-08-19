class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) == 1:
            return False

        stack = []
        mappedKeys = {")" : "(", "}" : "{", "]" : "["}

        for c in s:
            if c in mappedKeys:
                if stack and stack[-1] == mappedKeys[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if not stack:
            return True
        else: return False

            



        