
class Fair:
    def __init__(self, fruit_name):
        self._fruit_name = fruit_name


    def __getitem__(self, item):
        return self._fruit_name[item]

    @property
    def fruit_name(self):
        return self._fruit_name

class Requester:
    def __init__(self, name):
        self._requester_name = name.title()

    @property
    def name(self):
        return self._requester_name


