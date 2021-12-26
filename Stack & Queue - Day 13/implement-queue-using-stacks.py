# https://leetcode.com/problems/implement-queue-using-stacks/
# https://www.geeksforgeeks.org/queue-using-stacks/

# Approach 2: TC: AMORTIZED O(1) for pop-op, SC:O(2N)
class Queue:
    def __init__(self):
        self.input=[]
        self.output=[]

    def Enqueue(self,x):
        self.input.append(x)
    
    def Dequeue(self):
        # If both the stacks are empty
        if len(self.input)==0 and len(self.output)==0:
            return -1
        # if output-stack is empty -> get all the elements from input-stack to output-stack
        if len(self.output)==0:
            while len(self.input)!=0:
                self.output.append(self.input[-1])
                self.input.pop()
        x=self.output[-1]
        self.output.pop()
        return x
    
    def Front(self):
        if len(self.input)==0 and len(self.output)==0:
            return -1
        if len(self.output)==0:
            while len(self.input)!=0:
                self.output.append(self.input[-1])
                self.input.pop()
        return self.output[-1]
# Driver code
if __name__ == '__main__':
    q = Queue()
    q.Enqueue(1)
    q.Enqueue(2)
    q.Enqueue(3)
 
    print(q.Dequeue())
    print(q.Dequeue())
    print(q.Dequeue())

        

# Approach 1: TC:O(N) for Enqueue, SC:(2N)
class Queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]
    
    def Enqueue(self,x):
        # Move all elements from s1 to s2
        while len(self.s1)!=0:
            self.s2.append(self.s1[-1])
            self.s1.pop()
        # Push item into self.s1
        self.s1.append(x)
        # Push everything back to s1
        while len(self.s2)!=0:
            self.s1.append(self.s2[-1])
            self.s2.pop()
    
    def Dequeue(self):
        if len(self.s1)==0:
            return -1
        x=self.s1[-1]
        self.s1.pop()
        return x
    
    def Front(self):
        if len(self.s1)==0:
            return -1
        return self.s1[-1]

# Driver code
if __name__ == '__main__':
    q = Queue()
    q.Enqueue(1)
    q.Enqueue(2)
    q.Enqueue(3)
 
    print(q.Dequeue())
    print(q.Dequeue())
    print(q.Dequeue())

# On leetcode
class MyQueue:

    def __init__(self):
        self.s1=[]
        self.s2=[]

    def push(self, x: int) -> None:
        while len(self.s1)>0:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while len(self.s2)>0:
            self.s1.append(self.s2.pop())
            
    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return len(self.s1)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()