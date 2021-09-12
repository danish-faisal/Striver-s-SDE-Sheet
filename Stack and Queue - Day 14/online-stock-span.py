# https://leetcode.com/problems/online-stock-span

# Optimal Approach: TC: O(N), SC: O(N)

class StockSpanner:
    def __init__(self):
        self.stack=[]   # A stack: to keep track of greater-prices
        self.prices=[]  # A prices-arr: to store all the day-to-day prices

    def next(self, price: int) -> int:
        # append each new-price intothe prices array
        self.prices.append(price)
        # get the index of the new-price in the array
        i=len(self.prices)-1
        ans=None    # resultant-var

        # if stakc has values, pop-out indexes having values lesser than the curr-price
        while len(self.stack)!=0 and self.prices[self.stack[-1]]<=self.prices[i]:
            self.stack.pop()

        # if stack is empty: curr-price is greater than all prev-prices
        if len(self.stack)==0:
            ans=i+1
        else:
            # stock-span => curr-price-idx - idx-of-greater-val seen at the top of stack
            ans=i-self.stack[-1]
        # append the curr-index to the stack
        self.stack.append(i)
        
        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

'''
Brute Force Approach: TC: O(N^2), SC: O(1)
For Each Element, check previous indexes using an inner loop
and keep a count of no. of consecutive smaller elements as stock-span
'''