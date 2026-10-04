class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        hash_map = defaultdict(list)

        for word in strs:

            temp = [0] * 26 

            for char in word:
                temp[ord(char) - ord('a')] += 1

            hash_map[tuple(temp)].append(word)
        
        return list(hash_map.values())

        