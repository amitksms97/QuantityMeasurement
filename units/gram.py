class Gram:

    def __init__(self, gram):
        self.gram = gram

    def __eq__(self, other):
        if isinstance(other, Gram):
            if self.gram == other.gram:
                return True
        return False
