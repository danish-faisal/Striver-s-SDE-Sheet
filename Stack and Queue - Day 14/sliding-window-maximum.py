# https://leetcode.com/problems/sliding-window-maximum/

# Optimal Approach: Using Doubly Ended Queue (Deque); TC: O(), SC:O()
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        deq=deque()    # Deque
        ans=[]  #res-arr
        
        for i in range(n):
            # check and remove the earlier-index that belongs to a previous-sliding-window
            # Eg: q=[2,3,4,5]; to check max in window [3,4,5] -> '2' is not needed so remove it
            if len(deq)!=0 and deq[0]==i-k:
                deq.popleft()    # pop-front operation of Deque
            
            # remove the eles < the curr-ele in iteration
            while len(q)!=0 and nums[deq[-1]]<nums[i]:
                deq.pop()     # pop-back operation of Deque
            
            # add the curr-idx in iteration to Deque
            deq.append(i)
            
            # once k no. of elements are iterated-over
            if i>=k-1:
                # max of each window will be at front of Deque
                ans.append(nums[deq[0]])
        
        return ans

'''
Brute Force Approach: TC - O(N * k)
outer loop: 0 to n-1-k
    inner loop: i to i+k to check max-no in this range and store
'''