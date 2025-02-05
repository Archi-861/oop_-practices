class Car:
    brand: str
    model: str or int
    release_year: int
    color: str
    mileage: int
    status: bool
    current_speed: int

    def __init__(self, brand: str, model: str or int, release_year: int, color: str, mileage: int, status: bool, current_speed: int or float):

        if not isinstance(brand, str):
            raise ValueError('Марка должна быть строкой')

        if not isinstance(model, (str, int)):
            raise ValueError('Модель должна быть строкой или целым числом')

        if release_year < 1886 or release_year > 2025:
            raise ValueError('Год производства не может быть ранее 1886 года и позднее 2025 года')

        if not isinstance(release_year, int):
            raise ValueError('Год выпуска должен быть целым числом')

        if not isinstance(color, str):
            raise ValueError('Цвет должен быть строкой')

        if mileage < 0:
            raise ValueError('Пробег не может быть отрицательным')

        if not isinstance(mileage, int):
            raise ValueError('Пробег должен быть целым числом')

        if not isinstance(status, bool):
            raise ValueError('Состояние должно быть булевым значением True/False')

        if current_speed < 0:
            raise ValueError('Текущая скорость не может быть отрицательной')

        if not isinstance(current_speed, (int, float)):
            raise ValueError('Текущая скорость должна быть целым или вещественным числом')

        self.__brand = brand
        self.__model = model
        self.__release_year = release_year
        self.__color = color
        self.__mileage = mileage
        self.__status = status
        self.__current_speed = current_speed


    def start_engine(self):
        self.__status = True


    def stop_engine(self):
        self.__status = False


    def check_status(self):

        status = 'Запущен'

        if self.__status is False:
            status = 'Остановлен'

        return status


    def check_current_speed(self):
        return self.__current_speed


    def check_mileage(self):
        return self.__mileage


    def change_current_speed(self, new_speed: int or float):

        if not isinstance(new_speed, (int, float)):
            raise ValueError('Текущая скорость должна быть целым или вещественным числом')

        if new_speed + self.__current_speed > 200 or new_speed + self.__current_speed < 0:
            print('Текущая скорость не может быть отрицательной и выше 200 км/ч\n')
            return False

        self.__current_speed += new_speed


    def change_color(self, new_color: str):

        if not isinstance(new_color, str):
            raise ValueError('Цвет должен быть строкой')

        self.__color = new_color


    def __str__(self):

        status = 'Запущен'

        if self.__status is False:
            status = 'Остановлен'

        return (f'Марка автомобиля: {self.__brand};\n'
                f'Модель автомобиля: {self.__model};\n'
                f'Год выпуска: {self.__release_year};\n'
                f'Цвет: {self.__color};\n'
                f'Пробег: {self.__mileage} км;\n'
                f'Состояние: {status};\n'
                f'Текущая скорость: {self.__current_speed} км/ч.\n')


car_1 = Car('BMW', 740, 2019, 'Черный', 15000, True, 120)
print(car_1)

car_1.start_engine()
print(car_1)

car_1.change_current_speed(-150)
print(car_1)