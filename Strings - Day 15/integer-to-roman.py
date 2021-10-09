# https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        # roman literals of commonly utilised least-subsets possible
        romans=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        # integer values of the same
        intCode=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        
        ans=''      # resultant variable

        for i in range(len(intCode)):   # iterate over the intCodes arr
            while num>=intCode[i]: 
                ans+=romans[i]          # keep adding val at intCode[i] 
                num-=intCode[i]         # subtract the same from given-num so that break codn of num<intCode[i] is reached
        
        return ans