class Solution:
    def isHappy(self, n: int) -> bool:
        def happy(n):
            answer = 0
            for char in str(n):
                answer += int(char) ** 2
            return answer
        
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = happy(n)

        return n == 1
        