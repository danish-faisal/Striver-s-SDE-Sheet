# https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1#
# https://www.geeksforgeeks.org/rat-in-a-maze-backtracking-2/

# approach 2 - can be adjusted for n directions

class Solution:
    def findPath(self, m, n):
        # visited-matrix, to keep track of visited-cells, same size as matrix 'm'
        vis=[[0 for x in range(n)] for x in range(n)]
        # possible dirs to move row-wise, 1 for up & -1 for column
        rdir=[1,0,0,-1]
        # possible dirs to move col-wise, -1 for left & 1 for right
        cdir=[0,-1,1,0]
        # resultant array
        ans=[]
        # checking if first cell is not blocked and the journey can be started
        if m[0][0]==1:
            self.soln_helper(0,0,rdir,cdir,n,m,vis,"",ans)
        return ans
    
    def soln_helper(self,i,j,rdir,cdir,n,m,vis,move,ans):
        # if we have reached the destn (n-1,n-1), add the moves taken to result and return
        if i==n-1 and j==n-1:
            ans.append(move)
            return
        # chars of dirs that can be taken in lexical-order
        dirs=['D','L','R','U']
        # trying all 4 dirs for each cell
        for idx in range(0,4):
            # getting the next-cell to move to
            ni=i+rdir[idx]
            nj=j+cdir[idx]
            # if next-cell pos is in bounds & it is not yet visited in this path & is not blocked
            if ni>=0 and nj>=0 and ni<n and nj<n and vis[ni][nj]==0 and m[ni][nj]==1:
                # mark as visted
                vis[i][j]=1
                # move to next-cell and add the move-taken
                self.soln_helper(ni,nj,rdir,cdir,n,m,vis,move+dirs[idx],ans)
                # backtracking step: mark the visited-cell as not-visited
                vis[i][j]=0


# approach 1 - 4 specific directions 

class Solution:
    def soln_helper(self,i,j,m,n,ans,move,vis):
        if i==n-1 and j==n-1:
            ans.append('%s'%move)
            return
        
        if i+1 < n and not vis[i+1][j] and m[i+1][j] == 1:
            vis[i][j] = 1
            self.soln_helper(i+1, j, m, n, ans, move + 'D', vis)
            vis[i][j] = 0
        
        if j-1 >= 0 and not vis[i][j-1] and m[i][j-1] == 1:
            vis[i][j] = 1
            self.soln_helper(i, j-1, m, n, ans, move + 'L', vis)
            vis[i][j] = 0 
        
        if j+1 < n and not vis[i][j+1] and m[i][j+1] == 1:
            vis[i][j] = 1 
            self.soln_helper(i, j+1, m, n, ans, move + 'R', vis)
            vis[i][j] = 0 
        
        if i-1 >= 0 and not vis[i-1][j] and m[i-1][j] == 1:
            vis[i][j] = 1
            self.soln_helper(i-1, j, m, n, ans, move + 'U', vis)
            vis[i][j] = 0
    
    
    def findPath(self, m, n):
        vis=[[0 for x in range(n)] for x in range(n)]
        ans=[]
        if m[0][0]==1:
            self.soln_helper(0,0,m,n,ans,"",vis)
        return ans