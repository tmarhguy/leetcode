class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        s_min = len(min(strs))
        state = False

        for i in range(s_min):
            state = all(word[i] == strs[0][i] for word in strs)
            if state:
                answer += strs[0][i]
            else:
                return answer
        return answer
        