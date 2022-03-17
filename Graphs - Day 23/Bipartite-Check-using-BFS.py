# https://leetcode.com/problems/is-graph-bipartite/
# Time Complexity: O(V + E), since in its whole, it is a BFS implementation, V – vertices; E – edges;
# Space Complexity: O(V), because, apart from the graph, we maintain a color array.

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color=[-1 for _ in range(len(graph))]
        
        for i in range(len(color)):
            if color[i]==-1:
                if not self.bfsCheck(i, graph, color):
                    return False
        
        return True
    
    def bfsCheck(self, idx, graph, color):
        q=[]
        q.append(idx)
        color[idx]=1
        
        while len(q)!=0:
            curr=q.pop(0)
            
            for node in graph[curr]:
                if color[node]==-1:
                    color[node]=1-color[curr]
                    q.append(node)
                elif color[node]==color[curr]:
                    return False
        
        return True