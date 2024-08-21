# Linked list struct
class LinkedListNode:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.start_node = LinkedListNode(None, None) # We start with empty node
    
    def insert_begin (self, value):
        # If list of element is null so empty list, we edit start_node
        if self.start_node.value == None and self.start_node.next_node == None:
            self.start_node.value = value
        else:
            new_node = LinkedListNode(value, self.start_node)
            self.start_node = new_node
    
    def insert_end (self, value):
        # If list of element is null so empty list, we edit start_node
        if self.start_node.value == None and self.start_node.next_node == None:
            self.start_node.value = value
        else:
            new_node = LinkedListNode(value, None)
            x = self.start_node
            while(x.next_node != None):
                x = x.next_node
            x.next_node = new_node
    
    def remove_node (self, value):
        x = self.start_node
        # If value is in beginning
        if x.value == value:
            self.start_node = x.next_node
            return
        while(x.next_node != None):
            if x.next_node.value == value:
                x.next_node = x.next_node.next_node
                return
            x = x.next_node
            
    
    def print_list (self): # DeBUG
        x = self.start_node
        while(x != None):
            print(x.value)
            x = x.next_node
        