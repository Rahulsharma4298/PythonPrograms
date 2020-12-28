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
    head = None
    for data in input_data:
        new_node = Node(data)
        
        if head is None:
            head = new_node
        else:
            temp = head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
    
    return head
    
def print_LL(head):
    while head is not None:
        print(str(head.data), end="->")
        head = head.next
    print(None)
        
head = get_input()
print(head.data)
print_LL(head)

# This is taking O(n^2) to take input
# We can use efficient approach using tail to make it O(n)
