class Solution:
    # the first iterated number should be lesser than the upcoming numbers
    # the day to buy (index) should be lesser than the day to sell (index)
    def maxProfit(self, prices: List[int]) -> int:
        final = 0
        max_value = prices[-1]
        for i in range(len(prices)-1,-1,-1):
            max_value = max(max_value,prices[i])
            final = max(final,max_value - prices[i])
        return final
        