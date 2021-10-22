# https://www.geeksforgeeks.org/array-implementation-of-queue-simple/

class Queue:
    # To initialize the object.
    def __init__(self, c):
        self.queue = []
        self.front = self.rear = 0
        self.capacity = c
 
    # Function to insert an element at the rear of the queue
    def Enqueue(self, data):
        # Check queue is full or not
        if(self.capacity == self.rear):
            print("\nQueue is full")
 
        # Insert element at the rear
        else:
            self.queue.append(data)
            self.rear += 1
 
    # Function to delete an element from the front of the queue
    def Dequeue(self):
        # If queue is empty
        if(self.front == self.rear):
            print("Queue is empty")
 
        # Pop the front element from list
        else:
            x = self.queue.pop(0)
            self.rear -= 1
 
    # Function to print queue elements
    def printQueue(self):
        if(self.front == self.rear):
            print("\nQueue is Empty")
 
        # Traverse front to rear to print elements
        for i in self.queue:
            print(i, "<--", end = '')
     
    # Print front of queue
    def Front(self):
        if(self.front == self.rear):
            print("\nQueue is Empty")
 
        print("\nFront Element is:", self.queue[self.front])
 
# Driver code
if __name__=='__main__':
    # Create a new queue of capacity 4
    q = Queue(4)
 
    # Print queue elements
    q.printQueue()
 
    # Inserting elements in the queue
    q.Enqueue(20)
    q.Enqueue(30)
    q.Enqueue(40)
    q.Enqueue(50)
 
    # Print queue elements
    q.printQueue()
 
    # Insert element in queue
    q.Enqueue(60)
 
    # Print queue elements
    q.printQueue()
 
    q.Dequeue()
    q.Dequeue()
    print("\n\nafter two node deletion\n")
 
    # Print queue elements
    q.printQueue()
 
    # Print front of queue
    q.Front()