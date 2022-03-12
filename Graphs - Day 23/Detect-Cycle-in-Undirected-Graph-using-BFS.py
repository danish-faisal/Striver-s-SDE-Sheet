# Similar Problem
# https://leetcode.com/problems/course-schedule/

# Time Complexity: O(N+E),  N is the time taken and E is for traveling through adjacent nodes overall. 
# Space Complexity: O(N+E) +  O(N) + O(N) , space for adjacent list , array and queue

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        q=deque()
        
        graph = [[] for _ in range(numCourses)]  
        inDegree = [0]*numCourses
        
        for course, preReq in prerequisites:
            graph[preReq].append(course)
            inDegree[course] +=1 
            
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)
        while q:
            current = q.pop()
            for i in graph[current]:
                inDegree[i]-=1
                if inDegree[i] ==0:
                    q.append(i)
         
        
        return not any(inDegree)