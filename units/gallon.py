class Gallon:

    def __init__(self, gallon):
        self.gallon = gallon

    def __eq__(self, other):
        if isinstance(other, Gallon):
            if self.gallon == other.gallon:
                return True
        return False
