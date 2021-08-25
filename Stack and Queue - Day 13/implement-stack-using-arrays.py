# https://practice.geeksforgeeks.org/problems/implement-stack-using-array/1#

# Additionally should also manage the size when using languages like C, C++, Java
class MyStack:
    def __init__(self):
        self.arr=[]
        self.top=-1
    
    #Function to push an integer into the stack.
    def push(self,data):
        #add code here
        self.top+=1
        self.arr.append(data)
    
    #Function to remove an item from top of the stack.
    def pop(self):
        #add code here
        if self.top==-1:
            return -1
        x=self.arr[self.top]
        del self.arr[self.top]
        self.top-=1
        return x
    
    def top(self):
        if self.top==-1:
            return -1
        return self.arr[self.top]
    
    def isEmpty(self):
        return self.top==-1