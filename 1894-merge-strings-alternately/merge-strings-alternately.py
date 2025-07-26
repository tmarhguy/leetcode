class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = []
        size = min(len(word1),len(word2))

        for i in range(size):
            answer.append(word1[i])
            answer.append(word2[i])
        
        if size == len(word1):
            return ''.join(answer) + word2[size:]
        else:
            return ''.join(answer) + word1[size:]
        