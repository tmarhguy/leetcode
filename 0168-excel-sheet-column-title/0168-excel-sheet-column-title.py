class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""

        while columnNumber > 0:
            columnNumber -= 1
            temp = columnNumber%26
            result = chr(temp + 65) + result

            columnNumber = columnNumber//26

        return result