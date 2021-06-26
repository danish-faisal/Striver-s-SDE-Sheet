# https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # perform transpose of the matrix
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        
        # change 1st column with last column
        for i in range(n):
            for j in range(n//2):
                matrix[i][j],matrix[i][n-1-j]=matrix[i][n-1-j],matrix[i][j]