# https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1#

'''
Time complexity: O(N+E), Where N is the time taken for visiting N nodes and E is for travelling through adjacent nodes.

Space Complexity:O(N+E)+O(N)+O(N) , Space for adjacency list, Array,Auxiliary space.
'''

class Solution:
    def dfsHelper(self, node, adj, visited, storeDFS):
        storeDFS.append(node)
        visited[node]=True
        
        for i in adj[node]:
            if not visited[i]:
                self.dfsHelper(i, adj, visited, storeDFS)
        
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        visited=[False for i in range(V)]
        storeDFS=[]
        for i in range(V):
            if not visited[i]:
                self.dfsHelper(i, adj, visited, storeDFS)
        
        return storeDFS
