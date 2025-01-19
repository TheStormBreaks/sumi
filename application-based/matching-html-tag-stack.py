class Empty(Exception):
    pass
class ArrayStack:
    def __init__(self):
        self._data = []
        
    def push(self, e):
        self._data.append(e)
    
    def isEmpty(self):
        return len(self._data) == 0
    
    def __len__(self):
        return len(self._data)
    
    def pop(self):
        if self.isEmpty():
            raise Empty("Stack is Empty")
        return self._data.pop()
    def top(self):
        if self.isEmpty():
            raise Empty("Stack is Empty")
        return self._data[-1]

def is_matched(htmlCode):
    stack = ArrayStack()  # create an instance of ArrayStack
    j = htmlCode.find("<") 
    ''' find the index of opening angular bracket, find method of String (str) class returns 
the index number of occurrence the character sent as an argumnet or returns -1 if character is not present in the string'''
    while j != -1: 
        k = htmlCode.find(">", j+1) # find the index of closing angular bracket after opening angular bracket( after j +1 index number)
        if k!= -1: 
            tag = htmlCode[j+1:k] # slice the tag (between opening and closing angular brackets)
            
            if not tag.startswith("/"): # if tag is an opening tag then push the tag on the top of the stack
                stack.push(tag)
            elif stack.pop() != tag[1:]: # if opening on the top of the stack and current closing tags are not matching then return False
                
                return False
        j = htmlCode.find( "<", k+1)  # find next opening bracket
    
    return stack.isEmpty() # returns true if stack is empty
print(is_matched("<HTML> <Body> <P>First HTML Code </P></Body></HTML>"))
