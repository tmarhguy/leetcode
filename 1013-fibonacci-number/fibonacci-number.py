class Solution:
    def fib(self, n: int) -> int:
        dict_ans = {0:0,1:1}
        if n in dict_ans:
            return dict_ans[n]
        else:
            answer = self.fib(n-1) + self.fib(n-2)
            dict_ans[n] = answer
            return answer
        