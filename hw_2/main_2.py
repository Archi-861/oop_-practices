import math

# Task 1

class Data:
    day = int
    month = int
    year = int
    hour = int
    minute = int

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

class Time:
    hour = int
    minute = int

    def __init__(self, hour: int, minute: int):
        self.hour = hour
        self.minute = minute

class Patient:
    name = str
    age = int
    disease = str

    def __init__(self, name: str, age: int, disease: str):
        self.name = name
        self.age = age
        self.disease = disease

    def appointment(self, time: Time, data: Data):
        print(f'Пациент {self.name} записан {data.day}.{data.month}.{data.year}г. в {time.hour}:{time.minute}')

    def __str__(self):
        return f'Пациент - {self.name}, возраст - {self.age} лет, диагноз - {self.disease}'

# End Task 1

# Task 2

class Tourist:
    name = str

    def __init__(self, name: str):
        self.name = name

class TouristSpot:
    name = str
    country = str
    type = str

    def __init__(self, name: str, country: str, type: str):
        self.name = name
        self.country = country
        self.type = type

    def visit_place(self, tourist: Tourist):
        print(f'Турист {tourist.name} посетил {self.name}')

    def __str__(self):
        return f'Туристическая достопримечательность под названием {self.name} располагается в {self.country} и является {self.type} достопримечательностью'

# End Task 2

# Task 3

class ModelWindow:
    name = str
    coord_left_up_corner = list[int]
    horizon_size = int
    vertical_size = int
    color = str
    visible = bool
    frame = bool

    def __init__(self, name: str, coord_left_up_corner: list[int], horizon_size: int, vertical_size: int, color: str, visible: bool, frame: bool):
        self.name = name
        self.coord_left_up_corner = coord_left_up_corner
        self.horizon_size = horizon_size
        self.vertical_size = vertical_size
        self.color = color
        self.visible = visible
        self.frame = frame

    def __str__(self):
        return (f'Окно: {self.name}, '
                f'координаты верхнего левого угла: {self.coord_left_up_corner}, '
                f'размер по горизонтали: {self.horizon_size}, '
                f'размер по вертикали: {self.vertical_size},  '
                f'цвет окна: {self.color},'
                f'видимость: {self.visible},'
                f'рамка(состояние): {self.frame}')

    def window_move(self, coord_x: int, coord_y: int):
        if 1960 > coord_x > 0 and 1080 > coord_y > 0:
            self.coord_left_up_corner = [coord_x, coord_y]

    def window_change_height(self, new_value: int):
        pass

    def window_change_color(self, new_color: int):
        self.color = new_color
        print(f'Цвет окна изменен на {self.color}')

    def window_change_frame(self, new_frame: bool):
        self.frame = new_frame

    def window_change_visible(self, new_visible):
        self.visible = new_visible

#End Task 3

# Task 4

class ArrayUtils:

    @staticmethod
    def array_sum(array: list[int]) -> int:
        summ = 0
        for i in range(0, len(array)):
            summ += array[i]
        return summ

    @staticmethod
    def array_multi(array: list[int]) -> int:
        res = 1
        for i in range(0, len(array)):
            res *= array[i]
        return res

    @staticmethod
    def array_inverse(array: list[int]) -> list:
        new_array = array[::-1]
        return new_array

    @staticmethod
    def array_max(array: list[int]) -> int:
        max_elem = array[0]
        for i in range(1, len(array)):
            if max_elem < array[i]:
                max_elem = array[i]
        return max_elem

    @staticmethod
    def array_min(array: list[int]) -> int:
        min_elem = array[0]
        for i in range(1, len(array)):
            if min_elem < array[i]:
                min_elem = array[i]
        return min_elem

# End Task 4

# Task 5

class Vector:
    coord_x = float
    coord_y = float
    coord_z = float

    def __init__(self, coord_x: float, coord_y: float, coord_z: float):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.coord_z = coord_z

    def __str__(self):
        return (f'Координата X: {self.coord_x};'
                f'Координата Y: {self.coord_y};'
                f'Координата Z: {self.coord_z}.')

    def __add__(self, other):
        return self.coord_x + other.coord_x, self.coord_y + other.coord_y, self.coord_z + other.coord_z

    def __sub__(self, other):
        return self.coord_x - other.coord_x, self.coord_y - other.coord_y, self.coord_z - other.coord_z

    def __mul__(self, other):
        return self.coord_x * other.coord_x + self.coord_y * other.coord_y + self.coord_z * other.coord_z

    def vector_scalar_mul(self, other):
        new_coord_x = self.coord_z * other.coord_y - self.coord_y * other.coord_z
        new_coord_y = self.coord_x * other.coord_z - self.coord_z * other.coord_x
        new_coord_z = self.coord_y * other.coord_x - self.coord_x * other.coord_y
        return new_coord_x, new_coord_y, new_coord_z

    def vector_norma(self):
        norma = math.sqrt(self.coord_x ** 2 + self.coord_y ** 2 + self.coord_z ** 2)
        return norma

# End Task 5

# Task 6

class Fraction:
    numerator = int
    denominator = int

    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator

    @staticmethod
    def fraction_zero_check(check_denominator: int) -> bool:
        if check_denominator == 0:
            return False
        else:
            return True

    def __str__(self):
        if self.denominator == 1:
            res = f'{self.numerator}'
        else:
            res = f'{self.numerator}/{self.denominator}'
        return res

    def __add__(self, other):
        if Fraction.fraction_zero_check(self.denominator) == True and Fraction.fraction_zero_check(other.denominator) == True:
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        else:
            print('Знаменатель равен нулю!')

    def __sub__(self, other):
        if Fraction.fraction_zero_check(self.denominator) == True and Fraction.fraction_zero_check(other.denominator) == True:
            new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        else:
            print('Знаменатель равен нулю!')

    def __mul__(self, other):
        if Fraction.fraction_zero_check(self.denominator) == True and Fraction.fraction_zero_check(other.denominator) == True:
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        else:
            print('Знаменатель равен нулю!')

# End Task 6

# Task 7

class GeometryUtils:

    @staticmethod
    def square_circle(radius: float) -> float:
        return math.pi * radius ** 2

    @staticmethod
    def perimetr_circle(radius: float) -> float:
        return 2 * math.pi * radius

    @staticmethod
    def square_rectangle(side_a: float, side_b: float) -> float:
        return side_a * side_b

    @staticmethod
    def perimetr_rectangle(side_a: float, side_b: float) -> float:
        return 2 * (side_a + side_b)

    @staticmethod
    def square_triangle(side_a: float, side_b: float, side_c: float) -> float:
        pol_perimetr = (GeometryUtils.perimetr_triangle(side_a, side_b, side_c)) / 2
        return math.sqrt(pol_perimetr * (pol_perimetr - side_a) * (pol_perimetr - side_b) * (pol_perimetr - side_c))

    @staticmethod
    def perimetr_triangle(side_a: float, side_b: float, side_c: float) -> float:
        return side_a + side_b + side_c

# End Task 7

# Task 8

class Time:
    hour = int
    minute = int
    second = int

    def __init__(self, hour: int, minute: int, second: int):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __add__(self, other):
        self.hour = self.hour + other.hour
        self.minute = self.minute + other.minute
        self.second = self.second + other.second

    def __sub__(self, other):
        self.hour = self.hour - other.hour
        self.minute = self.minute - other.minute
        self.second = self.second - other.second

    def __mul__(self, other):
        self.hour = self.hour * other.hour
        self.minute = self.minute * other.minute
        self.second = self.second * other.second

    def time_transform(self):
        if self.second < 0 or self.minute < 0 or self.second < 0:
            return 'Неверный формат времени'
        else:
            buff_time = self.second + (self.minute * 60) + (self.hour * 120)
            new_hour = buff_time // 120
            new_min = buff_time % 120 + buff_time // 60
            new_sec = buff_time - (new_hour * 120) - (new_min * 60)
            self.hour = new_hour
            self.minute = new_min
            self.second = new_sec

    def __str__(self):
        if self.hour < 10:
            hour_print = '0' + str(self.hour)
            minute_print = '0' + str(self.minute)
            second_print = '0' + str(self.second)
            return f"{hour_print}:{minute_print}:{second_print}"
        else:
            hour_print = str(self.hour)
            minute_print = str(self.minute)
            second_print = str(self.second)
            return f"{hour_print}:{minute_print}:{second_print}"

# End Task 8