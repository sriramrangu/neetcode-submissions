class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        b = {
            ']' : '[',
            ')' : '(',
            '}' : '{'
        }
        for c in s:
            if  stack and c in b and stack[-1] == b[c] :
                stack.pop()
            else:
                stack.append(c)
        if stack:
            return False
        else : 
            return True