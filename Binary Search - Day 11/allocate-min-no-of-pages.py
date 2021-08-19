# https://practice.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1#
# https://www.geeksforgeeks.org/allocate-minimum-number-pages/

# TC O(NlogN) SC O(1)
class Solution:
    # m = no. of students, mid = no. of pages
    def canAllocate(self,arr,n,m,mid):
        students=0
        pages=0
        # start iterating over the books array
        for i in range(n):
            # if no. of pages allocated to a student crosses the allocation that can be done to a student
            if (pages + arr[i] > mid):
                # increase the no. of students
                students+=1
                # reset pages to curr-val, to count the pages getting allocated to the new-student
                pages=arr[i]
                # if the value of pages in a single-book crosses max-allocation that can be done
                # fails a condition to keep
                if (pages > mid):
                    return False 
            else:
                # keep track of pages getting allocated to a student
                pages += arr[i]
        # if the no. students needed of curr-allocation size doesn't exceed actual-students
        # can be allocated with the curr-allocation size within conditions
        if (students < m):
            return True
        
        return False 
    
    def findPages(self,arr, n, m):
        # initializing low to min-possible allocation anyone can have i.e., one book with min-pages
        low=min(arr)
        # initializing high to max-possible allocation i.e., when there's only 1 student-all books to that student 
        high=sum(arr)
        # not really needed
        res=-1
        # start binary-search in our search space of [low,high]
        while low<=high:
            mid=(low+high)//2
            # check if the curr-div done is a valid one that satisfies all the conditions
            if self.canAllocate(arr,n,m,mid):
                res=mid
                # to check if we can make a valid-div with even lesser pages to a student 
                high=mid-1
            else:
                # if the div-done is not valid, increase the no. of pages to be assigned to a student
                low=mid+1
        
        return low