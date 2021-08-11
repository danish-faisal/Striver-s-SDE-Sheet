# https://leetcode.com/problems/single-element-in-a-sorted-array/

# Brute Force Approach: linear search O(n)

# Optimal Approach
# Observation:
# For elements before the single element in the array => new element will be at an even-index and its copy will be at odd-index next to it
# For elements after the single element in the array => new element will be at an odd-index and its copy will be at even-index next to it
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # initialize low & high
        low = 0
        high=len(nums)-2
        # until low<=high -> keep shrinking down the array
        while low<=high:
            mid=(low+high)//2
            # if 'mid' is an odd-index, 'mid^1' will give the even-index before it
            # if 'mid' is an even-index, 'mid^1' will give odd-index next to it

            if nums[mid]==nums[mid^1]:  # will be true for left half -> nums[even]==nums[odd(even+1)]
                low=mid+1               # => as we're on the left-half of the single-element, cut the left-half
            else:
                high=mid-1              # as we're on the right-half, cut the right-half
        
        # when low>high => required element will be at nums[low]
        return nums[low]