class Student:
    first_name: str
    last_name: str
    age: int
    average_mark: float

    def __init__(self, first_name: str, last_name: str, age: int, average_mark: float):

        if not isinstance(first_name, str):
            raise TypeError('Имя должно быть строкой')

        if not isinstance(last_name, str):
            raise TypeError('Фамилия должна быть строкой')

        if not isinstance(age, int) and age > 0:
            raise TypeError('Возраст должен быть целым положительным числом')

        if not isinstance(average_mark, float) and average_mark > 0:
            raise TypeError('Средний балл должен быть вещественным положительным числом')

        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__average_mark = average_mark



    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_age(self):
        return self.__age

    def get_average_mark(self):
        return self.__average_mark



    def set_first_name(self, new_first_name: str):

        if not isinstance(new_first_name, str):
            raise TypeError('Имя должно быть строкой')

        self.__first_name = new_first_name

    def set_last_name(self, new_last_name: str):

        if not isinstance(new_last_name, str):
            raise TypeError('Фамилия должна быть строкой')

        self.__last_name = new_last_name

    def set_age(self, new_age: int):

        if not isinstance(new_age, int) and new_age > 0:
            raise TypeError('Возраст должен быть целым положительным числом')

        self.__age = new_age

    def set_average_mark(self, value: float):

         if not isinstance(value, float) and value > 0:
             raise TypeError('Средний балл должен быть вещественным положительным числом')

         self.__average_mark = value



    def __eq__(self, other): # Оператор сравнения ==

        result = 'Средние баллы разные'

        if self.__average_mark == other.__average_mark:
            result = 'Средние баллы одинаковые'

        print(result)



    def __ne__(self, other): # Оператор неравенства !=

        result = 'Средние баллы одинаковые'

        if self.__average_mark != other.__average_mark:
            result = 'Средние баллы разные'

        print(result)



    def __lt__(self, other): # Оператор меньше <

        result = f'У студента {self.__first_name} {self.__last_name} средний балл больше'

        if self.__average_mark < other.__average_mark:
            result = f'У студента {self.__first_name} {self.__last_name} средний балл меньше'

        print(result)



    def __gt__(self, other): # Оператор больше >

        result = f'У студента {self.__first_name} {self.__last_name} средний балл меньше'

        if self.__average_mark > other.__average_mark:
            result = f'У студента {self.__first_name} {self.__last_name} средний балл больше'

        print(result)



    def __le__(self, other):

        result = f'У студента {self.__first_name} {self.__last_name} средний балл больше или равно среднему баллу студента {other.__first_name} {other.__last_name}'

        if self.__average_mark <= other.__average_mark:
            result = f'У студента {self.__first_name} {self.__last_name} средний балл меньше или равно среднему баллу студента {other.__first_name} {other.__last_name}'

        print(result)

    def __ge__(self, other):

        result = f'У студента {self.__first_name} {self.__last_name} средний балл меньше или равно среднему баллу студента {other.__first_name} {other.__last_name}'

        if self.__average_mark >= other.__average_mark:
            result = f'У студента {self.__first_name} {self.__last_name} средний балл больше или равно среднему баллу студента {other.__first_name} {other.__last_name}'

        print(result)



    def __str__(self):
        return (f'Имя ученика: {self.__first_name};\n'
                f'Фамилия ученика: {self.__last_name};\n'
                f'Возраст: {self.__age} лет;\n'
                f'Средний балл: {self.__average_mark}.\n')


s_1 = Student('Alex', 'Alexov', 18, 3.5)
s_2 = Student('Nick', 'Nickovich', 19, 4.87)
print(s_1)
print(s_2)

Student.__eq__(s_2, s_1)
Student.__ne__(s_2, s_1)

Student.__lt__(s_2, s_1)
Student.__lt__(s_1, s_2)

Student.__gt__(s_2, s_1)
Student.__gt__(s_1, s_2)

Student.__le__(s_2, s_1)
Student.__le__(s_1, s_2)

Student.__ge__(s_2, s_1)
Student.__ge__(s_1, s_2)