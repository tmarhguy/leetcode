class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        for i in range(len(min(strs, key = len))):
            if all(word[i] == strs[0][i] for word in strs):
                answer += strs[0][i]
            else:
                return answer
        return answer
        
        """

        prefix = strs[0]

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
        """