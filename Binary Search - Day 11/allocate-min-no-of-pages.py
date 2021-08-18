# https://practice.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1#

# TC O(NlogN) SC O(1)
class Solution:
    def canAllocate(self,arr,n,m,mid):
        students=0
        pages=0
        for i in range(n):
            if (pages + arr[i] > mid):
                students+=1
                pages=arr[i]
                if (pages > mid):
                    return False 
            else:
                pages += arr[i]
        
        if (students < m):
            return True
        
        return False 
    #Function to find minimum number of pages.
    def findPages(self,arr, n, m):
        #code here
        low=min(arr)
        high=sum(arr)
        res=-1
        
        while low<=high:
            mid=(low+high)//2
            if self.canAllocate(arr,n,m,mid):
                res=mid
                high=mid-1
            else:
                low=mid+1
        
        return low