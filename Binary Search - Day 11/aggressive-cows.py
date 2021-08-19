# https://www.spoj.com/problems/AGGRCOW/

# Brute Force Approach: outer loop from 1->n, for each value of outer loop check if cows can be placed with that distance
#                       By having an inner loop of stalls and checking the distance between them >= the outer-loop val 'n'
# as we need the largest-minimal-distance, the last value of outer-loop, with which we can place cows successfully will be our answer 
# as after that value we won't be able to place the cows we can break out from the loops and return our answer
# TC O(N^2)


# Optimal Approach: Using Binary Search, TC: O(NlogN)
class Solution:
    def canPlace(self,arr,n,cows,dist):
        # val at which a cow is place
        coord=arr[0]
        # no. of cows placed
        cnt=1
        # iterate over the stalls
        for i in range(1,n):
            # if the dist b/w arr[i] & prev-placed-cow >= dist/mid
            if arr[i]-coord>=dist:
                # place another cow
                cnt+=1
                # update the coord-val with the curr-placed-cow
                coord=arr[i]
            # if the no. of placed cows == total-cows -> return True as the cows can be placed with the given-dist
            if cnt==cows:
                return True
        # if unable to place the no. of req-cows
        return False

    
    def aggressiveCows(self,arr,n,cows):
        # sort the stalls-array, easier to calc-dist and place the cows
        arr.sort()
        # search space of [1 to n-1] -> as the cows can be palce with min-dist of 1 and max-dist of arr[n-1]-(arr[0] or 1)
        low=arr[0]
        high=arr[-1]-arr[0]
        # resultant variable
        res=-1

        while low<=high:
            mid=(low+high)//2
            # if cows can be placed with min-dist=mid
            if self.canPlace(arr,n,cows,mid):
                # store the curr-mid val in result
                res=mid
                # incr low as to get the max min-dist with which cows can be placed
                low=mid+1
            else:
                # else reduce the dist to check the placement of cows
                high=mid-1
        return res