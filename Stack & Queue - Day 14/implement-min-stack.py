# https://leetcode.com/problems/min-stack/

class MinStack:
    def __init__(self):
        self.stack=[]   # initialize Stack
        self.mini=(2**31)-1     # INT_MAX

    def push(self, val: int) -> None:
        if len(self.stack)==0:      # if stack is empty
            self.stack.append(val)
            self.mini=val
        else:
            # if the new-val < curr-min
            if val<self.mini:
                # push the modified val into the stack
                self.stack.append(2*val-self.mini)
                self.mini=val   # update min-val with the new-val
            else:
                self.stack.append(val)

    def pop(self) -> None:
        if len(self.stack)==0:
            return None
        val=self.stack[-1]      # get the top-val
        self.stack.pop()        # pop the top-val
        if val<self.mini:       # get the org-val from the modified-val
            self.mini=2*self.mini-val
        # need not return in pop-op

    def top(self) -> int:
        if len(self.stack)==0:
            return None
        # if modified-val exists at top, mod-val will definitely be < min-val
        if self.stack[-1]<self.mini:
            # curr-min will be the org-val, if mod-val exists at top
            return self.mini
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

'''
Approach 1: TC: O(1), SC: O(2N)
Push pairs into the stack, pair of the value pushed and the min-val at that point
'''