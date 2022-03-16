# https://leetcode.com/problems/is-graph-bipartite/
# Time Complexity: O(V + E), since in its whole, it is a DFS implementation, V – vertices; E – edges;
# Space Complexity: O(V), because, apart from the graph, we maintain a color array.

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1 for _ in range(len(graph))]
        
        for i in range(len(color)):
            if color[i]==-1:
                if not self.dfsCheck(i, graph, color):
                    return False
                
        return True

    def dfsCheck(self, node, graph, color):
        
        for adj in graph[node]:
            if color[adj]==-1:
                color[adj]=1-color[node]
                if not self.dfsCheck(adj, graph, color):
                    return False
            if color[node]==color[adj]:
                return False
        
        return True
                