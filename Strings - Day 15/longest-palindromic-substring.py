# https://leetcode.com/problems/longest-palindromic-substring/

# TC - O(n^2), SC - O(1)

class Solution:
    def expandAroundCenter(self, s, left, right):
        while(left>=0 and right<len(s) and s[left]==s[right]):
            left-=1
            right+=1
        
        return right-left-1     # return length of the substr
    
    def longestPalindrome(self, s: str) -> str:
        if s==None or len(s)==0:
            return ""
        end=0
        start=0
        
        for i in range(len(s)):                         # iterate over each char in the given-str, to expand around it
            len1=self.expandAroundCenter(s, i, i)       # for odd-len strs
            len2=self.expandAroundCenter(s, i, i+1)     # for even-len strs
            lenf=max(len1, len2)                        # lenf(final-len) = max(len1,len2)
            
            if (lenf>end-start):
                start=i-(lenf-1)//2         # from the obtained lenf and the curr-idx 'i', calc the start-point
                end=i+lenf//2               # calc the end-point og the palindromic-substr
        
        return s[start:end+1]           # return the palindromic-substr