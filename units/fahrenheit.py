class Fahrenheit:

    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit

    def __eq__(self, other):
        if isinstance(other, Fahrenheit):
            if self.fahrenheit == other.fahrenheit:
                return True
        return False
