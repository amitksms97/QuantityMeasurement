class Cm:

    def __init__(self, cm):
        self.cm = cm

    def __eq__(self, other):
        if isinstance(other, Cm):
            if self.cm == other.cm:
                return True
        return False
