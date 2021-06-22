# https://leetcode.com/problems/next-permutation/
# [1,2,3] -> [1,3,2]
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=j=len(nums)-1
        # find the breakpoint -> nums[i-1]<nums[i]
        while i>0 and nums[i-1]>=nums[i]:
            i-=1
        # if no breakpoint, return reversed list
        if i==0:
            nums.reverse()
            return
        # k=breakpoint
        k=i-1
        # find element < element at breakpoint
        while nums[j]<=nums[k]:
            j-=1
        # swap ele at nums[k] and nums[k]
        nums[j],nums[k]=nums[k],nums[j]
        # intialize left and right pointer -> breakpoint & end
        l=k+1
        r=len(nums)-1
        # reverse list from breakpoint till end
        while l<=r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1