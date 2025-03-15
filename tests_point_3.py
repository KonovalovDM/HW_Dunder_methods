# %%file tests_point_3.py

from distance import Millimeter, Centimeter, Meter, Inch

def test_add_method():
    left = Meter(9.2)
    right = Inch(9.2)
    assert (left + right).as_millimeters() == 9433.68, 'Метод __add__ реализован не корректно'

def test_sub_method():
    left = Inch(86.44)
    right = Millimeter(94.78)
    assert (left - right).as_millimeters() == 2100.796, 'Метод __sub__ реализован не корректно'

def test_mul_method():
    left = Centimeter(94.95)
    right = Millimeter(10.8)
    assert (left * right).as_millimeters() == 10254.6, 'Метод __mul__ реализован не корректно'

def test_truediv_method():
    left = Meter(38.07)
    right = Millimeter(44.74)
    assert (left / right).as_millimeters() == 850.9164059, 'Метод __mul__ реализован не корректно'