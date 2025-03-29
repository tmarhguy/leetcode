class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = -1 + 2**31
        INT_MIN = -2**31
        state = 1

        if x < 0:
            state = -1

        x = abs(x)

        x = str(x)

        x = x[::-1]

        x = int(x)

        x *= state
        
        if x < INT_MIN or x > INT_MAX:
            return 0
        else:
            return x
        