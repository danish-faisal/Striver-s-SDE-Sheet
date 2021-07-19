# https://leetcode.com/problems/trapping-rain-water/

'''
Approach 1: O(N^2) TC and O(1) Space
outer loop -> iterating and calculation Left-Max, till the curr-index
nested loop -> itearting the remaining-indexes after curr-index and calculating Right-Max
Calculating -> Min(LeftMax,RightMax)-Value[curr-index], to get the water that can be stored at curr-index
Add tot Result if above-calc value>0
'''

# Approach 2 -> Calculating Right-Max for each index Initially and Store in an Array corresponding to same index

class Solution:
    def trap(self, height: List[int]) -> int:
        if not len(height)>0:
            return 0
        # initialize Suffix-Max array -> len equal to given array
        maxright=[0]*len(height)
        maxright[len(height)-1]=height[len(height)-1]
        # Get Suffix-Max for each index
        for i in range(len(height)-2,-1,-1):
            maxright[i]=max(maxright[i+1],height[i])

        res=0
        # initialize Max-Left
        maxleft=height[0]
        for i in range(1,len(height)-1):
            # apply formula
            temp=min(maxleft,maxright[i])-height[i]
            if temp>0:
                res+=temp
            # Update Prefix-Max
            if height[i]>maxleft:
                maxleft=height[i]
        return res