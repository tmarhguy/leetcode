class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_result = {}

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord("a")] += 1
            
            key = tuple(count)

            if key not in hash_result:
                hash_result[key] = [word]
            else:
                hash_result[key].append(word)
        
        return list(hash_result.values())
        """

        hash_result = defaultdict(list)

        for word in strs:

            count = [0] * 26

            for char in word:
                count[ord(char) - ord("a")] += 1

            key = tuple(count)

            hash_result[key].append(word)

        return list(hash_result.values())
        """