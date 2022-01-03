# https://leetcode.com/problems/divide-two-integers/

# https://leetcode.com/problems/divide-two-integers/discuss/1084803/Python-bitwise

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = 0
        xx, yy = abs(dividend), abs(divisor)
        # 32 -> as an Integer would be of 32 bits
        for i in range(32, -1, -1):
            # look for Largest Multiple of Divisor < Dividend
            if xx >= (yy<<i):
                # subtract that Multiple of Divisor from Dividend
                # xx -> will now store th remainder
                xx -= (yy<<i)
                # ans = Quotient as yy<<i=(Divisor * Quotient) => (1<<i) is the Quotient
                ans += (1<<i)
            # On the remainder repeat the same process
        
        # Check for Signs
        if (dividend>0 and divisor<0) or (dividend<0 and divisor>0): 
            ans = -ans
        
        # Check and Return Max Int and Min Int in case of very large numbers
        return min(2**31-1, max(-2**31, ans))