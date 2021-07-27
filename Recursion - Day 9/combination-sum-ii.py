# https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # resultant array
        ans=[]
        # sort the given array, to have the generated combinations sorted
        # call the recursive function 
        candidates.sort()
        self.findCombinations(0,target,[],ans,candidates)
        return ans
    
    def findCombinations(self,idx,target,curr,ans,candidates):
        # base case: if target is 0, the required combination is achived so return
        if target==0:
            ans.append(curr[:])
            return
        # call the recursive function with elements from idx to n-1
        for i in range(idx,len(candidates)):
            # skip the repeated elements
            if i>idx and candidates[i]==candidates[i-1]:
                continue
            # if the next element is > the req-target, target can't be achieved with the remaining elements so break and return
            if candidates[i]>target:
                break
            # add the curr-ele to the curr-combination ds
            curr.append(candidates[i])
            # call the recursive-func with the new target, and try to get the result with the remaining elements
            self.findCombinations(i+1,target-candidates[i],curr,ans,candidates)
            # removing the added element -> to not have it in the next-element's recursive call
            curr.pop()