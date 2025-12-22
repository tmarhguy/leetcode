class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1 or numRows >= len(s): return s
        
        hlist = [[] for _ in range(numRows)]
        n = 0
        idx = 0
        numRows -= 1

        while n < len(s):
            idx = numRows - abs((n % (2 * numRows))-numRows)
    
            hlist[idx].append(s[n])
            n += 1

        result = ["".join(l) for l in hlist]

        return "".join(result)


        