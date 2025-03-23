class Solution(object):
    def isValid(self, s):
        brack = {')':'(','}':'{',']':'[' }
        s_stack = []

        if len(s) % 2 == 1: return False

        for char in s:
            if char not in brack.keys():
                s_stack.append(char)
            else:
                if len(s_stack) > 0:
                    if brack[char] == s_stack[-1]:
                        s_stack.pop()
                    else:
                        return False
                else:
                    return False
        return True if len(s_stack) == 0 else False