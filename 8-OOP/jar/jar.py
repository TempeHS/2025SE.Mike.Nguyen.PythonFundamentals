class Jar:

    def __init__(self, capacity=12):
        if capacity < 0 and isinstance(capacity, int):
            raise ValueError
        self.capacity = capacity
        self.size = 0

    def __str__(self) -> str:
        return "🍪" * (self._size)

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    def deposit(self, n):
        self.size += n
        if self._size > self._capacity:
            raise ValueError

    def withdraw(self, n):
        self.size -= n
        if self.size < 0:
            raise ValueError
