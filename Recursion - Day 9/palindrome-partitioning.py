# https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # resultant array
        ans=[]
        # initial call of the recursive function
        self.findPalindromes(0,s,[],ans)
        return ans
    
    # function to check if the given string is a palindrome
    def isPalindrome(self,sub,start,end):
        while start<=end:
            if sub[start]!=sub[end]:
                return False
            start+=1
            end-=1
        return True
    
    # recursive-func to generate palindromes and check
    def findPalindromes(self,idx,stn,curr,ans):
        # if idx reached till the end of the given string
        # base case -> indicates that all the partitioned strings are plaindromes and no more to check so add the partitions to ans
        if idx==len(stn):
            ans.append(curr[:])
            return
        # iterate over the string and divide it into substrings
        for i in range(idx,len(stn)):
            # if the sub-str is palindrome
            if self.isPalindrome(stn,idx,i):
                # add it to the curr-arr, holding the partitions
                curr.append(stn[idx:i+1])
                # make the recursive call -> to divide rest of the characters in sub-strings
                # with curr-arr holding the palindromic partitions of the earlier characters
                self.findPalindromes(i+1,stn,curr,ans)
                # remove the added sub-str to not have it in next iteration with new division of characters for sub-strs
                curr.pop()