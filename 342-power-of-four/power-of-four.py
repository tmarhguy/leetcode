class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        n = bin(n)

        if len(str(n)) % 2 == 0:
            return False
        else:
            if str(n)[2] == "1":
                if all(bit == "0" for bit in str(n)[3:]):
                    return True
        return False
        