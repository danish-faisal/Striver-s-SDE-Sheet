# https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1#
# https://www.geeksforgeeks.org/rat-in-a-maze-backtracking-2/

# approach 2 - can be adjusted for n directions - (code not working)

class Solution:
    def findPath(self, m, n):
        vis=[[0]*n]*n
        rdir=[1,0,0,-1]
        cdir=[0,-1,1,0]
        ans=[]
        if m[0][0]==1:
            self.soln_helper(0,0,rdir,cdir,n,m,vis,"",ans)
        return ans
    
    def soln_helper(self,i,j,rdir,cdir,n,m,vis,move,ans):
        if i==n-1 and j==n-1:
            ans.append(move)
            return
        
        dirs=['D','L','R','U']
        for idx in range(0,4):
            ni=i+rdir[idx]
            nj=j+cdir[idx]
            if ni>=0 and nj>=0 and ni<n and nj<n and vis[ni][nj]==0 and m[ni][nj]==1:
                vis[i][j]=1
                self.soln_helper(ni,nj,rdir,cdir,n,m,vis,move+dirs[idx],ans)
                vis[i][j]=0


# approach 1 - 4 specific directions - (code not working) 

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
        vis=[[0]*n]*n
        ans=[]
        if m[0][0]==1:
            self.soln_helper(0,0,m,n,ans,"",vis)
        return ans