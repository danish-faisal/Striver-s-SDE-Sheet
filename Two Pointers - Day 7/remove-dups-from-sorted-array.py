# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 2nd ptr
        j=0
        # iterate with 1st ptr
        for i in range(len(nums)):
            # if value at n==value at n-1, skip this iteration
            if i!=0 and nums[i]==nums[i-1]:
                continue
            # else place the new number at 2nd ptrs indes
            nums[j]=nums[i]
            # incr 2nd ptr
            j+=1
        # return 2nd ptr as it'll be at nth index where 0 to (n-1) are non-repeated digits
        return j