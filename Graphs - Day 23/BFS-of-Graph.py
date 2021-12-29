# https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1

'''
Time Complexity : O(N+E)
N = Nodes , E = travelling through adjacent nodes

Space Complexity : O(N+E) + O(N) + O(N) 
Space for adjacency list, visited array, queue data structure
'''

class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        vis=[False for _ in range(V)]
        q=[0]
        vis[0]=True
        bfs=[]
        while len(q)>0:
            node=q.pop(0)
            bfs.append(node)
            
            for a in adj[node]:
                if not vis[a]:
                    q.append(a)
                    vis[a]=True
        
        return bfs