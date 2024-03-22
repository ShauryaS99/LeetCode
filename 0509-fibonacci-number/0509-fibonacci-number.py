class Solution:
    def fib(self, n: int) -> int:
        #DP solution b/c we save previous work O(N)
        fib_lst = [0] * (n + 1)
        for i in range(n + 1):
            if i <= 1:
                fib_lst[i] = i
            else:
                fib_lst[i] = fib_lst[i - 1] + fib_lst[i - 2]
        return fib_lst[n]