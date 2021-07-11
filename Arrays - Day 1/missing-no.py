# https://leetcode.com/problems/missing-number/
"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # sum of n natural numbers + 0
        sumN = (n * (n+1))/2
        arrSum = 0
        
        # calc sum of no.s in array
        for num in nums:
            arrSum += num
        # arrSum - sumN will result in missing number in the range 0-n
        return int(sumN - arrSum)