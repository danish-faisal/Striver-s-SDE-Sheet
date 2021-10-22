# https://leetcode.com/problems/next-greater-element-ii/
# https://www.geeksforgeeks.org/find-the-next-greater-element-in-a-circular-array/

# Optimal Approach: TC: O(N), SC: O(1)
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]    #stack to be used
        n=len(nums)
        nge=[-1]*n  # resultant array
        # Iterating in reverse-order 2n times: 2n-1 to 0 
        # => 1st-half in reverse order to get the greater element on the left-side of the last-elements in the array
        for i in range((2*n)-1,-1,-1):
            # pop all the elements smaller than the current-element form the stack
            while len(stack)!=0 and stack[-1]<=nums[i%n]:
                stack.pop()
            # only need to store NGE elements for 0 to n elements
            # for first n iterations stack will have the relevant greater elements for the last-elements
            if i<n:
                # store the stack-top as the NGE for the curr-ele in iteration
                if len(stack)!=0:
                    nge[i]=stack[-1]
                # if no eles in the stack -> store -1, will only occur for greatest element
                else:
                    nge[i]=-1
            # add the curr-ele to the stack in each iteration
            stack.append(nums[i%n])
        
        return nge

'''
Brute Force Approach: TC:O(N^2), SC: O(1)
Use two loops: The outer loop picks all the elements one by one. 
The inner loop looks for the first greater element for the element picked by the outer loop. 
If a greater element is found then that element is printed as next, otherwise, -1 is printed.
'''