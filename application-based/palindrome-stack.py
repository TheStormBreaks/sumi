#we can define custom exceptions by creating a new class that is derived from the built-in Exception class
#Empty is a user defined exception class
class Empty(Exception):
    pass
#ArrayStack class implements the stack data structure 
class ArrayStack:
    # class constructor 
    def __init__(self):
        self._data = []
    
    # push/insert the element on the top of the stack    
    def push(self, e):
        self._data.append(e)
    
    # isEmpty returns true if stack is empty else returns false
    def isEmpty(self):
        return len(self._data) == 0
    
    # returns the number of elements in the stack
    def __len__(self):
        return len(self._data)

    # pop() chcecks if stack is empty then raise empty exception, else removes the top most element of stack and returns it to user 
    def pop(self):
        if self.isEmpty():
            raise Empty("Stack is Empty")
        return self._data.pop()
    
    # top() chcecks if stack is empty then raise empty exception, else returns the top most element of stack 
    def top(self):
        if self.isEmpty():
            raise Empty("Stack is Empty")
        return self._data[-1]
'''      
isPalindrome returns True if a given string is palindrome else retruns False
First half of the string is pushed on the stack
later one character is popped out of the stack and one charater is taken from the second half of the string, if charaters don't match, 
method returns False as String is not a palindrome
'''
def isPalindrome(str):
    length1 = len(str)
    stack = ArrayStack()
    if length1 %2 == 0:
        for i in range(0, length1 // 2):
            stack.push(str[i])
        for i in range(length1 // 2, length1):
            if str[i] != stack.pop():
                return False
        return True
    else:
        for i in range(0, length1 // 2):
            stack.push(str[i])
        for i in range(length1 // 2 + 1, length1):
            if str[i] != stack.pop():
                return False
        return True

print(isPalindrome("abbbca"))