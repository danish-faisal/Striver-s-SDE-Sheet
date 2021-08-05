# https://leetcode.com/problems/permutations

# TC: O(n! * n), SC: O(n)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # resultant array
        ans=[]
        # call the recursive solution function
        self.recurPermute(0,nums,ans)
        return ans
    
    def recurPermute(self,index,nums,ans):
        # base case: index crosses the lenght of the given list -> we have a permutation
        if index>len(nums)-1:
            # add copy of current-array state to resultant array
            # copy because -> actual array will keep changing
            ans.append(nums[::])
            return ans
        # iterate from index->n-1 [0 based]
        for i in range(index,len(nums)):
            # swapping each element at index 'i' with all elements in range (i,n-1) indexes
            nums[i],nums[index]=nums[index],nums[i]
            # call the recursive solution function
            self.recurPermute(index+1,nums,ans)
            # swap the elements back -> to have the array in correct state for next recursion
            nums[i],nums[index]=nums[index],nums[i]