import enum


class Length(enum.Enum):
    FEET = 12.0
    YARD = 36.0
    INCH = 1.0

    def convert(self, length):
        return self.unit * length
