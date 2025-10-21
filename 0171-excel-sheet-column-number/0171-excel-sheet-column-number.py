class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        answer = 0
        columnTitle = columnTitle[::-1]

        for i in range(len(columnTitle)):
            answer += (ord(columnTitle[i]) - 64) * 26 ** i

        return answer
        