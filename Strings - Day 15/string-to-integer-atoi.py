# https://leetcode.com/problems/string-to-integer-atoi/

# Best Code: https://leetcode.com/problems/string-to-integer-atoi/discuss/4673/60ms-python-solution-OJ-says-this-beats-100-python-submissions

# TC - O(N), SC - O(1)

class Solution:
    def myAtoi(self, s: str) -> int:
        n=len(s)
        if n==0:
            return 0

        negative=False
        otherchars=['+','-']
        ans=0
        idx=0
        for c in s:
            if c==' ':
                idx+=1
            else:
                break
        
        if idx>=n:
            return 0
        
        if s[idx]=='-':
            negative=True
        if s[idx] in otherchars:
            idx+=1
            if idx>=n:
                return 0
        
        u=1
        
        for i in range(idx,n):
            val=ord(s[i])-ord('0')
            if val>=0 and val<=9:
                ans*=u
                ans+=val
                u=10
            else:
                break
        
        if ans>(2**31)-1 or (ans>(2**31) and negative):
            ans=(2**31)-1 if not negative else (2**31)
        
        return 0-ans if negative else ans