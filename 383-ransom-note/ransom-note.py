class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote): return False

        mag_dict = defaultdict(int)

        for char in magazine:
            mag_dict[char] += 1

        for char in ransomNote:
            if mag_dict[char] == 0:
                return False
            mag_dict[char] -= 1

        return True
        