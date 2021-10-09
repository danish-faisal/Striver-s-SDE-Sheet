# https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        ans=''      # resultant var
        count=0

        for c in reversed(s):       # iterate ove rhte string char-by-char in reverse-order
            if count==1:    # add a space only when count=1
                ans+=' '
            
            if c==' ':      # to ignore extra spaces
                count+=1
                continue
            
            ans+=c          # other all alpha-chars
            count=0         # reset count-var as a new-word starts
                
        ans=ans.strip()     # to remove the extra space added at start & end of string if any
        res=ans.split(' ')  # split the completely reverse string in reverse words
        
        for i in range(len(res)):
            res[i]=res[i][::-1]     # each val in the arr will be a reversed-word, reverse them back to get the aactual word
        
        return " ".join(res)        # join the words with space and return