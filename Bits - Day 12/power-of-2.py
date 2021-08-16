# https://leetcode.com/problems/power-of-two/

# Approach 2: Using (n & (n-1))==0
"""
It's figuring out if n is either 0 or an exact power of two.

It works because a binary power of two is of the form 1000...000 and subtracting one will give you 111...111. Then, when you AND those together, you get zero, such as with:

  1000 0000 0000 0000
&  111 1111 1111 1111
  ==== ==== ==== ====
= 0000 0000 0000 0000
"""
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and (n & (n-1))==0


# Approach 1: If 'n' is a power of 2 -> its log base 2 will be a definte integer; if its an integer it ceil and floor value will be same
# if they are not same then 'n' is not a power of 2
import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        logged=math.log2(n)
        return math.ceil(logged)==math.floor(logged)