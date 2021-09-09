# https://leetcode.com/problems/rotting-oranges/

# Time complexity: O(rows * cols) * 4 -> each cell is visited at least once; 4 as we check all 4 dirs for each cell
# Space complexity: O(rows * cols) -> in the worst case if all the oranges are rotten they will be added to the queue

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)     # no. of rows
        n=len(grid[0])  # no. of cols
        mins=total=count=0
        rotten=deque()  # declare a deque
        
        # iterate over each cell in the grid
        for i in range(m):
            for j in range(n):
                # calc total-no of non-empty cells
                if grid[i][j]!=0:
                    total+=1
                # count no. of rotten oranges
                if grid[i][j]==2:
                    rotten.append([i,j])
        
        # dirs one can move in a grid from a cell: left, top, right, bottom
        dx=[0,-1,0,1]
        dy=[-1,0,1,0]

        while len(rotten)!=0:
            # getting no. of rotten-oranges in the deque, before each minute
            k=len(rotten)
            count+=k
            # for each rotten-orange cell in the deque
            while k>0:
                pair=rotten[0]
                x=pair[0]
                y=pair[1]
                # pop_front the rotten orange whose cell we're iterating over
                rotten.popleft()
                for i in range(4):
                    # get the next-dir we're checking in L U R D
                    nx=x+dx[i]
                    ny=y+dy[i]
                    # check we're within bounds and the cell-val==1
                    if (nx<0 or ny<0 or nx>=m or ny>=n or grid[nx][ny]!=1):
                        continue
                    # mark the affected cell as rotten
                    grid[nx][ny]=2
                    # push the affected cell in the deque
                    rotten.append([nx,ny])
                # reduce the no. of rotten-oranges to check in this iteration
                k-=1
            # if deque is not-empty, incr mins
            if len(rotten)!=0:
                mins+=1
        
        # return mins if the no. of pushed-rotten-oranges in the deque == total-oranges; else -1
        return mins if total==count else -1