# https://practice.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1#
# https://www.geeksforgeeks.org/m-coloring-problem-backtracking-5/

def isValid(node, graph, color, N, col_sel):
    # for each node in node's row in graph's adjacency-matrix
    for k in range(0,N):
        # if an edge k-node exists check if the adjacent 'k' node has the same color selected for this node
        if k!=node and graph[k][node]==1 and color[k]==col_sel:
            # if yes-> the selected-color cant be used
            return False
    return True

def helper_func(node, graph, color, M, N):
    # base case: if reached N then all nodes are colored -> return True
    if node==N:
        return True
    # iterate over all colors
    for i in range(1,M+1):
        # check if the curr-node can be filled with curr-color
        if isValid(node, graph, color, N, i):
            # if yes -> fill the node with the color
            color[node]=i
            # recursively proceed to check the next-nodes
            if helper_func(node+1, graph, color, M , N):
                return True
            # backtracking step: if returned False in any recursive-step will reach here
            # and unmark all the colors-to-nodes used 
            color[node]=0
    # if True is not returned and all the colors are checked -> means its not possible
    return False
    
def graphColoring(graph, M, N):
    # to store the colors used for each node
    color=[0]*N
    return True if helper_func(0, graph, color, M, N) else False


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        V = int(input())
        k = int(input())
        m = int(input())
        list = [int(x) for x in input().strip().split()]
        graph = [[0 for i in range(V)] for j in range(V)]
        cnt = 0
        for i in range(m):
            graph[list[cnt]-1][list[cnt+1]-1]=1
            graph[list[cnt+1]-1][list[cnt]-1]=1
            cnt+=2
        if(graphColoring(graph, k, V)==True):
            print(1)
        else:
            print(0)

        t = t-1
# } Driver Code Ends