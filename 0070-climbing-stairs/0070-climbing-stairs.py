class Solution:
    def climbStairs(self, n: int) -> int:
        #Algo is same as fib, DP solution O(N)
        stair_lst = [0] * (n+1)
        for i in range(n + 1):
            if i <= 2:
                stair_lst[i] = i
            else:
                stair_lst[i] = stair_lst[i - 1] + stair_lst[i - 2]
        print(stair_lst)
        return stair_lst[n]