# https://www.geeksforgeeks.org/implement-a-stack-using-single-queue/
# Approach 2: Using Single Queue
'''
// x is the element to be pushed and s is stack
push(s, x) 
  1) Let size of q be s. 
  1) Enqueue x to q
  2) One by one Dequeue s items from queue and enqueue them.
  
// Removes an item from stack
pop(s)
  1) Dequeue an item from q
'''
from queue import Queue
def Stack:
    def __init__(self):
        self.q=Queue()
        self.curr_size=0
    def push(self,x):
        self.q.put(x)
        self.curr_size+=1
        for i in range(self.curr_size-1):
            self.q.put(self.q.queue[0])
            self.q.get()
    def pop(self):
        if self.q.empty():
            return -1
        self.q.get()
    def top(self):
        if self.q.empty():
            return -1
        return self.q.queue[0]
    def size(self):
        return self.curr_size

# https://www.geeksforgeeks.org/implement-stack-using-queue/
# Approach 1: Using 2 Queues
'''
By making push operation costly

push(s, x) operation’s step are described below:
1. Enqueue x to q2
2. One by one dequeue everything from q1 and enqueue to q2.
3. Swap the names of q1 and q2

pop(s) operation’s function are described below:
1. Dequeue an item from q1 and return it.
'''
from queue import Queue

class Stack:
    def __init__(self):
        self.q1=Queue()
        self.q2=Queue()
        self.curr_size=0
    def push(self,x):
        self.q2.put(x)
        self.curr_size+=1

        while(not self.q1.empty()):
            self.q2.put(self.q1.queue[0])
            self.q1.get()
        self.q1,self.q2=self.q2,self.q1
    def pop(self):
        if self.q1.empty():
            return -1
        self.q1.get()
        self.curr_size-=1
    def top(self):
        if self.q1.empty():
            return -1
        return self.q1.queue[0]
    def size(self):
        return self.curr_size

# Driver Code 
if __name__ == '__main__':
    s = Stack()
    s.push(1) 
    s.push(2) 
    s.push(3) 
  
    print("current size: ", s.size())
    print(s.top()) 
    s.pop() 
    print(s.top()) 
    s.pop() 
    print(s.top()) 
  
    print("current size: ", s.size())