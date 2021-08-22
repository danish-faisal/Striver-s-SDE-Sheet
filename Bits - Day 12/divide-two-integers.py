# https://leetcode.com/problems/divide-two-integers/

# https://leetcode.com/problems/divide-two-integers/discuss/1084803/Python-bitwise
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = 0
        xx, yy = abs(dividend), abs(divisor)
        for i in range(32, -1, -1):
            if xx >= (yy<<i):
                xx -= (yy<<i)
                ans += (1<<i)
        
        if (dividend>0 and divisor<0) or (dividend<0 and divisor>0): 
            ans = -ans
        
        return min(2**31-1, max(-2**31, ans))