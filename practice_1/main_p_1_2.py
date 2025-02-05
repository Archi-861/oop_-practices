from __future__ import annotations


class Smartphone:
    brand: str
    model: str or int
    os: str
    built_in_memory: int
    ram: int
    charge_level: int
    status: bool
    applications: list[Application]

    def __init__(self, brand: str, model: str or int, os: str, built_in_memory: int, ram: int, charge_level: int, status: bool, applications=None):

        if not isinstance(brand, str):
            raise ValueError('Марка должна быть строкой')

        if not isinstance(model, (str, int)):
            raise ValueError('Модель должна быть строкой или целыми числом')

        if not isinstance(os, str):
            raise ValueError('Операционная система должна быть строкой')

        if not isinstance(built_in_memory, int):
            raise ValueError('Встроенная память должна быть')

        if not isinstance(ram, int):
            raise ValueError('Оперативная память должна быть целым числом')

        if 0 > charge_level > 100:
            raise ValueError('Уровень заряда не может быть отрицательным или больше 100')

        if not isinstance(charge_level, int):
            raise ValueError('Заряд батареи должен быть целым числом')

        if not isinstance(status, bool):
            raise ValueError('Состояние должно быть булевым значением True/False')

        self.__brand = brand
        self.__model = model
        self.__os = os
        self.__built_in_memory = built_in_memory
        self.__ram = ram
        self.__charge_level = charge_level
        self.__status = status
        self.__applications = applications or []

    def __str__(self):

        applications = self.__applications
        applications = ', '.join(applications)
        if len (self.__applications) == 0:
            applications = 'Приложений нет'

        status = 'Включен'

        if self.__status is False:
            status = 'Выключен'

        return (f'Марка смартфона: {self.__brand};\n'
                f'Модель смартфона: {self.__model};\n'
                f'Операционная система: {self.__os};\n'
                f'Объем встроенной памяти: {self.__built_in_memory};\n'
                f'Объем оперативной памяти: {self.__ram};\n'
                f'Заряд батареи: {self.__charge_level};\n'
                f'Приложения: {applications}\n'
                f'Состояние: {status}\n')


    def turn_on(self):
        self.__status = True

    def turn_off(self):
        self.__status = False


    def installation_os(self, new_os: str):

        if not isinstance(new_os, str):
            raise ValueError('Операционная система должна быть строкой')

        self.__os = new_os


    def add_application(self, applications: Application):

        # if not isinstance(applications, str):
        #     raise ValueError('Приложение должно быть строкой')

        self.__applications.append(applications)


    def remove_application(self,  applications: Application):

        if not isinstance(applications, str):
            raise ValueError('Приложение должно быть строкой')

        if applications in self.__applications:
            self.__applications.remove(applications)

        else:
            print('Такого приложения нет на этом смартфоне. Удаление невозможно')
            return False


    def change_charge_level(self, value):

        if self.__charge_level + value < 0 or self.__charge_level + value > 100:
            raise ValueError('Уровень заряда не может быть отрицательным числом или больше 100')

        if not isinstance(value, int):
            raise ValueError('Уровень заряда должен быть целым числом')

        self.__charge_level += value


    def check_charge_level(self):
        print(f'Текущий уровень заряда батареи {self.__charge_level} %')

    def check_status(self):

        status = 'Включен'

        if self.__status is False:
            status = 'Выключен'

        print(f'В данный момент смартфон {status}')




class Application:
    name: str

    def __init__(self, name: str):

        if not isinstance(name, str):
            raise ValueError('Приложение должно быть строкой')

        self.__name = name

    def get_name(self):
        return self.__name



s_1 = Smartphone('Apple', 'Iphone 15', 'IOS', 512, 8, 58, True)
s_1.turn_off()
print(s_1)

s_1.installation_os('Android')
print(s_1)


ap_1 = Application('Instagram')
s_1.add_application(ap_1.get_name())
print(s_1)