from enum_class import Length


class QuantityMeasurement:
    def __init__(self, unit, length):
        self.unit = unit
        self.length = length
    '''''
    def __eq__(self, other):
        if isinstance(other, QuantityMeasurement):
            return self.unit == other.unit and other.length == self.length

    def compareto(self, other):
        if isinstance(self.unit, Length) and isinstance(other.unit, Length):
            return Length.convert(self.unit, self.length) == Length.convert(other.unit, other.length)

        return False

    '''''
    def __eq__(self, other):
        if isinstance(other, QuantityMeasurement):
            return self.unit == other.unit and other.length == self.length
        if isinstance(self.unit, Length) and isinstance(other.unit, Length):
            if Length.convert(self.unit, self.length) == Length.convert(other.unit, other.length):
                return True
        return False

    def addition(self, other):
        return Length.convert(self.unit, self.length) + Length.convert(other.unit, other.length)
