# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap to store the already seen nums
        obj = {}
        for i in range(len(nums)):
            # subtract curr-ele with target and check if the difference exists in the hashmap of no.s seen
            if target - nums[i] in obj:
                # if yes return the first pair found
                return [obj[target - nums[i]],i]
            # else add the curr-ele to no.s seen hashmap
            else:
                obj[nums[i]] = i