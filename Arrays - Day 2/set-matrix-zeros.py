# https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = []
        cols = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    rows.append(i)
                    cols.append(j)
        if len(rows)==0 and len(cols)==0:
            return
        m=len(matrix)
        n=len(matrix[0])
        for r in rows:
            matrix[r] = [0]*n
        for c in cols:
            for i in range(m):
                matrix[i][c]=0