class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1: return s
        
        hashmap = dict()

        for i in range(numRows):
            hashmap[i] = ""

        n = 0
        idx = 0

        print(hashmap)
        numRows -= 1

        while n < len(s):
            idx = numRows - abs((n % (2 * numRows))-numRows)
    
            hashmap[idx] += s[n]
            print(idx)
            n += 1
        result = list(hashmap.values())

        print(hashmap)
        return "".join(result)


        