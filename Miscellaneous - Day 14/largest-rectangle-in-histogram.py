# https://leetcode.com/problems/largest-rectangle-in-histogram/

# Best Approach: One Pass Solution; TC: O(2N) ~ O(N), SC: O(2N)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        stack=[]
        maxArea=0
        
        for i in range(n+1):
            # until stack is not-empty and curr-ele < ele-at-top of the stack
            # (or) until stack is not-empty and i==n [means right-small for the remaining elements in the stack will be last-index]
            while len(stack)!=0 and (i==n or heights[i]<heights[stack[-1]]):
                # get the height at index on top-of-stack
                height=heights[stack[-1]]
                stack.pop()
                # width will be equal to curr-idx 'i', when stack is emptied with the pop-step above
                width=i
                # width = curr-idx 'i' (right-small) - idx_at_top (left-small) - 1 
                if len(stack)!=0:
                    width=i-stack[-1]-1
                
                maxArea=max(maxArea, height*width)
            
            stack.append(i)
        return maxArea

# A Better Approach: Two Pass Solution; TC: O(5N) ~ O(N), SC: O(3N)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        stack=[]
        # to declare an array of the same size as heights-arr, also has a better way in Python
        leftSmall=[0 for x in heights]
        rightSmall=[0 for x in heights]
        # To get the Left-Smaller-Index for each element
        for i in range(n):
            # if the stack has elements, check for the eles greater than the curr-ele and pop them out
            # only smaller-eles than the curr-ele will remain if any
            while len(stack)!=0 and heights[stack[-1]]>=heights[i]:
                stack.pop()
            # for a curr-ele if nothing remains in stack -> its left-smaller-index will be start-of-the-arr
            if len(stack)==0:
                leftSmall[i]=0
            else:       # left-smaller-index for curr-ele will be index-seen-at-the-top-of-stack + 1
                leftSmall[i]=stack[-1]+1
            # add the curr-index to the stack, as a potential left-smaller for coming-eles
            stack.append(i)
        
        # pop all the elements off the stack to reuse the stack in getting right-smaller-indexes
        while len(stack)!=0:
            stack.pop()
        # Iterate in reverse-order
        for i in range(n-1,-1,-1):
            while len(stack)!=0 and heights[stack[-1]]>=heights[i]:
                stack.pop()
            # for a curr-ele if nothing remains in stack -> its right-smaller-index will be end-of-the-arr
            if len(stack)==0:
                rightSmall[i]=n-1
            else:       # right-smaller-index for curr-ele will be index-seen-at-the-top-of-stack - 1
                rightSmall[i]=stack[-1]-1
            stack.append(i)
        
        maxArea=0
        for i in range(n):
            # calc max-area for each ele, using their left and right smaller indexes
            maxArea=max(maxArea, heights[i]*(rightSmall[i]-leftSmall[i]+1))
        
        return maxArea

'''
Brute Force Approach: TC - O(N^2), SC - O(1) 
For each element in the heights-arr
An Inner Loop to look for an element smaller than the Current on the Left Side
Another Inner Loop to look for an element smaller than the current on the Right Side
Apply Formula to get the Area: heights[i]*(rightSmallIndex - leftSmallIndex + 1)
Return the Max-Area 
'''