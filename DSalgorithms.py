# Linked list struct
class LinkedListNode:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.start_node = None # We start as null initially
    
    def insert_begin (self, value):
        # If we have an empty list we create one
        if self.start_node == None:
            self.start_node = LinkedListNode(value, None)
        else:
            new_node = LinkedListNode(value, self.start_node)
            self.start_node = new_node
    
    def insert_end (self, value):
        # If we have an empty list we create one
        if self.start_node == None:
            self.start_node = LinkedListNode(value)
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
        
    def get_list (self): # Returns as ordered python list (Start to end)
        ordered_list = []
        x = self.start_node
        while(x != None):
            ordered_list.append(x.value)
            x = x.next_node
        return ordered_list
    
class Stack:
    def __init__ (self):
        self.stack = LinkedList() # We start an empty with linked list
    
    def push (self, value): # Add element on the top of the stack
        self.stack.insert_begin(value)
    
    def pop (self): # Remove a element from the top of the stack
        self.stack.remove_node(self.stack.start_node.value)
        
    def print_stack (self): # Print the list DeBUG
        self.stack.print_list()
        
    def get_list (self): # Returns as ordered python list (Top to botton)
        return self.stack.get_list()
        
class Queue:
    def __init__ (self):
        self.queue = LinkedList() # We start with an empty linked list
        
    def enqueue (self, value): # Simple Queues gets input just from the end of the list
        self.queue.insert_end(value)
    
    def dequeue (self): # Simple Queues removes elements just from the beginning of the list
        self.queue.remove_node(self.queue.start_node.value)
    
    def print_list (self): # DeBUG
        self.queue.print_list()
        
    def get_list (self): # Returns as ordered python list (Start to end)
        return self.queue.get_list()
    
class BinaryTreeNode:
    def __init__(self, value, left_node = None, right_node = None):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node
        
class BST: # Binary Search Tree
    def __init__ (self):
        self.root = None
    
    def insert_node (self, value):
        # We create a new tree if there is not
        if self.root == None: # So if root is empty means empty tree
            self.root = BinaryTreeNode(value, None, None)
        # We add nodes to tree is tree isn't empty
        else:
            self.root = self._insert_node_recursive(self.root, value)
            
    def _insert_node_recursive(self, x, value):
        if x == None: # If we reached to the leaf of the node, create a new node
            return BinaryTreeNode(value)
        
        if value < x.value:
            x.left_node = self._insert_node_recursive(x.left_node, value)
        else:
            x.right_node = self._insert_node_recursive(x.right_node, value)
            
        return x
    
    def remove_node(self, value):
        self.root = self.remove_node_recursive(self.root, value)
    
    def min_value_node(self, node):
        current = node
        while current.left_node != None:
            current = current.left_node
        return current
    
    def remove_node_recursive(self, node, value):
        if node is None:
            return node  # If the node is not found, return None
        
        if value < node.value:
            node.left_node = self.remove_node_recursive(node.left_node, value)
        elif value > node.value:
            node.right_node = self.remove_node_recursive(node.right_node, value)
        else:
            # Node with only one child or no child
            if node.left_node is None:
                return node.right_node
            elif node.right_node is None:
                return node.left_node
            
            # Node with two children: Get the in-order successor (smallest in the right subtree)
            node.value = self.min_value_node(node.right_node).value
            
            # Delete the in-order successor
            node.right_node = self.remove_node_recursive(node.right_node, node.value)
        
        return node
    
    def get_level_order_list(self):
        if self.root is None:
            return []
        
        queue = [(self.root, None, None)]  # Queue stores tuples of (node, parent_value, position)
        result = []
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node, parent_value, position = queue.pop(0)
                current_level.append([node.value, [parent_value, position]])
                
                if node.left_node:
                    queue.append((node.left_node, node.value, 'left'))
                if node.right_node:
                    queue.append((node.right_node, node.value, 'right'))
            
            result.append(current_level)
        
        return result

