"""
A linked list is a linear data structure, in which the elements are stored at non-contiguous memory locations
LinkedList consists of nodes where each node contains a data field and a reference(link) to the next node in the list.

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next
        print(None)
        

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        

    def insert(self, data, index):
        count = 0
        if index < 0 or index >= self.length():
            raise Exception("Invalid Index")
        elif index == 0:
            self.prepend(data)
        else:
            temp = self.head
            while temp.next is not None:
                if count == index - 1:
                    new_node = Node(data)
                    current = temp.next
                    temp.next = new_node
                    new_node.next = current
                    break
                temp = temp.next
                count += 1
                

    def insert_after(self, prev_node_data, data):
        temp = self.head
        while temp is not None:
            if temp.data == prev_node_data:
                new_node = Node(data)
                next_to_prev = temp.next
                temp.next = new_node
                new_node.next = next_to_prev
                break
            temp = temp.next


    def create_from_arrays(self, arr):
        for i in arr:
            self.append(i)
                 

    def length(self):
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    def length_rec(self, node):
        if node is None:
            return 0
        return 1 + self.length_rec(node.next)


    def remove_first(self):
        self.head = self.head.next
        

    def remove_last(self):
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None
        
        
    def remove(self, index):
        count = 0
        if index < 0 or index >= self.length():
            raise Exception("Invalid Index")
        elif index == 0:
            self.head = self.head.next
        else:
            temp = self.head
            while temp is not None:
                if count == index - 1:
                    temp.next = temp.next.next
                    break
                temp = temp.next
                count += 1
                
                
    def delete_node(self, key):
        curr = self.head
        if curr and curr.data == key:
            self.head = curr.next
            curr = None
            return
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next

        if curr is None:
            return

        prev.next = curr.next
        curr = None
        

    def reverse(self):
        prev_node = None
        curr_node = self.head
        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node
        

    def reverse_rec(self):
        def _reverse_rec(prev_node, curr_node):
            if curr_node is None:
                return prev_node

            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
            return _reverse_rec(prev_node, curr_node)
        self.head = _reverse_rec(None, self.head)
        

    def get_mid(self):
        slow = fast = self.head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.data
    

    def get_node(self, index):
        if index < 0 or index >= self.length():
            raise Exception("Invalid Index")
        elif index == 0:
            return self.head
        else:
            count = 0
            temp = self.head
            while temp is not None:
                if count == index:
                    break
                count += 1
                temp = temp.next
        return temp


    def nth_to_last_node(self, index):
        temp = self.get_node(index)
        while temp is not None:
                print(temp.data, end="->")
                temp = temp.next
        print(None)


    def slice(self, start_index, end_index):
        start_node = self.get_node(start_index)
        end_node = self.get_node(end_index)
        temp = start_node
        while temp and temp != end_node:
            print(temp.data, end="->")
            temp = temp.next
        print(temp.data, end="->")
        print(None)    
        
            
    def get_prev_node(self, ref_node):
        curr = self.head
        while curr and curr.next != ref_node:
            curr = curr.next
        return curr

    
    def swap_nodes(self, key1, key2):
        if key1 == key2:
            return
        prev1 = None
        curr1 = self.head
        while curr1 and curr1.data != key1:
            prev1 = curr1
            curr1 = curr1.next

        prev2 = None
        curr2 = self.head
        while curr2 and curr2.data != key2:
            prev2 = curr2
            curr2 = curr2.next

        if prev1:
            prev1.next = curr2
        else:
            self.head = curr2

        if prev2:
            prev2.next = curr1
        else:
            self.head = curr1

        curr1.next, curr2.next = curr2.next, curr1.next

    
    def remove_duplicates(self):
        curr = self.head
        prev = None
        dup_values = dict()
        while curr:
            if curr.data in dup_values:
                prev.next = curr.next
            else:
                dup_values[curr.data] = 1
            prev = curr
            curr = curr.next
            

    def is_palindrome(self):
        #1 Using String
        s = ""
        temp = self.head
        while temp is not None:
            s += temp.data
            temp = temp.next
        return s[::-1] == s
    

    def is_palindrome2(self):
        #2 Using Stack
        s = []
        temp = self.head
        while temp is not None:
            s.append(temp.data)
            temp = temp.next
        temp = self.head
        while temp is not None:
            data = s.pop()
            if temp.data != data:
                return False
            temp = temp.next
        return True


    def is_palindrome3(self):
        #3 By comparing starting and end node
        # & incrementing untill start, end reach
        # to common node
        start = self.head
        end = self.get_node(self.length()-1)
        while start != end:
            if start.data != end.data:
                return False
            start = start.next
            end = self.get_prev_node(end)
        return True


    def move_tail_to_head(self):
        prev = None
        curr = self.head
        while curr.next is not None:
            prev = curr
            curr = curr.next
        prev.next = None
        curr.next = self.head
        self.head = curr
    

    def count(self, node_data):
        count = 0
        temp = self.head
        while temp is not None:
            if temp.data == node_data:
                count += 1
            temp = temp.next
        return count
                
                                                  
def merge(head1, head2):
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

    
l = LinkedList()
l.create_from_arrays([1, 5, 7])
l.print_ll()

l2 = LinkedList()
l2.create_from_arrays([2,3,4,6])
l2.print_ll()
print("Merging two sorted linkedlist")
merge(l.head, l2.head)
l.print_ll()
l = LinkedList()
l.create_from_arrays([1,2,3,4])
l.print_ll()
print(l.get_node(1).data)
print("After Swapping")
l.swap_nodes(2, 4)
l.print_ll()
print("\nAfter Removing duplicates")
l3 = LinkedList()
l3.create_from_arrays([1,5,7,4,4,5,2,2,8])
l3.print_ll()
l3.remove_duplicates()
l3.print_ll()
print("\nChecking for palindrom LinkedList")
l4 = LinkedList()
l4.create_from_arrays(["R","A","D","A","R"])
l4.print_ll()
print(l4.is_palindrome3())
print("\nNth to last node")
l4.nth_to_last_node(2)
print("\nSlicing")
l4.slice(1,3)
print("\nCount:", l4.count("A"))
print("\nMoved Head to Tail")
l4.move_tail_to_head()
l4.print_ll()



# print("Length:", l.length())
# print("Mid Node:", l.get_mid())

