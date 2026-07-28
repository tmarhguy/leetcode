class Solution(object):
    def shuffle(self, nums, n):
        x = nums[:n]
        y = nums[n:]
        ans = [0 for i in range(2 * n)]

        for i in range(2*n):
            if i % 2 == 0:
                ans[i] = x[i/2]
            else:
                ans[i] = y[(i-1)/2]
        return ans