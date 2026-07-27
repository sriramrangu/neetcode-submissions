class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        b = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }
        for c in s :
            if stack and c in b and b[c] == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        if stack:
            return False
        return True        