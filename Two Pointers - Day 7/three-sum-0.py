# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3:
            return [] 
        n=len(nums)
        res=[]
        # sort the array
        nums.sort()
        for i in range(n-2):
            # skip the number if it's same as the previous number
            # to avoid checking the same-no again
            if i>0 and nums[i]==nums[i-1]:
                continue
            # 2 ptrs -> left & right -> left = first in remaining list to iterate, right=last index
            l,r=i+1,n-1

            while l<r:
                s=nums[i]+nums[l]+nums[r]
                # if sum<0, move to greater-nos in sorted list
                if s<0:
                    l+=1
                # if sum>0, move to smaller-nos in sorted list
                elif s>0:
                    r-=1
                # if sum=0
                else:
                    # append the digits as a result
                    res.append([nums[i],nums[l],nums[r]])
                    # skip same-nos in the list
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
        return res