class Solution:
    def isValid(self, s: str) -> bool:

        valid = {"(":")","{":"}","[":"]"}
        stack = []

        for char in s:
            if char in valid:
                stack.append(char)
            else:
                if stack and char == valid[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return True and not stack
        