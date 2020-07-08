from decimal import Decimal


def test_float():
    a = 4.2
    b = 2.1
    print(a + b)  #6.300000000000001


def test_decimal():
    a = Decimal('4.2')
    b = Decimal('2.1')
    print(a + b)  #6.3