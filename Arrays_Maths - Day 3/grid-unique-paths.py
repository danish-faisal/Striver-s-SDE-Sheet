# https://leetcode.com/problems/unique-paths/submissions/

# combinations (maths) problem
# total no. of combinations of rights and downs to be taken = (m+n-2)C(m-1)
# not fully understood
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        N = m+n-2
        r = m-1
        res = 1
        
        res = math.factorial(N)/(math.factorial(r) * math.factorial(N-r))
        
        return int(res)