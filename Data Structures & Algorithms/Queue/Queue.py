class Queue:
	"""
	Queue is a linear data structure which works on FIFO principal.
	
	"""
    def __init__(self, max_size):
        self.max_size = max_size
        self.arr = [None]*max_size
        self.front = self.rear = -1
        self.size = 0

    def is_empty(self):
        if(self.front == -1 or self.front > self.rear):
            return True
        return False
    
    def is_full(self):
        if(self.rear == self.max_size-1):
            return True
        return False

    def enqueue(self, data):
        if self.is_full():
            raise Exception("Queue Overflow")
        if self.front == -1:
            self.front = 0
        self.rear = self.rear+1
        self.arr[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue Underflow")
        data = self.arr[self.front]
        self.front = self.front + 1
        return data

    def peek(self, front=None):
        if front is None:
            front = self.front
        return self.arr[front]

    def print(self):
        temp = self.front
        while(temp <= self.rear and temp is not None):
            print(self.arr[temp], end="<-")
            temp += 1
        print()


q = Queue(10)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.print()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

q.print()
print(q.peek(1))


    
