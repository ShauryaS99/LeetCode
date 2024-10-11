class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        curr_min = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < curr_min:
                curr_min = prices[i]
            max_profit = max(max_profit, prices[i] - curr_min)
        return max_profit