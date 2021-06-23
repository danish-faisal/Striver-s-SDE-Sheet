# https://leetcode.com/problems/global-and-local-inversions/

# actual problme in sde sheet is: https://www.geeksforgeeks.org/counting-inversions/
# which will need to actuall calculate all the inversions

# for leetcode problem
# all local inversions are global inversions
# so if even a single global inversion exists that is not a local inversion -> results in False

class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        cmax = -1
        # current-max is needed for comparision as it will have the highest chances of being greater than other elements
        for i in range(len(nums)-2):
            # get the current max to compare with as we iterate over elements
            cmax = max(nums[i],cmax)
            # for a global but not local inv -> check if current-max is greater than an element with an index of cmax's index+2
            if cmax>nums[i+2]:
                return False
        return True