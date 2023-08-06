class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        dp[0] = 0
        for i in range(n + 1):
            if i % 2 == 0:
                # a number multiplied by 2 has the same number of ones just shifted to the left
                # i.e. 10 (1010) => 5 (101)
                dp[i] = dp[i // 2]
            else:
                # if its an odd number then it has a 1 at the Least Significant Bit
                # i.e. 11 (1011) => 10 (1010)
                dp[i] = dp[i - 1] + 1
        return dp