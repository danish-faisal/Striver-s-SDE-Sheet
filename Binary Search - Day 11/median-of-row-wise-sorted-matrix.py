# https://www.geeksforgeeks.org/find-median-row-wise-sorted-matrix/
# https://practice.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1#

# Brute Force Approach: convert the matrix to an array -> sort the array -> return its mid; TC: O(n*m log n*m), SC:(n*m)

# Optimal Search: Apply Binary search in the search space [low,high]
class Solution:
    def countSmallerThanEqualTo(self,rowarr,mid):
        l=0
        h=len(rowarr)-1
        while l<=h:
            m=(l+h)//2
            # for each row: check if the curr-mid <= outer-mid of search-space
            # if yes, cut down the row to right-half
            if rowarr[m]<=mid:
                l=m+1
            # cut down to left-half
            else:
                h=m-1
        # after binary-search's base-codn, req-ans will be 'l'
        return l

    def median(self, matrix, r, c):
        # assigning low: to max-no. in the constraint, high: to lowest no. in the costraint
    	low=1e9+1
    	high=0
        # iterate over all rows in the matrix: compare all elements at first-index in each row to get the lowest-no. & last-index to get the highest
    	for i in range(r):
    	    if matrix[i][0]<low:
    	        low=matrix[i][0]
    	    if matrix[i][c-1]>high:
    	        high=matrix[i][c-1]
    	# in our search-space of [low,high]
    	while(low<=high):
    	    count=0
            # calc-mid
    	    mid=(low+high)//2
            # count the elements, less than mid in each row
    	    for i in range(r):
    	        count+=self.countSmallerThanEqualTo(matrix[i],mid)
            # if count < half of the search-space, cut the space to right-half
    	    if count<=(r*c)/2:
    	        low=mid+1
            # cut the space to left-half
    	    else:
    	        high=mid-1
        # after the binary-search's break codn has met, answer will be at 'low'
        return int(low)