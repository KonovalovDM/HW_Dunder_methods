#@title Код модуля distance.py

# %%file distance.py

from functools import total_ordering
from typing import Any, Union


@total_ordering
class Millimeter:
    label = 'мм'
    ratio = 1 # Отношение определяемой еденицы измерения к миллиметрам

    def __init__(self, value: Any) -> None:
        if isinstance(value, (int, float)):
          self._value = float(value)
        elif isinstance(value, Millimeter):
          self._value = value.as_millimeters() / self.ratio
        else:
          raise TypeError("Неподдерживаемый тип данных: {type(value)}")

    # def __lt__(self, other):
    #     if not isinstance(other, Millimeter):
    #         return NotImplemented
    #     return self.as_millimeters() < other.as_millimeters()

    def __eq__(self, other) -> bool:
        """Сравнение объектов на равенство через хеш-функции."""
        if not isinstance(other, Millimeter):
            return NotImplemented
        return hash(self) == hash(other)

    def __le__(self, other) -> bool:
        """Сравнение объектов на меньше или равно."""
        if not isinstance(other, Millimeter):
            return NotImplemented
        return self.as_millimeters() <= other.as_millimeters()

    def __hash__(self) -> int:
        """Хеш-функция на основе значения в миллиметрах."""
        return hash(self.as_millimeters())

    def as_millimeters(self) -> float:
        """Возвращает значение в миллиметрах с округлением до 7 знаков."""
        return round(self._value * self.ratio, 7)

    def __int__(self) -> int:
        """Возвращает значение в миллиметрах как целое число"""
        return int(self.as_millimeters())

    def __float__(self) -> float:
        """Возвращает значение в миллиметрах как вещественное число с округлениме до 5 знаков."""
        return round(self.as_millimeters(), 5)

    def __repr__(self) -> str:
        """Строковое представление объекта."""
        return f"{self.__class__.__name__}({self._value})"

    def __add__(self, other):
        if not isinstance(other, Millimeter):
            return NotImplemented
        result_mm = self.as_millimeters() + other.as_millimeters()
        return type(self)(result_mm / self.ratio)

    def __sub__(self, other):
        if not isinstance(other, Millimeter):
            return NotImplemented
        result_mm = self.as_millimeters() - other.as_millimeters()
        return type(self)(result_mm / self.ratio)

    def __mul__(self, other: Union[float, 'Millimeter']):
        if isinstance(other, (int, float)):
            result_mm = self.as_millimeters() * other
            return type(self)(result_mm / self.ratio)
        elif isinstance(other, Millimeter):
            result_mm = self.as_millimeters() * other.as_millimeters()
            return type(self)(result_mm / self.ratio)
        else:
            return NotImplemented

    def __truediv__(self, other: Union[float, 'Millimeter']):
        if isinstance(other, (int, float)):
            result_mm = self.as_millimeters() / other
            return type(self)(result_mm / self.ratio)
        elif isinstance(other, Millimeter):
            result_mm = self.as_millimeters() / other.as_millimeters()
            return type(self)(result_mm / self.ratio)
        else:
            return NotImplemented

class Centimeter(Millimeter):
    label = 'см'
    ratio = 10  # 1 см = 10 мм

class Meter(Millimeter):
    label = 'метр'
    ratio = 1000  # 1 метр = 1000 мм

class Inch(Millimeter):
    label = 'дюйм'
    ratio = 25.4  # 1 дюйм = 25.4 мм