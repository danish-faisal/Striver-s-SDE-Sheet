# https://leetcode.com/problems/n-queens/
# https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # we need to look only on the left side to check where the queens are placed
        # rows -> to hash the row-no filled by a queen
        rows = [0] * n
        # to hash a lower-left-diagonal filled by a queen -> diagonal can be identified bu sum of intersecting row & col
        l_diag = [0] *(2*n-1)
        # to hash upper left diagonal filled by a queen -> can be identified by (n-1)+(col-row)
        anti_diag = [0] *(2*n-1)
        # resultant-array
        result = []
        # coverting list[list[chars]]=>list[strings]
        def format_queens(positions):
            res = [['.' for i in range(n)]for j in range(n)]
            # placing a 'Q' where positions' contain a (row,col) pair
            for x, y in positions:
                res[x][y] = 'Q'
            return ["".join(r) for r in res]
        # DFS logic
        def search(y):
            # base codn: if col has reached the end -> send a copy of positions [as the org-one keeps changing] to build the board and add to result
            if y == n:
                result.append(format_queens(positions[:]))
                return
            # iterate over rows for each column
            for x in range(n):
                # if a queen is placed in the same row or upper-left or lower-left diagonal -> skip this position
                if rows[x] or l_diag[x+y] or anti_diag[x-y+n-1]:
                    continue
                # mark the row,upper-left & lower-left diagonal as occupied
                rows[x] = l_diag[x+y] =anti_diag[x-y+n-1] = 1
                # mark the position as a queen can be placed here
                positions.append((x,y))
                # with this position filled at a (row,col), look for a position to fill in next-col
                search(y+1)
                # backtracking step: unmark position and row & left-diagonals -> as a different position will be used in next iteration & set of recursions
                rows[x] = l_diag[x+y] =anti_diag[x-y+n-1] = 0
                positions.pop()
        # storing the positions where a queen is placed
        positions = []
        # starting the operation from first column(0)
        search(0)
        return result