class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_map = defaultdict(int)

        for i in range(len(s)):
            s_map[s[i]] += 1
            s_map[t[i]] -= 1
            
        return all(value == 0 for value in s_map.values())
        