class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        
        prefix = [1] * size
        postfix = [1] * size
        result = []
        pre, post = 1,1

        for i in range(size):
            pre *= nums[i]
            post *= nums[size - 1 - i]

            prefix[i] = pre
            postfix[size - i - 1] = post

        result.append(postfix[1])
        
        for i in range(1,size-1):
            final = prefix[i-1] * postfix[i+1]
            result.append(final)
        
        result.append(prefix[-2])

        return result