class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.top = -1

    def push(self, data):
        if self.is_full():
            print("Stack is full")
        else:
            self.top += 1
            self.top = data

    def pop(self):
        if self.is_empty():
            print("Stack is already empty")
        else:
            data = self.top
            self.top -= 1
            return data

    def is_full(self):
        if self.top == self.max_size:
            return True
        return False

    def is_empty(self):
        if self.top == -1:
            return True
        return False

    def print_stack(self):
        temp = self.top
        while temp != -1:
            print(temp)
            temp -= 1
            
           
s = Stack(5)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(0)
s.push(6)
s.print_stack()

    

    
        
