class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        prices[0] = 0
        for i in range(1, len(prices)):
            current = prices[i]
            prices[i] -= min_price
            min_price = min(min_price, current)
        
        return max(prices)