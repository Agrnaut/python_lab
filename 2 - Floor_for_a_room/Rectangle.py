class Rectangle:
    def __init__(self, sidea, sideb):
        self._sidea = sidea
        self._sideb = sideb


    @property
    def show_sides(self):
        return self.sidea, self._sideb

    def novos_lados(self, new_sidea, new_sideb):
        self._sidea = new_sidea
        self._sideb = new_sideb

    @property
    def calculate_area(self):
        return float(round(self._sidea * self._sideb, 2))

    @property
    def calculate_perimeter(self):
        return float(self._sidea * 2 + self._sideb * 2)

    def calculate_cm2(self):
        return float(self._sidea * self._sideb)