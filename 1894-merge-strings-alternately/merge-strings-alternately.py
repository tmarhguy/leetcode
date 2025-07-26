class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ""
        size = min(len(word1),len(word2))

        for i in range(size):
            answer += word1[i]
            answer += word2[i]
        
        if size == len(word1):
            return answer + word2[size:]
        else:
            return answer + word1[size:]
        