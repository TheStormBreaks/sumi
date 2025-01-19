class ArrayDeque:
    def __init__(self, capacity=10):
        """Initialize an empty deque with a fixed capacity."""
        self._data = [None] * capacity
        self._size = 0
        self._front = 0  # index of the front element
        self._capacity = capacity

    def __len__(self):
        """Return the number of elements in the deque."""
        return self._size

    def is_empty(self):
        """Return True if the deque is empty."""
        return self._size == 0

    def is_full(self):
        """Return True if the deque is full."""
        return self._size == self._capacity

    def add_first(self, e):
        """Add an element to the front of the deque."""
        if self.is_full():
            raise IndexError("Deque is full")
        self._front = (self._front - 1) % self._capacity  # circularly decrement front
        self._data[self._front] = e
        self._size += 1

    def add_last(self, e):
        """Add an element to the end of the deque."""
        if self.is_full():
            raise IndexError("Deque is full")
        avail = (self._front + self._size) % self._capacity  # index for the new element
        self._data[avail] = e
        self._size += 1

    def delete_first(self):
        """Remove and return the first element of the deque."""
        if self.is_empty():
            raise IndexError("Deque is empty")
        answer = self._data[self._front]
        self._data[self._front] = None  # help garbage collection
        self._front = (self._front + 1) % self._capacity  # circularly increment front
        self._size -= 1
        return answer

    def delete_last(self):
        """Remove and return the last element of the deque."""
        if self.is_empty():
            raise IndexError("Deque is empty")
        back = (self._front + self._size - 1) % self._capacity  # index of last element
        answer = self._data[back]
        self._data[back] = None  # help garbage collection
        self._size -= 1
        return answer

    def first(self):
        """Return (but do not remove) the first element of the deque."""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self._data[self._front]

    def last(self):
        """Return (but do not remove) the last element of the deque."""
        if self.is_empty():
            raise IndexError("Deque is empty")
        back = (self._front + self._size - 1) % self._capacity
        return self._data[back]

    def print_deque(self):
        """Print the elements of the deque from front to back."""
        if self.is_empty():
            print("Deque is empty")
        else:
            index = self._front
            elements = []
            for _ in range(self._size):
                elements.append(self._data[index])
                index = (index + 1) % self._capacity
            print("Deque contents:", elements)

D= ArrayDeque()
D.add_first(21)
D.add_first(20)
D.print_deque()
D.add_last(22)
D.print_deque()
print(D.delete_first())
D.print_deque()