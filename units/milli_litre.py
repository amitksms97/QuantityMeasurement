class Ml:

    def __init__(self, ml):
        self.ml = ml

    def __eq__(self, other):
        if isinstance(other, Ml):
            if self.ml == other.ml:
                return True
        return False
