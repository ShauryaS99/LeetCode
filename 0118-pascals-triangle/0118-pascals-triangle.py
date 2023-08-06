class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = []
        for i in range(1, numRows + 1):
            dp.append([1] * i)
        for row in range(len(dp)):
            for j in range(len(dp[row])):
                if j == 0 or j == len(dp[row]) - 1:
                    continue
                elif row > 1:
                    dp[row][j] = dp[row -1][j - 1] + dp[row -1][j]
        return dp
                