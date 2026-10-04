class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        hash_map = defaultdict(int)

        state = 0

        for i in range(len(s)):
            hash_map[s[i]] += 1
            hash_map[t[i]] -= 1

        for _, value in hash_map.items():
            if value != 0: return False

        return True

        