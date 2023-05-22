class Room:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width


    def calculate_m2(self):
        return (float(self._lenght * self._width))