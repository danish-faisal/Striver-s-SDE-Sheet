# https://leetcode.com/problems/combination-sum/
# https://www.geeksforgeeks.org/combinational-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # resultant array
        res = []
        # call the recursive function -> that gets the combinations
        self.findCombinations(0,candidates,target,res,[])
        return res
    
    def findCombinations(self,idx,candidates,target,res,curr):
        # base case: checked all the elements and crossed the last index in the given-array
        if idx==len(candidates):
            # if the last index is crossed and the target is 0 -> target is achieved somewhere in the recursive calls
            # and the combination achieving the target is in "curr" -> add it to the result 
            if target==0:
                res.append(curr[:])
            # else just return back
            return
        # if the value at current-index is "<=" the req-target then
        if candidates[idx]<=target:
            # pick the element
            curr.append(candidates[idx])
            # call the recursive-func again, and 
            # subtract the req-target with the curr-ele to get the new-target to be achieved in the next-recursion
            self.findCombinations(idx,candidates,target-candidates[idx],res,curr)
            # remove the selected element -> to go for recursion-calls without the curr-ele
            curr.pop()
        # make recursion-call without the curr-ele
        self.findCombinations(idx+1,candidates,target,res,curr)