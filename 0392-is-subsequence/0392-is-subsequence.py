class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_point = 0
        s_point = 0
        t_size = len(t)
        s_size = len(s)

        while t_point < t_size and s_point < s_size:
            if s[s_point] == t[t_point]:
                s_point += 1
                t_point += 1
            else:
                t_point += 1

        if s_point != s_size:
            return False
        else:
            return True

        