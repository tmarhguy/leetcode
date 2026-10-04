class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        hash_map = defaultdict(int)

        state = 0

        for i in range(len(s)):
            hash_map[s[i]] += 1
            hash_map[t[i]] -= 1


        return all(value == 0 for value in hash_map.values())

        