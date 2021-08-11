# https://leetcode.com/problems/search-in-rotated-sorted-array/

# Brute Force Approach: Linear Search, O(n)

# Optimal Approach:
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # initialize low & high
        low = 0
        high = len(nums)-1
        # until low<=high
        while low<=high:
            mid=(low+high)//2
            # if nums[mid]=target, return mid-index
            if nums[mid]==target:
                return mid
            # check if left-half is sorted
            if nums[low]<=nums[mid]:
                # check if the target-ele lies in the left half -> if yes reduce the array to left-half
                if target>=nums[low] and target<=nums[mid]:
                    high=mid-1
                # else reduce the array to right-half
                else:
                    low=mid+1
            else:
                # check if the target-ele lies in the right-half -> if yes reduce the array to right-half
                if target>=nums[mid] and target<=nums[high]:
                    low=mid+1
                # else reduce the array to left-half
                else:
                    high=mid-1
        # will return -1 in case the element doesn't exist
        return -1