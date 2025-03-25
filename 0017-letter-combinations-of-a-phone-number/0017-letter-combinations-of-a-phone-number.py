class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        def combine(a,b):
            letters = {"1":" ","2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz","0":" "}
            result = []

            for i in range(len(letters[a])):
                for j in range(len(letters[b])):
                    result.append((letters[a][i] + letters[b][j]).strip())
            return result
        

        def combine2(a,b):
            result = []
            for element in a:
                for other in b:
                    result.append(element+other)
            return result


        if len(str(digits)) == 0:
            return []

        elif len(str(digits)) == 1:
            temp = combine("1",str(digits))
            return temp
        elif len(str(digits)) == 2:
            temp = combine(str(digits)[0],str(digits)[1])
            return temp
        elif len(str(digits)) == 3:
            temp = combine(str(digits)[0],str(digits)[1])
            temp2 = combine("1",str(digits)[2])
            return combine2(temp,temp2)
        elif len(str(digits)) == 4:
            temp = combine(str(digits)[0],str(digits)[1])
            temp2 = combine(str(digits)[2],str(digits)[3])
            return combine2(temp,temp2)


        