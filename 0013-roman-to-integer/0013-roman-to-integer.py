class Solution:
    def romanToInt(self, s: str) -> int:
        seen = []
        answer = 0
        nums = {'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000}

        for num in s:
            seen.append(nums[num])

        print("seen", seen)

        i = 0

        while i < len(seen) - 1:
            if seen[i] >= seen[i+1]:
                answer += seen[i]
            else:
                answer -= seen[i]
            i += 1
        return answer + seen[i]






        return answer
