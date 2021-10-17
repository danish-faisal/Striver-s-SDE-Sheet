# https://leetcode.com/problems/count-and-say/

# TC - O(N), SC - Auxillary O(N)

class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:        # base case
            return "1"
        
        prev=self.countAndSay(n-1)
        res=""          # Initialize curr-term in series
        cnt=1           # Initialize count of matching chars
        
        for i in range(len(prev)):
            if i==len(prev)-1 or prev[i]!=prev[i+1]:        # If current character doesn't match (or) curr-char is the last in the str
                res+=str(cnt)+prev[i]                       # Append prev[i] & count of prev[i] to temp
                cnt=1                                       # Reset count
            else:
                cnt+=1                                      # If matches, then increment count of matching characters
        
        return res