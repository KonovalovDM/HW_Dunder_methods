# %%file tests_point_4.py

from distance import Millimeter, Centimeter, Meter, Inch

def test_hash_method():
    instance = Meter(20.64)
    assert hash(instance) == hash(20640)

def test_eq_method():
    left = Millimeter(20.64)
    right = Meter(0.02064)
    assert left == right, 'Неверный результат сравнения'

def test_lt_method():
    left = Millimeter(74.0)
    right = Meter(0.075)
    assert left < right, 'Неверный результат сравнения'

def test_ge_method():
    left = Meter(57.97)
    assert not (left.__ge__(left) is NotImplemented), 'Метод __ge__ не реализован'