# https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # resultant var
        res=0
        # count var to count consecutive 1s
        count=0
        for i in range(len(nums)):
            # if a 0 is seen, set count to 0
            if nums[i]==0:
                count=0
            # increment count as consecutive 1 is seen
            else:
                count+=1
            # store the max-count seen in the iteration as result
            res=max(res,count)
        return res