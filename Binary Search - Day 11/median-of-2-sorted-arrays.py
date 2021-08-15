# https://leetcode.com/problems/median-of-two-sorted-arrays/

# Naive Approach: Peform Merge step of Merge Sort to get 1 sorted array of the 2 sorted arrays
                # return avg of 2-mid elements if length is even, return mid-ele for odd-length; TC: O(N1+N2), SC: O(N1+N2)
# Optimized Naive: Instead of storing the whole array, get the positions needed from the length of the arrays
                # have a counter while iterating and store only the elements in the positions-needed; SC:O(1)

# Optimal: Divide the two arrays into two equal halves such that 'left-half < right-half', using binary-search
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2)<len(nums1):
            # call the func with smaller-array as the first-array
            return self.findMedianSortedArrays(nums2,nums1)
        n1=len(nums1)
        n2=len(nums2)
        low=0
        high=n1
        
        while low<=high:
            # divide 1st-array
            cut1=(low+high)//2
            # divide 2nd-array
            cut2=(n1+n2+1)//2 - cut1
            
            # left1: left to the division made in 1st-arr, right-1: right to the division made in 1st-arr
            # left2: left to the division made in 2nd-arr, right-2: right to the division made in 2nd-arr
            left1= float('-inf') if cut1==0 else nums1[cut1-1]
            left2= float('-inf') if cut2==0 else nums2[cut2-1]
            right1= float('inf') if cut1==n1 else nums1[cut1]
            right2= float('inf') if cut2==n2 else nums2[cut2]

            # checking if left-half < right-half, need to compare the elements only near division as the arrays are sorted
            if(left1<=right2 and left2<=right1):
                # if combined-length of two arrays is even
                if((n1+n2)%2==0):
                    return (max(left1,left2)+min(right1,right2))/2
                # if the combined lenght is odd
                else:
                    return max(left1,left2)
            # if the division made is incorrect i.e., elements at left-half>right-half, reduce left-half & increase right-half
            elif left1>right2:
                high=cut1-1
            # increase values at left-half, reduce at right-half
            else:
                low=cut1+1
        # will reach here only if arrays are not sorted
        return 0.0