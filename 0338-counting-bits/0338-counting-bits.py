class Solution:
    def countBits(self, n: int) -> List[int]:
        c = 0
        answer = [0]

        for i in range(1,n+1):
            while i:
                i &= (i - 1)
                c += 1
            answer.append(c)
            c = 0
        return answer
        