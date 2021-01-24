class Tonne:

    def __init__(self, tonne):
        self.tonne = tonne

    def __eq__(self, other):
        if isinstance(other, Tonne):
            if self.tonne == other.tonne:
                return True
        return False
