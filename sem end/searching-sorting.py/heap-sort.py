class MinHeap:
    def __init__(self, capacity):
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0
        
    def getParentIndex(self, index):
        return (index-1)//2
    
    def getLeftChildIndex(self, index):
        return 2*index + 1
        
    def getRightChildIndex(self, index):
        return 2*index + 2
        
    def hasParent(self, index):
        return self.getParentIndex(index) >= 0
        
    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size
    
    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size
    
    def parent(self, index):
        return self.storage[self.getParentIndex(index)]
    
    def leftChild(self, index):
        return self.storage[self.getLeftChildIndex(index)]
        
    def rightChild(self, index):
        return self.storage[self.getRightChildIndex(index)]
    
    def isFull(self):
        return self.size == self.capacity
        
    def swap(self, index1, index2):
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp
        
    def insert(self, data):
        if(self.isFull()):
            raise Exception("Heap is Full")
        self.storage[self.size] = data
        self.size += 1
        self.heapifyUp()
    
    def heapifyUp(self):
        index = self.size - 1
        while(self.hasParent(index) and self.parent(index) > self.storage[index]):
            self.swap(self.getParentIndex(index), index)
            index = self.getParentIndex(index)
            
    def removeMin(self):
        if self.size == 0:
            raise Exception("Heap is Empty")
        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.storage[self.size - 1] = 0
        self.size = self.size - 1 
        self.heapifyDown()
        return data
        
    def heapifyDown(self):
        index = 0
        while self.hasLeftChild(index):
            smallerChildIndex =  self.getLeftChildIndex(index)
            if self.hasRightChild(index) and self.leftChild(index) > self.rightChild(index):
                smallerChildIndex = self.getRightChildIndex(index)
                
            if self.storage[index] < self.storage[smallerChildIndex]:
                return
            else:
                self.swap(index, smallerChildIndex)
                index = smallerChildIndex


def heapSort(list):
    # sorting of data can be achieved using min heap and max heap tress 
    # because whenever delete opertion is performed on min heap, it always deletes the minimum value in the heap
    # and when delete is performed on max heap , it always deletes the maximum value in the heap.
    # Hence, if we want to sort the values in the ascending order, we can construct a min heap and then perform the delete opertion
    # if we want the value to be sorted in descending order, construct a max heap and then perform delete operation
    minH = MinHeap(len(list))
    sortedList = []
    for ele in list:
        # insert the list element into heap one by one
        minH.insert(ele)
    for ele in list:
        # delete the values from heap and append the deleted values in the sorted list
        sortedList.append(minH.removeMin())
    print(sortedList)
 
 
if __name__ == "__main__": 
    heapSort([12, 11, 7, 23, 45])
        

           
                
