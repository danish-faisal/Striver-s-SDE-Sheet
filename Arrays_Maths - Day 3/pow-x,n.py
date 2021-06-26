# https://leetcode.com/problems/powx-n

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # base case, x^0 = 1
        if n == 0:
            return 1
        if n<0:
            return self.myPow(1/x,-n)  # -n -> -(-) -> +n
        
        # x^n = x^(n/2) * x^(n/2), if n is even
        # x^n = x^(n/2) * x^(n/2) * x, if n is odd
        
        half = self.myPow(x,n//2)
        if n%2 == 0:
            return half * half
        else:
            return half*half*x