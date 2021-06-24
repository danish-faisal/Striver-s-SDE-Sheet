# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initialize min to +ve infinity
        minPrice = float('inf')
        # initialize max to 0
        maxDiff = 0
        # start iterating over array elements
        for i in range(len(prices)):
            # keep updating min element as we iterate over the array
            if prices[i]<minPrice:
                minPrice = prices[i]
            # calculate difference between current-element and min-ele, to check of we get max-diff and keep updating it
            if prices[i]-minPrice > maxDiff:
                maxDiff = prices[i]-minPrice
        return maxDiff