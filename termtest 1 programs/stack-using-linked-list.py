class Empty(Exception):
    pass

class LinkedListStack:
    ''' 
align the stack top with head of the linked list, because in singly linked list inserting and removing element 
from the linked list is efficient (as time complexity is O(1))'''

class Empty(Exception):
    pass

class LinkedListStack:
    def __init__(self): # Constructor of LinkedListStack class
       self._head = None   # reference to head node of LinkedListStack
       self._size = 0      # number of elements in stack
    
#Nested Node class
    
    class Node:
        __slots__ = "element" , "next"  # streamline the memory usage
        def __init__(self, element = None, next = None):    # constructor of Nested Node class
            self.element = element  # reference to the node element
            self.next = next        # reference to the next node


    def __init__(self): # Constructor of LinkedListStack class
       self._head = None   # reference to head node of LinkedListStack
       self._size = 0      # number of elements in stack
       
    def isEmpty(self):
        return self._size ==0   # returns true if stack is empty (number of elements in stack is equal to zero)
        
    def __len__(self):
        return self._size      # returns the number of elements in the stack
    def push(self, e):
        newNode = self.Node(e, self._head) # creats a new node
        self._head = newNode  # new node is assigned as the head  of the linked list/ stack
        self._size = self._size + 1
        
    def pop(self):
        if self.isEmpty(): 
            # checks if stack is empty then raise Empty exception
            raise Empty("stack is empty")
        answer = self._head.element # otherwise returns the head/top-most element's value
        
        self._head = self._head.next # update the head of the linked list to next node of linked list
        self._size = self._size - 1
        return answer

    def top(self):
        if self.isEmpty(): 
            # checks if stack is empty then raise Empty exception
            raise Empty("stack is empty")
        answer = self._head.element # otherwise returns the head/top-most element's value
        return answer

l1 = LinkedListStack()
print(l1.push(10))
print(len(l1))
print(l1.top())
print(l1.pop())