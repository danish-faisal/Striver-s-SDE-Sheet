# https://leetcode.com/problems/majority-element-ii/

class Solution:
    # maximum 2 elements can exist with count > N/3 times
    def majorityElement(self, nums: List[int]) -> List[int]:
        # 2 counters and 2 pointers
        count1, count2, candid1, candid2 = 0,0,None,None
        for i in nums:
            # curr-ele same as 1st candidate -> incr 1st counter
            if i == candid1:
                count1+=1
            # curr-ele same as 2nd candidate -> incr 2nd counter
            elif i == candid2:
                count2+=1
            # if 1st counter = 0, update 1st candidate with new element
            elif count1==0:
                candid1,count1 = i,1
            # if 2nd counter = 0, update 2nd candidate with new element
            elif count2==0:
                candid2,count2 = i,1
            # curr-ele not same as either 1st or 2nd candidate -> decr both counters
            else:
                count1-=1
                count2-=1
        # return the 1 or 2 elements whose counts are the highest in the list and appear more than N/3 times 
        return [n for n in (candid1,candid2) if nums.count(n) > len(nums)//3]