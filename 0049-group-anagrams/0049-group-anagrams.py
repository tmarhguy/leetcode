class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1: return [strs]
        hash_set = defaultdict(list)
        char_list = [0] * 26

        for word in strs:
            for char in word:
                char_list[ord(char) - ord('a')] += 1
            hash_set[tuple(char_list)].append(word)
            char_list = [0]*26

        return list(hash_set.values())

        
        