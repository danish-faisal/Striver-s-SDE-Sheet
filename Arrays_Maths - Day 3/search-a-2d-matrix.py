# https://leetcode.com/problems/search-a-2d-matrix/

# binary search in a matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or target is None:
            return False
        m = len(matrix)
        n = len(matrix[0])
        low=0
        # total no. of elements = m*n
        high=m*n-1
        while(low<=high):
            mid = (low+high)//2
            # mid//n -> row of the mid-ele; mid%n -> col of the mid-ele
            if target == matrix[mid//n][mid%n]:
                return True
            elif target < matrix[mid//n][mid%n]:
                high = mid-1
            else:
                low = mid+1
        
        return False