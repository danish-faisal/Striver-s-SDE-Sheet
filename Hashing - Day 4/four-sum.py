# https://leetcode.com/problems/4sum/

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            # skipping repeated numbers, as we have to find unique-pairs
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n):
                # skipping repeated numbers, as we have to find unique-pairs
                if j>0 and j-1>i and nums[j]==nums[j-1]:
                    continue
                # picking two nums at index - i & j -> subtracting them with target -> looking for other 2 nums with 2-pointers in the rest of the array
                to_sum = target - nums[i] - nums[j]
                front = j+1
                back = n-1
                while front < back:
                    temp_to_sum = nums[front] + nums[back]
                    if temp_to_sum < to_sum:
                        front+=1
                    elif temp_to_sum > to_sum:
                        back-=1
                    else:
                        res.append([nums[i],nums[j],nums[front],nums[back]])
                        r=len(res)-1
                        # skipping repeated numbers
                        while front<back and res[r][2]==nums[front]:
                            front+=1
                        while front<back and res[r][3]==nums[back]:
                            back-=1
        return res