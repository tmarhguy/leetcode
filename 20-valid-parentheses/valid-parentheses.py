class Solution(object):
    def isValid(self, s):
        brack = {')':'(','}':'{',']':'[' }
        array = []
        for c in s:
            if c in brack:
                if array and array[-1] == brack[c]:
                    array.pop()
            
                else:
                    return False
            else:
                array.append(c)
            
        return True if not array else False