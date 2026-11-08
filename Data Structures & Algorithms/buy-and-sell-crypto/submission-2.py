class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        min_price = prices[0]
        for i in range(0,n):
            min_price = min(min_price,prices[i])
            profit = max(profit,prices[i]-min_price)
        return profit
