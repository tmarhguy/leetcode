class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = defaultdict(int)

        for char in s:
            s_map[char] += 1
        
        for char in t:
            s_map[char] -= 1

        return all(value == 0 for value in s_map.values())
        