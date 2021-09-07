# https://leetcode.com/problems/sliding-window-maximum/

# Use Deque instead of Queue for the actual solution

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        q=[]    # Deque
        ans=[]  #res-arr
        
        for i in range(n):
            # check and remove the earlier-index that belongs to a previous-sliding-window
            # Eg: q=[2,3,4,5]; to check max in window [3,4,5] -> '2' is not needed so remove it
            if len(q)!=0 and q[0]==i-k:
                q.pop(0)    # pop-front operation of Deque
            
            # remove the eles < the curr-ele in iteration
            while len(q)!=0 and nums[q[-1]]<nums[i]:
                q.pop()     # pop-back operation of Deque
            
            # add the curr-idx in iteration to Dequeue
            q.append(i)
            
            # once k no. of elements are iterated-over
            if i>=k-1:
                # max of each window will be at front of Deque
                ans.append(nums[q[0]])
        
        return ans

'''
Brute Force Approach: TC - O(N * k)
outer loop: 0 to n-1-k
    inner loop: i to i+k to check max-no in this range and store
'''