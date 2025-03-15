# %%file tests_point_5.py

from distance import Millimeter, Centimeter, Meter, Inch

import random

def test_int_value_method():
    value = random.random()
    instance = Meter(value)
    assert int(instance) == int(value * 1000)

def test_int_type_method():
    instance = Meter(36.94)
    assert type(int(instance)) is int

def test_float_value_method():
    value = random.random()
    instance = Inch(value)
    assert float(instance) == float(round(value * 25.4, 5))

def test_int_type_method():
    instance = Inch(43.63)
    assert type(float(instance)) is float