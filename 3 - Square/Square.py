class Square:
    def __init__(self, side_size):
        self._size = side_size

    @property
    def size(self):
        return self._size

    def calculate(self):
        return float(round(self._size * self._size, 3))

    def new_size(self, new_size):
        self._size = float(new_size)