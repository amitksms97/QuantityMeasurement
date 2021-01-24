class Kg:

    def __init__(self, kg):
        self.kg = kg

    def __eq__(self, other):
        if isinstance(other, Kg):
            if self.kg == other.kg:
                return True
        return False
