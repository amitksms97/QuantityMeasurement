import enum


class Length(enum.Enum):
    FEET = 12.0
    YARD = 36.0
    INCH = 1.0
    CM = 0.4
    GALLON = 3.78
    LITRE = 1
    ML = 0.001

    def convert(self, length):
        return self.unit * length

'''''
class Volume(enum.Enum):
    GALLON = 3.78
    LITRE = 1
    ML = 0.001

    def convert(self, volume):
        return self.unit * volume
'''''

