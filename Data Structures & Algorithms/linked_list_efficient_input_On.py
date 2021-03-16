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

    def append(self, data):
        pass
              
    
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

def insert_at_i(head, i, data):
    count = 0
    prev = None
    curr = head
    if i < 0 or i > length(head):
        return head

    while count < i:
        prev = curr
        curr = curr.next
        count += 1

    new_node = Node(data)

    if prev is None:
        head = new_node
    else:
        prev.next = new_node
    new_node.next = curr
        
    return head

def insert_at_i_rec(head, i, data):
    if i<0:
        return head
    if i == 0:
        new_node = Node(data)
        new_node.next = head
        return new_node
    
    if head is None:
        return None
    
    small_head = insert_at_i_rec(head.next, i-1, data)
    head.next = small_head
    return head

def reverse_rec(head):
    if head is None or head.next is None:
        return head

    new_head = reverse_rec(head.next)
    curr = new_head
    while curr.next is not None:
        curr = curr.next
    curr.next = head
    head.next = None
    return new_head

def reverse_itr(head):
    prev_node = None
    curr_node = head
    while curr_node is not None:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
    head = prev_node
    return head

def get_mid(head):
    slow = fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(head1, head2):
    temp = None
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    if head1.data <= head2.data:
        temp = head1
        temp.next = merge(head1.next, head2)
    else:
        temp = head2
        temp.next = merge(head1, head2.next)
    return temp

def merge_sort(head):
    if head is None or head.next is None:
        return head
    middle = get_mid(head)
    next_to_middle = middle.next
    middle.next = None
    left = merge_sort(head)
    right = merge_sort(next_to_middle)
    sorted_list = merge(left, right)
    return sorted_list
    
       
        
head = get_input()
# print(head.data)
print_LL(head)
# print(length(head))
# head = insert_at_i(head, 0, 6)
# print_LL(head)
# head = insert_at_i_rec(head, 3, 6)
# print_LL(head)
# head = reverse_itr(head)
# print_LL(head)
# print(get_mid(head))
head = merge_sort(head)
print_LL(head)


# O(n)
