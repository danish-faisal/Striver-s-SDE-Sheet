# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs==None or len(strs)==0:
            return ""
        
        prefix=strs[0]      # assume the first-word to be the complete prefix in others
        
        # start iterating from 2nd word in the list
        for i in range(1,len(strs)):
            # until the string 'prefix' is completely found in the curr-word under iteration
            # keep removing the last-char from prefix and check again 
            while strs[i].find(prefix)!=0:
                prefix=prefix[:-1]
        
        return prefix