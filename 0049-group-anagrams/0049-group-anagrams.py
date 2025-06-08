class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_set = defaultdict(list)
        key = [0 for _ in range(26)]

        for word in strs:
            for char in word:
                key[ord(char) - ord('a')] += 1
            key = tuple(key)
            hash_set[key].append(word)
            key = [0 for _ in range(26)]
            
        return list(hash_set.values())

        