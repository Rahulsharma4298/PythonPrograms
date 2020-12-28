class Node:
    """
A linked list is a sequence of data elements, 
which are connected together via links. 
Each data element contains a connection 
to another data element in form of a pointer.
    
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        

class Linked_List:
    def __init__(self):
        self.head = self.tail = None

        
    
def get_input():
    input_data = [int(x) for x in input().split()]
    head = tail = None
    
    for data in input_data:
        new_node = Node(data)
        
        if head is None:
            head = tail = new_node
        else:
            tail.next = new_node
            tail = new_node
            
    return head
    
def print_LL(head):
    while head is not None:
        print(str(head.data), end="->")
        head = head.next
    print(None)

def length(head):
    count = 0
    while head is not None:
        head = head.next
        count += 1
    return count
        
head = get_input()
print(head.data)
print_LL(head)
print(length(head))

# O(n)
