class Litre:

    def __init__(self, litre):
        self.litre = litre

    def __eq__(self, other):
        if isinstance(other, Litre):
            if self.litre == other.litre:
                return True
        return False
