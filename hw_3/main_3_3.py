from __future__ import annotations

class Robot:
    part_number = any
    model = any
    current_task = str
    charge_level = int
    status = bool

    def __init__(self, part_number: any, model: any, current_task: str, charge_level: int, status: bool):

        if not isinstance(current_task, str):
            raise ValueError('Текущая задача должно быть строкой')

        if not isinstance(charge_level, int):
            raise ValueError('Уровень заряда должен быть числом')

        if charge_level < 0:
            raise ValueError('Уровень заряда не может быть отрицательной')

        if not isinstance(status, bool):
            raise ValueError('Состояние должно быть булевым значением (True/False')

        self.__part_number = part_number
        self.__model = model
        self.__current_task = current_task
        self.__charge_level = charge_level
        self.__status = True


    def get_part_number(self):
        return self.__part_number

    def get_model(self):
        return self.__model

    def get_current_task(self):
        return self.__current_task

    def get_charge_level(self):
        return self.__charge_level

    def get_status(self):
        return self.__status


    def set_part_number(self, new_part_number: any):
        self.__part_number = new_part_number

    def set_model(self, new_model: any):
        self.__model = new_model

    def set_current_task(self, new_current_task: str):

        if not isinstance(new_current_task, str):
            raise ValueError('Текущая задача должна быть строкой')

        self.__current_task = new_current_task

    def set_charge_level(self, value: int):

        if not isinstance(value, int):
            raise ValueError('Уровень заряда должен быть числом')

        if value < 0:
            raise ValueError('Уровень заряда не может быть отрицательным')

        self.__charge_level = value

    def set_status(self, new_status: bool):

        if not isinstance(new_status, bool):
            raise ValueError('Состояние должно быть булевым значением (True/False)')

        self.__status = new_status


    def __str__(self):
        status = 'В работе'
        if self.__status is False:
            status = 'На перерыве'

        return (f'Серийный номер: {self.__part_number};\n'
                f'Модель: {self.__model};\n'
                f'Текущая задача: {self.__current_task};\n'
                f'Уровень заряда: {self.__charge_level};\n'
                f'Состояние: {status}.')

r_1 = Robot('Wally', 'Garbage collector', 'Clean up', 55, True)
print(r_1)

r_1.set_current_task('Waste recycling')
print(r_1)

r_1.set_charge_level(95)
print(r_1)

r_1.set_status(False)
print(r_1)