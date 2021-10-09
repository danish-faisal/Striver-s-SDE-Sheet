# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        # create hashmap of roman numerals
        romans={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        ans=romans[s[-1]]   # add the val of last char to result

        for i in range(len(s)-2,-1,-1):     # start traversing in reverse-order from 2nd last char
            curr=romans[s[i]]       # get the int-val of current roman-char
            nxt=romans[s[i+1]]      # get the int-val of roman-char next to curr-char
            
            if curr<nxt:        # if curr-val < nxt-val, the no. is like IV,IX,XL,XC.....; so we should subtract
                ans-=curr
            else:               # else just add the curr-val to the ans
                ans+=curr
        
        return ans