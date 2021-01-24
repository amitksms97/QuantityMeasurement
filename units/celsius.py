class Celsius:

    def __init__(self, celsius):
        self.celsius = celsius

    def __eq__(self, other):
        if isinstance(other, Celsius):
            if self.celsius == other.celsius:
                return True
        return False
