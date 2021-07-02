# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # removing repeated nums
        numset = set(nums)
        maxc = 0
        for i in numset:
            # checking if i-1 exists -> if it doesn't => it indicates beginning of a new sequence
            if i-1 not in numset:
                # start of sequence
                cnum = i
                # current length of repeating sequence
                cmax = 1
                # iterate to check the succeeding numbers from cnum are in the sequence
                while cnum+1 in numset:
                    # increment the number to check the next
                    cnum+=1
                    # increment sequence length count
                    cmax+=1
                # comparision to have maximum length seen stored in maxc
                maxc = max(maxc,cmax)
        return maxc