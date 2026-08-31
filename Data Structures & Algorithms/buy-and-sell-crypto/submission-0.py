class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit = 0
        for p in prices:
            if p < lowest:
                lowest = p
            if (p-lowest) > profit:
                profit = (p-lowest)
        return profit
        