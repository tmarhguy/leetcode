class Solution:
    def maxDifference(self, s: str) -> int:
        temp = set(list(s))
        maxx, minn = 0, float('inf')
        c = 0
        
        for char in temp:
            c = s.count(char)
            if c % 2 == 1 and c > maxx:
                maxx = c
            elif c % 2 == 0 and c < minn:
                minn = c
        return int(maxx - minn)

            

        