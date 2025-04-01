class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        result = []
        pre, post = 1,1

        for i in range(len(nums)):
            pre *= nums[i]
            post *= nums[len(nums)-1-i]
            prefix.append(pre)
            postfix.append(post)

        postfix = postfix[::-1]
        print("prefix", prefix)
        print("postfix", postfix)
        

        result.append(postfix[1])
        for i in range(1,len(nums)-1):
            result.append(prefix[i-1] * postfix[i+1])

        result.append(prefix[-2])

        return result