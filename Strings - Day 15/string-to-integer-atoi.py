# https://leetcode.com/problems/string-to-integer-atoi/

# Best Code: https://leetcode.com/problems/string-to-integer-atoi/discuss/4673/60ms-python-solution-OJ-says-this-beats-100-python-submissions

# TC - O(N), SC - O(1)

class Solution:
    def myAtoi(self, s: str) -> int:
        n=len(s)
        if n==0:
            return 0

        negative=False      # flag to mark if negative-no
        otherchars=['+','-']
        ans=0
        idx=0
        for c in s:         # check for spaces and skip them
            if c==' ':
                idx+=1
            else:
                break
        
        if idx>=n:
            return 0
        
        if s[idx]=='-':        # check the char after spaces if its a + or - sign
            negative=True
        if s[idx] in otherchars:
            idx+=1
            if idx>=n:
                return 0
        
        u=1
        
        for i in range(idx,n):          # check if the string after spaces and sign starts with a number
            val=ord(s[i])-ord('0')      # if a no. then the diff b/w ascii value of curr-char and '0' char  will be between 0 and 9
            if val>=0 and val<=9:
                ans*=u
                ans+=val
                u=10
            else:
                break
        
        if ans>(2**31)-1 or (ans>(2**31) and negative):         # for too high and too low no.s
            ans=(2**31)-1 if not negative else (2**31)
        
        return 0-ans if negative else ans