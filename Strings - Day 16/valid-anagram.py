# https://leetcode.com/problems/valid-anagram/

# TC - O(N), SC - O(N)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        dic={}
        
        for c in s:
            if c in dic:
                dic[c]+=1
            else:
                dic[c]=1
        
        for c in t:
            if c in dic:
                dic[c]-=1
            else:
                return False
        
        for k in dic:
            if dic[k]!=0:
                return False
        
        return True