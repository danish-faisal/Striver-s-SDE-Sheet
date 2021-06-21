# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # intialize max sub array as max element from array
        max_so_far = max(nums)

        max_ends_here = 0
        n = len(nums)
        
        for i in range(0,n):
            # keep adding array elements
            max_ends_here+=nums[i]
            # if sum of numbers calculated till now, exceeds max sum pbtained till now
            # replace max till now with sum obtained till now
            if max_so_far<max_ends_here:
                max_so_far=max_ends_here
            # if sum of elements goes negative, keep/replace the sum of elements obtained to 0
            if max_ends_here<0:
                max_ends_here = 0
        return max_so_far