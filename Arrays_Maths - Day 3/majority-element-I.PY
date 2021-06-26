# https://leetcode.com/problems/majority-element/


# if an element exist >n/2 times -> after sorting it should be available at n/2 index even if its the smallest ot largest element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # sort the array
        nums.sort()
        # return element at mid-index
        return nums[len(nums)//2]