class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        buy = float("inf")

        for i in prices:

            if i < buy:
                buy = min(i,buy)

            
            profit = max(profit, i - buy)

        return profit


        