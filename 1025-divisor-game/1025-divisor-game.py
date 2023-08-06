class Solution:
    def divisorGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        dp[0] = False
        dp[1] = False
        for i in range(2, n + 1):
            for j in range(1, i):
                if i % j == 0:
                    #if dp[i-j] is a losing position
                    if not dp[i-j]:
                        dp[i] = True
                        continue
        return dp[n]
                        
                    
        
        