class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        mapped = {"}":"{", "]":"[", ")":"("}

        for c in s:
            if c in mapped.values():
                stack.append(c)
            elif c in mapped.keys():
                if not stack:
                    return False
                pair = stack.pop()
                if pair != mapped[c]:
                    return False
        
        if not stack:
            return True
        else:
            return False


            



        