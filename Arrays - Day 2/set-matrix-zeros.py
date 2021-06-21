# https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = []
        cols = []
        # get the indexes row and column wise where 0 is present in rows & cols list
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    rows.append(i)
                    cols.append(j)
        if len(rows)==0 and len(cols)==0:
            return
        m=len(matrix)
        n=len(matrix[0])
        # make total row to 0 for an index in rows list
        for r in rows:
            matrix[r] = [0]*n
        # make a col to 0 for index in cols list
        for c in cols:
            for i in range(m):
                matrix[i][c]=0