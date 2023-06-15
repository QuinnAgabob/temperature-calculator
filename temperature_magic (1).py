"""Tools for working with Temperatures."""


class Temperature:
    """Represents a temperature."""

    def __init__(self, degrees=0):
        self.celsius = degrees
    def __str__(self):
        return 'Celsius: ' + str(self.celsius)

    def __repr__(self):
        return 'Celsius: ' + str(self.celsius)

    def __eq__(self, other):
        if self.celsius == other:
            return True
        else:
            return False
    def __gt__(self, other):
        if self.celsius > other:
            return True
        else:
            return False
    def __lt__(self, other):
        if self.celsius < other:
            return True
        else:
            return False
    def __ge__(self, other):
        if self.celsius >= other:
            return True
        else:
            return False
    def __le__(self, other):
        if self.celsius <= other:
            return True
        else:
            return False
    def __add__(self, other):
        if type(other) is int or type(other) is float:
            return Temperature(self.celsius + other)
        else:
            return Temperature(self.celsius + other.celsius)

    def __sub__(self, other):
        if type(other) is int or type(other) is float:
            return Temperature(self.celsius - other)
        else:
            return Temperature(self.celsius - other.celsius)

    def __iadd__(self, other):
        if type(other) is int or type(other) is float:
            self.celsius = self.celsius + other
            return self
        else:
            self.celsius = self.celsius + other.celsius
            return self

    def __isub__(self, other):
        if type(other) is int or type(other) is float:
            self.celsius = self.celsius - other
            return self
        else:
            self.celsius = self.celsius - other.celsius
            return self
    def __hash__(self):
        return('Hash of this object is: Hash: ', hash(self.celsius))

temperature1 = Temperature(20.5)
temperature2 = Temperature(10.5)
temperature3 = Temperature(20.5)
temperature1 += temperature2
print(temperature1.__hash__())




