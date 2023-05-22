class People:
    def __init__(self, name, age, weight, height):
        self._name = name.title()
        self._age = age
        self._weight = weight
        self._height = height

    def get_older(self, new_age): #nova idade 30
        self._age = new_age


    @property
    def show_person(self):
        return self._name, self._age, self._weight, round((self._height), 2)

    def fatten(self, new_weight):
        self._weight = new_weight


    def grow_tall(self, new_height):
        self._height = new_height