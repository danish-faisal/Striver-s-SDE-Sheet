# https://practice.geeksforgeeks.org/problems/count-total-set-bits-1587115620/1#
# https://www.geeksforgeeks.org/count-total-set-bits-in-all-numbers-from-1-to-n-set-2/

#Function to return sum of count of set bits in the integers from 1 to n.
class Solution:
    # to get the larget power of 2 < n
    def largestPowerOf2InRange(self,n):
        x=0
        # while 2^x <= n
        while (1<<x)<=n:
            x+=1
        # x-1 => x will be higher when the condition fails, so -1 to get the prev-value
        return x-1
        
    def countSetBits(self,n):
        # in case of single-bit: 0 or 1
        if n<=1:
            return n

        # x = largest power of 2 < n
        x = self.largestPowerOf2InRange(n)

        # formula to get all the 1s under a power of 2 -> 2^(x-1) * x
        # for 8 -> 1000 => total 1s from L->R will be = (8/2+8/2+8/2) = 12 = 4*3 = 2^(3-1)*3 => 2^(x-1)*x
        btill2x=x*(1<<(x-1))

        # MSB of numbers from (2^x)->n => n-(2^x)+1
        # if n=11,x=3,2^x=8 => total MSBs = 11-8+1=3+1=4
        # removal of MSB to shrink the numbers' size for calculation
        msb2xton=n-(1<<x)+1

        # remaining no.s, after removal of MSB => (n-2^x) => new n
        rest=n-(1<<x)
        
        # recursive-call with the new n
        return btill2x+msb2xton+self.countSetBits(rest)