class Empty(Exception):
    pass

class Full(Exception):
    pass

class ArrayQueue:
    DEFAULT_CAPACITY = 5

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def deque(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size = self._size - 1
        return answer

    def is_queue_full(self):
        return self._size == len(self._data)

    def enqueue(self, e):
        if self.is_queue_full():
            raise Full("Queue is Full")
        else:
            avail = (self._front + self._size) % len(self._data)
            self._data[avail] = e
            self._size = self._size + 1

    def print_queue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            current = self._front
            print("Queue elements: ", end="")
            for i in range(self._size):
                print(self._data[current], end=" ")
                current = (current + 1) % len(self._data)
            print()



q=ArrayQueue()
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
q.enqueue(70)
q.print_queue()
print(q.deque())
q.enqueue(80)
q.print_queue()