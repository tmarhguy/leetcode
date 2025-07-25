class Solution:
    def romanToInt(self, s: str) -> int:
        answer,i = 0,0
        nums = {'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000}
        while i < len(s) - 1:
            if nums[s[i]] >= nums[s[i+1]]:
                answer += nums[s[i]]
            else:
                answer -= nums[s[i]]
            i += 1
        return answer + nums[s[i]]






        return answer
