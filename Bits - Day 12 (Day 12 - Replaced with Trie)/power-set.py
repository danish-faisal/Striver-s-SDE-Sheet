# https://leetcode.com/problems/subsets/
# https://practice.geeksforgeeks.org/problems/power-set4302/1#
# https://www.geeksforgeeks.org/power-set/

# power-set of a set with n-elements will contain 2^n elements
# so all the Subsets can be obtained from 0 to (2^n -1) combination of bits 
# where each 1 corresponds to selecting an element and 0 to not-selecting
class Solution:
	def AllPossibleStrings(self, s):
        # get length of string
		n=len(s)
        # resultant array
		res=[]
        # In range of 0 to 2^n -1
		for i in range(0,(1<<n)):
            # to store sub-string of each iteration
		    substr=""
            # in range 0 to n-1 (the indexes of characters in the string)
		    for j in range(0,n):
                # check if the bit at index j in set by doing bit-wise and with 2^i
		        if i & (1<<j):
                    # add the character at index j to the sub-string
		            substr+=s[j]
            # to skip empty string
		    if len(substr)>0:
                # add the sub-string of the iteration to resultant-array
                res.append(substr)
        # sorted -> to return substrings in lexical order (alphabetical)
	    return sorted(res)