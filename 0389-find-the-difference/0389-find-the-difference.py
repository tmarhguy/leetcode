class Solution(object):
    def findTheDifference(self, s, t):
        s = list(s); t = list(t)

        while len(s) > 0:
            for a in s:
                s.remove(a)
                t.remove(a)


        return (''.join(t))