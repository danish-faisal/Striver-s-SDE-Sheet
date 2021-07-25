# https://leetcode.com/problems/subsets-ii/

# In the array A at every step we have two choices for each element either we can
# ignore the element or we can include the element in our subset

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # sort the array -> needed to skip the repeated elements easily
        nums.sort()
        # resultant list
        subsets=[]
        # call the recursive function
        self.generateSubsets(0,nums,[],subsets)
        return subsets
    
    def generateSubsets(self,ind,nums,curr,subsets):
        # append the current-sub-array to the resultant array
        subsets.append(curr[:])
        
        # make the next iterations -> with the curr-ele & without the curr-ele added in the current-sub-array
        for i in range(ind,len(nums)):
            # to skip the repeated elements
            if ind!=i and nums[i]==nums[i-1]:
                continue
            # include the nums[i] in subset.
            curr.append(nums[i])
            # move onto the next element
            self.generateSubsets(i+1,nums,curr,subsets)
            # exclude nums[i] from the subset
            curr.pop()