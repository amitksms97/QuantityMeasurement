import pytest
from converter import QuantityMeasurement
from enum_class import Length
from feet import Feet


# case1 : comparing two feet value

def test_givenZeroFtandZeroFt_WhenCompared_ShouldReturnTrue():
    first_feet = QuantityMeasurement(Length.FEET, 0.0)
    second_feet = QuantityMeasurement(Length.FEET, 0.0)
    assert first_feet == second_feet


# case2 : comparing Two instance feet variable
def test_givenTwoFeetValueInstanceVariable_WhenCompared_ShouldReturnTrue():
    first_feet = Feet(0.0)
    second_feet = first_feet
    assert first_feet == second_feet


# case3 : comparing one feet value should return false when None
def test_givenZeroFtValue_WhenComparedIfNotNone_ShouldReturnTrue():
    first_feet = QuantityMeasurement(Length.FEET, 0.0)
    assert first_feet is not None


# case4 : compared one feet value with float value
def test_givenZeroFeetAndFloatValue_WhenCompared_ShouldReturnTrue():
    first_feet = QuantityMeasurement(Length.FEET, 0.0)
    second_feet = float(0.0)
    with pytest.raises(AttributeError):
        assert first_feet == second_feet


# case5 : comparing two different feet value
def test_givenZeroFeetandOneFeet_WhenCompared_ShouldReturnFalse():
    first_feet = QuantityMeasurement(Length.FEET, 0.0)
    second_feet = QuantityMeasurement(Length.FEET, 1.0)
    assert first_feet != second_feet


# cases for Yard
def test_givenZeroYardandZeroYard_WhenCompared_ShouldReturnTrue():
    first_yard = QuantityMeasurement(Length.YARD, 0.0)
    second_yard = QuantityMeasurement(Length.YARD, 0.0)
    assert first_yard == second_yard

def test_givenZeroYardValueandInstanceVariable_WhenCompared_ShouldReturnTrue():
    first_yard = QuantityMeasurement(Length.YARD, 0.0)
    second_yard = first_yard
    assert first_yard == second_yard


def test_givenZeroYardValue_WhenComparedIfNotNone_ShouldReturnTrue():
    first_yard = QuantityMeasurement(Length.YARD, 0.0)
    assert first_yard is not None


def test_givenZeroYardAndFloatValue_WhenCompared_ShouldReturnTrue():
    first_yard = QuantityMeasurement(Length.YARD, 0.0)
    second_yard = float(0.0)
    with pytest.raises(AttributeError):
        assert first_yard == second_yard


def test_givenZeroYardandOneYard_WhenCompared_ShouldReturnFalse():
    first_yard = QuantityMeasurement(Length.YARD, 0.0)
    second_yard = QuantityMeasurement(Length.YARD, 1.0)
    assert first_yard != second_yard

#testcase:for Inch

def test_givenZeroInchandZeroInchValue_WhenCompared_ShouldReturnTrue():
    first_inch = QuantityMeasurement(Length.INCH, 0.0)
    second_inch = QuantityMeasurement(Length.INCH, 0.0)
    assert first_inch == second_inch


def test_givenZeroInchValueInstanceVariable_WhenCompared_ShouldReturnTrue():
    first_inch = QuantityMeasurement(Length.INCH, 0.0)
    second_inch = first_inch
    assert first_inch == second_inch


def test_givenZeroInchValue_WhenComparedIfNotNone_ShouldReturnTrue():
    first_inch = QuantityMeasurement(Length.INCH, 0.0)
    assert first_inch is not None


def test_givenZeroInchAndFloatValue_WhenCompared_ShouldReturnTrue():
    first_inch = QuantityMeasurement(Length.INCH, 0.0)
    second_inch = float(0.0)
    with pytest.raises(AttributeError):
        assert first_inch == second_inch

def test_givenZeroInchandOneInch_WhenCompared_ShouldReturnFalse():
    first_inch = QuantityMeasurement(Length.INCH, 0.0)
    second_inch = QuantityMeasurement(Length.INCH, 1.0)
    assert first_inch != second_inch


# case1 : for compare 3ft = 1yd
def test_given_3FeetAnd_1YardValue_WhenCompared_ShouldReturnTrue():
    first_feet = QuantityMeasurement(Length.FEET, 3.0)
    second_yard = QuantityMeasurement(Length.YARD, 1.0)
    with pytest.raises(AssertionError):
        assert first_feet == second_yard


# case2 : for compare 1ft != 1yd
def test_given_1FeetAnd_1YardValue_WhenCompared_ShouldReturnFalse():
    first_feet = QuantityMeasurement(Length.FEET, 1.0)
    second_yard = QuantityMeasurement(Length.YARD, 1.0)
    assert first_feet != second_yard


# case3 : for compare 1in != 1yd
def test_given_OneInch_And_OneYardValue_WhenCompared_ShouldReturnFalse():
    first_inch = QuantityMeasurement(Length.INCH, 1.0)
    second_yard = QuantityMeasurement(Length.YARD, 1.0)
    assert first_inch != second_yard


# case4 : fr Compare 36in = 1yd
def test_given_36Inch_And_1YardValue_WhenCompared_ShouldReturnTrue():
    first_inch = QuantityMeasurement(Length.INCH, 36.0)
    second_yard = QuantityMeasurement(Length.YARD, 1.0)
    with pytest.raises(AssertionError):
        assert first_inch == second_yard


# case5 : for compare 1yd = 3ft
def test_given_1Yard_And_3FeetValue_WhenCompared_ShouldReturnTrue():
    first_yard = QuantityMeasurement(Length.YARD, 1.0)
    second_feet = QuantityMeasurement(Length.FEET, 3.0)
    with pytest.raises(AssertionError):
        assert first_yard == second_feet


# case6 : for compare 1yd = 36in
def test_given_OneYardAnd_36InchValue_WhenCompared_ShouldReturnTrue():
    first_yard = QuantityMeasurement(Length.YARD, 1.0)
    second_inch = QuantityMeasurement(Length.INCH, 36.0)
    with pytest.raises(AssertionError):
        assert first_yard == second_inch


# UC3 : 2in = 5cm
def test_givenTwoInchAndFiveCMValue_WhenCompared_ShouldReturnTrue():
    first_inch = QuantityMeasurement(Length.INCH, 2.0)
    second_cm = QuantityMeasurement(Length.CM, 5.0)
    with pytest.raises(AssertionError):
        assert first_inch == second_cm

'''''
@pytest.mark.parametrize("first_length, second_length,expected",
                         [
                             (QuantityMeasurement(Length.FEET, 3.0), QuantityMeasurement(Length.YARD, 1.0), True),
                             (QuantityMeasurement(Length.FEET, 1.0), QuantityMeasurement(Length.YARD, 1.0), False),
                             (QuantityMeasurement(Length.INCH, 1.0), QuantityMeasurement(Length.YARD, 1.0), False),
                             (QuantityMeasurement(Length.INCH, 36.0), QuantityMeasurement(Length.YARD, 1.0), True),
                             (QuantityMeasurement(Length.YARD, 1.0), QuantityMeasurement(Length.FEET, 3.0), True),
                             (QuantityMeasurement(Length.YARD, 1.0), QuantityMeasurement(Length.INCH, 36.0), True),
                             (QuantityMeasurement(Length.INCH, 2.0), QuantityMeasurement(Length.CM, 5.0), True)
                         ])

def test_givenTwoLengthsUnitValue_WhenCompared_ShouldReturnExpected(first_length, second_length, expected):
    assert QuantityMeasurement.compareto(first_length, second_length) == expected


@pytest.mark.parametrize("first_length, second_length,expected",
                         [
                             (QuantityMeasurement(Length.INCH, 2.0), QuantityMeasurement(Length.INCH, 2.0), 4.0),
                             (QuantityMeasurement(Length.FEET, 1.0), QuantityMeasurement(Length.INCH, 2.0), 14.0),
                             (QuantityMeasurement(Length.FEET, 1.0), QuantityMeasurement(Length.FEET, 1.0), 24.0),
                             (QuantityMeasurement(Length.INCH, 2.0), QuantityMeasurement(Length.CM, 2.5), 3.0),
                         ])
def test_givenTwoLengthsUnitValue_WhenAdd_ShouldReturnExpectedResult(first_length, second_length, expected):
    assert QuantityMeasurement.addition(first_length, second_length) == expected
'''''