# HW_Dunder_methods
## *** Изучение Dunder_methods Дандер методов***

### Задача в последовательном написании кода и прогонке специально созданных тестов после каждого шага
### Каждое последующее задание зависит от реализации предыдущего

### Шаг 1
    ***В модуле distance.py определенен класс Millimeter он является базовым классом дочерних классов 
    Centimeter, Meter, Inch. Классы имеют атрибуты label и ratio, последний определяет отношение длины
    к базововому значению длины (базовые еденицы измерения это миллиметр). У класса Millimeter атрибут 
    ratio равен 1 значит отношение выглядит как 1 к 1.
    Также в базовом классе реализован метод as_millimeters который возвращает значение в базовых единицах
    измерения.***

    ***Инициализация
    Установите значения атрибута ratio в определении классов Centimeter, Meter и Inch. Например, для класса
    Inch значение атрибута ratio будет равно 25.4.
    Дополните определение dunder метод __init__. Метод принимает один аргумент value любого типа (int, float,
    Millimeter, Centimeter и т.д.). Если значение агрумента value соответствует типам int тогда необходимо
    преобразовать значение к типу float и присвоить результат атрибуту self._value. Во всех остальных случаях
    нужно конвертировать значение. Чтобы выполнить конвертацию нужно вызвать метод value.as_millimeters и
    разделить значение на self.ratio, преобразовать в тип float, а результат присвоить атрибуту self._value.***

#### Выполняем проверку, запускаем код прграммы distance.py в случае отсутствия ошибок запускаем tests_poin_1.
    Любым из нижеописанных способов:
    1. **Использование окна терминала в PyCharm:**
        - Откройте терминал внутри PyCharm (обычно он доступен в нижней панели).
        - Введите команду `python -m pytest -vs tests_point_1.py и нажмите Enter.
        Это запустит pytest для указанного файла теста.

    2. **Конфигурация запуска:**
        - В меню PyCharm выберите "Run" -> "Edit Configurations..."
        - Нажмите на "+" и выберите "Python tests" -> "pytest".
        - Укажите путь к вашим тестовым файлам или директории с тестами.
        - Сохраните конфигурацию и запустите её.

    3. **Контекстное меню:**
        - Найдите папку с тестами в дереве проекта.
        - Щелкните правой кнопкой мыши по папке или конкретным файлам и выберите "Run pytest in ...".

python -m pytest -vs tests_point_1.py

#### Корректный результат
    tests_point_1.py::test_value_type PASSED
    tests_point_1.py::test_init_millimeter PASSED
    tests_point_1.py::test_convert_millimeters_to_meters PASSED
    tests_point_1.py::test_convert_centimeters_to_meters PASSED
    tests_point_1.py::test_convert_inches_to_meters PASSED
    tests_point_1.py::test_convert_millimeters_to_inches PASSED
    tests_point_1.py::test_convert_centimeters_to_inches PASSED
    tests_point_1.py::test_convert_meters_to_inches PASSED

### Шаг 2
    ***Представление объекта
    Реализуйте метод __repr__. Помните, что результат вызова функции repr по возможности должен возвращать
    корректное python выражение.***

#### Выполняем проверку, запускаем tests_poin_2 (способы описаны выше)
    python -m pytest -vs tests_point_2.py

#### Корректный результат
    tests_point_2.py::test_repr_method PASSED

### Шаг 3
    ***Арифметические операции
    Реализуйте методы __add__, __sub__, __mul__ и __truediv__. Данные методы должны возвращать новый объект 
    того же типа, что и класс у которого вызывается данный метод, то есть type(self). Методы реализуются с 
    помощью выполнения арифметических операций над результатами вызваных у операндов методов as_millimeters
    разделенных на значение атрибута self.ratio, то есть значение атрибута левого операнда.***

#### Выполняем проверку, запускаем tests_poin_3
    python -m pytest -vs tests_point_3.py

#### Корректный результат
    tests_point_3.py::test_add_method PASSED
    tests_point_3.py::test_sub_method PASSED
    tests_point_3.py::test_mul_method PASSED
    tests_point_3.py::test_truediv_method PASSED

### Шаг 4
    ***Сравнение объектов
    Для сравнения объектов реализуйте методы сравнения __eq__, __le__ и метод __hash__, а также оберните 
    класс Millimeter в декоратор total_ordering. Метод __hash__ нужно реализовать вызовом метода функции 
    hash над результатом вызова метода self.as_millimeters. Сравнение объектов методом __eq__ реализуется 
    с помощью сравнения хеш функций операндов. Реализация метода __le__ подразумевает сравнение оператором
    результатов вызова метода as_millimeters у сравниваемых объектов.

#### Выполняем проверку, запускаем tests_poin_4
    python -m pytest -vs tests_point_4.py

#### Корректный результат
    tests_point_4.py::test_hash_method PASSED
    tests_point_4.py::test_eq_method PASSED
    tests_point_4.py::test_lt_method PASSED
    tests_point_4.py::test_ge_method PASSED

### Шаг 5
    ***Преобразование объектов
    Реализайте методы __int__ и __float__, результат методов должен представлять из себя расстояние в 
    миллиметрах с преобразованием к соответствующему типу.

#### Выполняем проверку, запускаем tests_poin_5
    python -m pytest -vs tests_point_5.py

#### Корректный результат
    tests_point_5.py::test_int_value_method PASSED
    tests_point_5.py::test_int_type_method PASSED
    tests_point_5.py::test_float_value_method PASSED

### Финальное тестирование
### Окончательный результат прогонки тестов должен выглядеть так:

    запуск тестов в терминале:
    python -m pytest -vs tests_point_1.py tests_point_2.py tests_point_3.py tests_point_4.py tests_point_5.py

    tests_point_1.py::test_value_type PASSED
    tests_point_1.py::test_init_millimeter PASSED
    tests_point_1.py::test_convert_millimeters_to_meters PASSED
    tests_point_1.py::test_convert_centimeters_to_meters PASSED
    tests_point_1.py::test_convert_inches_to_meters PASSED
    tests_point_1.py::test_convert_millimeters_to_inches PASSED
    tests_point_1.py::test_convert_centimeters_to_inches PASSED
    tests_point_1.py::test_convert_meters_to_inches PASSED
    tests_point_2.py::test_value_type PASSED
    tests_point_2.py::test_init_millimeter PASSED
    tests_point_2.py::test_convert_millimeters_to_meters PASSED
    tests_point_2.py::test_convert_centimeters_to_meters PASSED
    tests_point_2.py::test_convert_inches_to_meters PASSED
    tests_point_2.py::test_convert_millimeters_to_inches PASSED
    tests_point_2.py::test_convert_centimeters_to_inches PASSED
    tests_point_2.py::test_convert_meters_to_inches PASSED
    tests_point_3.py::test_add_method PASSED
    tests_point_3.py::test_sub_method PASSED
    tests_point_3.py::test_mul_method PASSED
    tests_point_3.py::test_truediv_method PASSED
    tests_point_4.py::test_hash_method PASSED
    tests_point_4.py::test_eq_method PASSED
    tests_point_4.py::test_lt_method PASSED
    tests_point_4.py::test_ge_method PASSED
    tests_point_5.py::test_int_value_method PASSED
    tests_point_5.py::test_int_type_method PASSED
    tests_point_5.py::test_float_value_method PASSED
