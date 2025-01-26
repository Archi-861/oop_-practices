from __future__ import annotations


class Wizard:
    name = str
    house: str
    magic_level = int
    spells = list
    status = bool

    def __init__(self, name: str, house: str, magic_level: int, status: str, spells=None):
        if not isinstance(name, str):
            raise ValueError('Имя волшебника должно быть строкой')
        if not isinstance(house, str):
            raise ValueError('Название факультета должно быть строкой')
        if not isinstance(magic_level, int):
            raise ValueError('Уровень магической силы должно быть число')
        if not magic_level >= 0:
            raise ValueError('Уровень магической силы не может быть отрицательным')
        if not isinstance(status, str):
            raise isinstance('Статус волшебника должно быть строкой')

        self.__name = name
        self.__house = house
        self.__magic_level = magic_level

        if spells is None:
            self.__spells = []
        else:
            self.__spells = spells

        self.__status = status



    def get_name(self):
        return self.__name


    def get_house(self):
        return self.__house


    def get_magic_level(self):
        return self.__magic_level


    def get_spells(self):
        return self.__spells


    def get_status(self):
        return self.__status


    def set_house(self, house: str):
        self.__house = house


    def set_magic_level(self, magic_level: int):

        if magic_level < 0:
            print('Уровень магической силы не может быть отрицательным!')

        else:
            self.__magic_level = magic_level


    def set_status(self, status: str):
        self.__status = status


    def add_spell(self, spell):
        if not isinstance(spell, str):
            raise ValueError('Заклинание должно быть строкой')
        self.__spells.append(spell)


    def remove_spell(self, spell):
        if spell in self.__spells:
            self.__spells.remove(spell)
        else:
            raise ValueError('Такого заклинания нет')


    def increase_magic_level(self, amount: int):
        if not amount >= 0:
            raise ValueError('Уровень магической силы не может быть отрицательным')
        self.__magic_level = amount


    def __str__(self):
        if self.__spells == []:
            spells = 'Заклинаний нет'
        else:
            spells = self.__spells
            spells = ', '.join(spells)

        wizard_info = (f'Волшебник: {self.__name};\n'
                       f'Факультет: {self.__house};\n'
                       f'Уровень магической силы: {self.__magic_level};\n'
                       f'Заклинания: {spells};\n'
                       f'Статус: {self.__status}.')
        return wizard_info



class Spell:
    name = str
    difficulty_level = int
    type = str
    description = str

    def __init__(self, name: str, difficulty_level: int, type: str, description: str):
        if not isinstance(name, str):
            raise ValueError('Имя заклинания должно быть строкой')
        if not isinstance(difficulty_level, int):
            raise ValueError('Уровень сложности должно быть числом')
        if not 1 <= difficulty_level <= 10:
            raise ValueError('Уровень сложности должен быть от 1 до 10')
        if not isinstance(type, str):
            raise ValueError('Тип заклинания должен быть строкой')
        if not isinstance(description, str):
            raise ValueError('Описание должно быть строкой')

        self.__name = name
        self.__difficulty_level = difficulty_level
        self.__type = type
        self.__description = description


    def get_name(self):
        return self.__name

    def get_difficulty_level(self):
        return self.__difficulty_level

    def get_type(self):
        return self.__type

    def get_description(self):
        return self.__description

    def set_name(self, new_name: str):
        if not isinstance(new_name, str):
            raise ValueError('Имя заклинания должно быть строкой')
        self.__name = new_name

    def set_difficulty_level(self, new_value: int):
        if not isinstance(new_value, int):
            raise ValueError('Уровень сложности должно быть числом')
        if not 1 >= new_value <= 10:
            raise ValueError('Уровень сложности должен быть от 1 до 10')
        self.__difficulty_level = new_value

    def set_type(self, new_type):
        if not isinstance(new_type, str):
            raise ValueError('Тип заклинания должен быть строкой')
        self.__type = new_type

    def set_description(self, new_description):
        if not isinstance(new_description, str):
            raise ValueError('Описание должно быть строкой')


    def __str__(self):
        return (f'Название заклинания: {self.__name};\n'
                f'Уровень сложности: {self.__difficulty_level};\n'
                f'Тип: {self.__type};\n'
                f'Описание: {self.__description}.')


wizard_1 = Wizard('Harry', 'Griffindor', 10, 'В Хогвартсе')
wizard_2 = Wizard('Ron', 'Griffindor', 1, 'Выпущен')
spell_1 = Spell('Авада Кедавра', 10, 'Непростительное', 'Самое мощное')
spell_2 = Spell('Круцио', 10, 'Непростительное', 'Заклинание боли и ужаса')
spell_3 = Spell('Репаро', 1, 'Восстанавливающее', 'Восстановление сломанных предметов')

print(wizard_1)
print(wizard_2)

wizard_1.set_house('Слизерин')
print(wizard_1.get_house())

wizard_2.set_magic_level(15)
print(wizard_2.get_magic_level())

wizard_1.set_status('Выпущен')
print(wizard_1.get_status())

wizard_1.add_spell(Spell.get_name(spell_1))
wizard_1.add_spell(Spell.get_name(spell_2))
print(wizard_1)

wizard_1.remove_spell(Spell.get_name(spell_2))
print(wizard_1)


wizard_2.increase_magic_level(5)
print(wizard_2)

print(spell_1)