class Solution:
    def scoreOfString(self, s):
        sum_1 = 0
        
        for i in range(0, len(s)- 1):
            sum_1 += abs(ord(s[i]) - ord(s[i+1]))
        return sum_1
        