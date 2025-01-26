from __future__ import annotations

class Athlete:
    name = str
    age = int
    sport_type = str
    status = bool


    def __init__(self, name: str, age: int, sport_type: str, status: bool, achievement=None):
        if not isinstance(name, str):
            raise ValueError('Имя должно быть строкой')
        if not isinstance(age, int):
            raise ValueError('Возраст должен быть числом')
        if age < 0:
            raise ValueError('Возраст не может быть отрицательным')
        if not isinstance(sport_type, str):
            raise ValueError('Вид спорта должен быть строкой')
        if not isinstance(status, bool):
            raise ValueError('Текущий статус должен быть булевым значением (True/False)')

        self.__name = name
        self.__age = age
        self.__sport_type = sport_type
        if achievement is None:
            self.__achievement = []
        else:
            self.__achievement = achievement
        self.__status = True


    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_sport_type(self):
        return self.__sport_type

    def get_achievement(self):
        return self.__achievement


    def set_name(self, new_name: str):
        if not isinstance(new_name, str):
            raise ValueError('Имя должно быть строкой')
        self.__name = new_name

    def set_age(self, value: int):
        if not isinstance(value, int):
            raise ValueError('Возраст должен быть числом')
        if value < 0:
            raise ValueError('Возраст не может быть отрицательным')

        self.__age = value

    def set_sport_type(self, new_sport_type: str):
        if not isinstance(new_sport_type, str):
            raise ValueError('Вид спорта должен быть строкой')
        self.__sport_type = new_sport_type

    def set_achievement(self, new_achievement: Achievement):
        self.__achievement.append(new_achievement)

    def set_status(self, new_status: bool):
        if not isinstance(new_status, bool):
            raise ValueError('Состояние должно быть булевым значением (True/False)')

        self.__status = new_status

    def remove_achievement(self, achievement: str):
        if achievement in self.__achievement:
            self.__achievement.remove(achievement)
        else:
            raise ValueError('Такого достижения нет')

    def __str__(self):
        status = 'Активен'
        if self.__status == False:
            status = 'На пенсии'

        if self.__achievement == []:
            achievement = 'Достижений нет'
        else:
            achievement = self.__achievement
            achievement = ', '.join(achievement)

        return (f'Имя спортсмена: {self.__name};\n'
                f'Возраст: {self.__age};\n'
                f'Вид спорта: {self.__sport_type};\n'
                f'Список достижений: {achievement};\n'
                f'Статус: {status}.')


class Achievement:
    name = str

    def __init__(self, name: str):
        if not isinstance(name, str):
            raise ValueError('Достижение должно быть строкой')

        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, new_name: str):
        if not isinstance(new_name, str):
            raise ValueError('Название достижения должно быть строкой')
        self.__name = new_name


achiev_1 = Achievement('КМС')
achiev_2 = Achievement('МС')

ath_1 = Athlete('Alex', 50, 'Box', True)

ath_1.set_achievement(Achievement.get_name(achiev_1))
ath_1.set_achievement(Achievement.get_name(achiev_2))

print(ath_1)