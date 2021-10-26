# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
# https://www.geeksforgeeks.org/minimum-insertions-to-form-a-palindrome-dp-28/

# DP based Optimal Soln: TC - O(N^2), SC - O(N^2)

class Solution:
    # LCS = Longest Commn Subsequence
    """ Returns length of LCS for X[0..m-1], Y[0..n-1]. See http://goo.gl/bHQVP for details of this function """
def lcs(self, X, Y, m, n) :
    L = [[0 for i in range(n + 1)] for j in range(m + 1)]

    """ Following steps build L[m + 1, n + 1] in bottom up fashion. Note that L[i, j]
    contains length of LCS of X[0..i - 1] and Y[0..j - 1] """
    for i in range(m + 1):
        for j in range(n + 1):
            if (i == 0 or j == 0) :
                L[i][j] = 0
 
            elif (X[i - 1] == Y[j - 1]) :
                L[i][j] = L[i - 1][j - 1] + 1
            else :
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
 
    """ L[m,n] contains length of LCS for X[0..n-1] and Y[0..m-1] """
    return L[m][n]
     
# LCS based function to find minimum number of insertions
def minInsertions(self, Str: str) -> int:
    # Using charArray to reverse a String
    n=len(Str)
    charArray = list(Str)
    charArray.reverse()
    revString = "".join(charArray)
     
    # The output is length of string minus length of lcs of str and it reverse
    return (n - lcs(Str, revString , n, n))

# Recursive soln: TC - O(2^N), SC - O(2^N)

import sys

class Solution:
    def minInsertions(self, s: str) -> int:
        return self.minInsertionsHelper(s, 0, len(s)-1)
    
    def minInsertionsHelper(self, s: str, l: int, h: int) -> int:
        # Base Cases
        if l>h:
            return sys.maxsize
        if l==h:
            return 0
        if l==h-1:
            return 0 if (s[l]==s[h]) else 1
        
        # Check if the first and last characters are same. On the basis of the comparison result, decide which subrpoblem(s) to call
        if s[l]==s[h]:
            return self.minInsertionsHelper(s, l+1, h-1)
        else:
            return min(self.minInsertionsHelper(s, l, h-1), self.minInsertionsHelper(s, l+1, h))+1