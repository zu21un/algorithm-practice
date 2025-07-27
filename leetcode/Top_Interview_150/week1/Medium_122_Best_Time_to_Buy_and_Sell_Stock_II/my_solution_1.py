class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = -1
        flow = -1
        
        profit = 0

        for i in range(1, len(prices)):
            current = prices[i]
            before = prices[i - 1]

            if current == before:
                continue

            current_flow = 1 if current - before > 0 else -1
            
            if flow < 0 and current_flow > 0:
                # buy
                buy_price = before
            elif flow > 0 and current_flow < 0:
                # sell
                profit += before - buy_price
                buy_price = -1

            # update graph flow
            flow = current_flow
        
        # sell if bought
        if buy_price >= 0:
            profit += prices[-1] - buy_price


        return profit
                
        