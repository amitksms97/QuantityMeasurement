from enum_class import Length
from converter import QuantityMeasurement

if __name__ == '__main__':
    print("Welcome to Quantity Measurement Program")
    first_feet = QuantityMeasurement(Length.FEET, 2.0)
    second_feet = QuantityMeasurement(Length.FEET, 2.0)
    addition = QuantityMeasurement.addition(first_feet, second_feet)
    print("first_feet", addition)
    print(("second_feet", second_feet))
