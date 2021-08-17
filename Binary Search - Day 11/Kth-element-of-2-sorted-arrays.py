# https://practice.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1#
# https://www.geeksforgeeks.org/k-th-element-two-sorted-arrays/

class Solution:
    def kthElement(self,  nums1, nums2, n, m, k):
        if len(nums2)<len(nums1):
            # call the func with smaller-array as the first-array
            return self.kthElement(nums2,nums1,m,n,k)
        
        # min no. of elements that can be picked from arr1 -> 0 (or) (k-n) if k>n
        # max no. of elements that can be picked from arr1 -> m (or) (k-m) if k<m
        low=max(0,k-m)
        high=min(k,n)
        
        while low<=high:
            # divide 1st-array
            cut1=(low+high)//2
            # divide 2nd-array
            cut2=k - cut1
            
            # left1: left to the division made in 1st-arr, right-1: right to the division made in 1st-arr
            # left2: left to the division made in 2nd-arr, right-2: right to the division made in 2nd-arr
            left1= float('-inf') if cut1==0 else nums1[cut1-1]
            left2= float('-inf') if cut2==0 else nums2[cut2-1]
            right1= float('inf') if cut1==n else nums1[cut1]
            right2= float('inf') if cut2==m else nums2[cut2]

            # checking if left-half < right-half, need to compare the elements only near division as the arrays are sorted
            if(left1<=right2 and left2<=right1):
                # max of the left-half will be the Kth element
                    return max(left1,left2)
            # if the division made is incorrect i.e., elements at left-half>right-half, reduce left-half & increase right-half
            elif left1>right2:
                high=cut1-1
            # increase values at left-half, reduce at right-half
            else:
                low=cut1+1
        # will reach here only if arrays are not sorted
        return 0.0