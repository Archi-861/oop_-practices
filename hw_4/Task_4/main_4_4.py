from __future__ import annotations
import  random
import time



class Hogwarts:

    students: list[HogwartsStudent]
    spells: list[Spell]



    def __init__(self, students=None, spells=None):

        self.__students = students or []
        self.__spells = spells or []



    def get_students(self):
        return self.__students

    def get_spells(self):
        return self.__spells



    def enroll_student(self, student: HogwartsStudent):

        if not isinstance(student, HogwartsStudent):
            raise TypeError('Студент должен быть объектом класса HogwartsStudent')

        if student not in self.__students:
            self.__students.append(student)

        else:
            print('Данный студент уже зачислен в Хогвартс')
            return False



    def teach_spell(self, spell: Spell):

        if not isinstance(spell, Spell):
            raise TypeError('Заклинание должно быть объектом класса Spell')


        if spell not in self.__spells:
            self.__spells.append(spell)

        else:
            print('Данное заклинание уже знакомо в Хогвартсе')
            return False



    def simulate_duel(self, student1: HogwartsStudent, student2: HogwartsStudent):

        if not isinstance(student1, HogwartsStudent):
            raise TypeError('Студенты должны быть объектами класса HogwartsStudent')

        if not isinstance(student2, HogwartsStudent):
            raise TypeError('Студенты должны быть объектами класса HogwartsStudent')

        print(f'Внимание! Началась дуэль между {student1.get_name()} и {student2.get_name()}\n')

        assaulter, defender = random.choice([(student1, student2), (student2, student1)])

        while student1.get_mp() > 0 and student2.get_mp() > 0:

            assaulter.cast_spell(defender)
            time.sleep(0.8)

            if defender.get_mp() <= 0:
                break

            assaulter, defender = defender, assaulter

        if student1.get_mp() > 0:

            print(f'{student1.get_name()} побеждает!'
                  f'5 очков {student1.get_house()}у!\n')
        else:
            print(f'{student2.get_name()} побеждает!'
                  f'5 очков {student2.get_house()}у!\n')



    def __str__(self):

        if self.__students is None or len(self.__students) == 0:
            students = 'Нет выученных заклинаний'

        else:
            students = ', '.join([student.get_name() for student in self.__students])

        if self.__spells is None or len(self.__spells) == 0:
            spells = 'Нет выученных заклинаний'

        else:
            spells = ', '.join([spell.get_name() for spell in self.__spells])

        return (f'Студенты: {students};\n'
                f'Заклинания: {spells}.\n')



class HogwartsStudent:

    name: str
    house: str
    mp: int
    spells: list[Spell]



    def __init__(self, name: str, house: str, mp=100, spells=None):

        if not isinstance(name, str):
            raise TypeError('Имя должно быть строкой')

        if not isinstance(house, str):
            raise TypeError('Факультет должен быть строкой')

        self.__name = name
        self.__house = house
        self.__mp = mp
        self.__spells = spells or []



    def get_name(self):
        return self.__name

    def get_house(self):
        return self.__house

    def get_mp(self):
        return self.__mp

    def get_spells(self):
        return self.__spells



    def set_name(self, new_name: str):

        if not isinstance(new_name, str):
            raise TypeError('Имя должно быть строкой')

        self.__name = new_name

    def set_house(self, new_house: str):

        if not isinstance(new_house, str):
            raise TypeError('Факультет должен быть строкой')

        self.__house = new_house

    def set_mp(self, value: int):

        if not isinstance(value, int) or 0 > value > 100:
            raise TypeError('Значение маны должно быть строкой')

        self.__mp = value



    def learn_spell(self, spell: Spell, hogwarts: Hogwarts):

        if not isinstance(spell, Spell):
            raise TypeError('Заклинание должно быть объектом класса Spell')

        if not isinstance(hogwarts, Hogwarts):
            raise TypeError('Хогвартс должен быть объектом класса Хогвартс))')

        if spell not in hogwarts.get_spells():
            print('Черной магией не обучают в Хогвартсе!')

        if spell not in self.__spells:
            self.__spells.append(spell)

        else:
            print('Данный студент уже знает это заклинание')
            return False



    def cast_spell(self, target: HogwartsStudent):

        if not isinstance(target, HogwartsStudent):
            raise TypeError('Студент должен быть объектом класса HogwartsStudent')

        if len(self.__spells) == 0 or self.__spells is None:
            print(f'Студент {self.__name} не знает ни одного заклинания!')
            return False

        spell = random.choice(self.__spells)

        if self.__mp >= spell.get_mp_cost():
            print(f'Студент {self.__name} использует заклинание {spell.get_name()} на {target.get_name()}!\n')
            spell.cast(target)
        else:
            print(f'Oops.. У студента {self.__name} не хватает маны для заклинания {spell.get_name()}!\n')



    def __str__(self):

        if self.__spells is None or len(self.__spells) == 0:
            spells = 'Нет выученных заклинаний'

        else:
            spells = ', '.join([spell.get_name() for spell in self.__spells])


        return (f'Студент: {self.__name};\n'
                f'Факультет: {self.__house};\n'
                f'Магическая энергия: {self.__mp} ед.;\n'
                f'Заклинания: {spells}.\n')



class Spell:

    name: str
    description: str
    mp_cost: int



    def __init__(self, name: str, description: str, mp_cost: int):

        if not isinstance(name, str):
            raise TypeError('Имя заклинания должно быть строкой')

        if not isinstance(description, str):
            raise TypeError('Описание должно быть строкой')

        if not isinstance(mp_cost, int) and mp_cost < 0:
            raise TypeError('Стоимость магической энергии должно быть целое положительное число')

        self.__name = name
        self.__description = description
        self.__mp_cost = mp_cost



    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_mp_cost(self):
        return self.__mp_cost



    def set_name(self, new_name: str):

        if not isinstance(new_name, str):
            raise TypeError('Имя заклинания должно быть строкой')

        self.__name = new_name

    def set_description(self, new_description: str):

        if not isinstance(new_description, str):
            raise TypeError('Описание должно быть строкой')

        self.__description = new_description

    def set_mp_cost(self, value: int):

        if not isinstance(value, int) and value < 0:
            raise TypeError('Стоимость магической энергии должно быть целым положительным числом')

        self.__mp_cost = value



    def cast(self, target: HogwartsStudent):

        if not isinstance(target, HogwartsStudent):
            raise TypeError('Цель должна быть объектом класса HogwartsStudent')

        target.set_mp(target.get_mp() - self.__mp_cost)



    def __str__(self):
        return (f'Заклинание: {self.__name};\n'
                f'Описание: {self.__description};\n'
                f'Стоимость магической энергии: {self.__mp_cost}.\n')



sp_1 = Spell('Expelliarmus', 'Дизармирование противника', 15)
sp_2 = Spell('Stupefy', 'Оглушение противника', 15)
sp_3 = Spell('Avada Kedavra', 'Смертельное ранение (используется редко)', 30)
sp_4 = Spell('Protego', 'Защитный щит, отражающий заклинания',  10)
sp_5 = Spell('Petrificus Totalus', 'Полная парализация противника', 15)
sp_6 = Spell('Lumos', 'Создание источника света на конце волшебной палочки', 5)
sp_7 = Spell('Expecto Patronum', 'Призывание патронуса для защиты от дементоров', 30)


s_1 = HogwartsStudent('Гарри Поттер', 'Гриффиндор')
s_2 = HogwartsStudent('Драко Малфой', 'Слизерин')


hogwarts = Hogwarts()
hogwarts.enroll_student(s_1)
hogwarts.enroll_student(s_2)
hogwarts.teach_spell(sp_1)
hogwarts.teach_spell(sp_2)
hogwarts.teach_spell(sp_3)
hogwarts.teach_spell(sp_4)
hogwarts.teach_spell(sp_5)
hogwarts.teach_spell(sp_6)
hogwarts.teach_spell(sp_7)



s_1.learn_spell(sp_1, hogwarts)
s_1.learn_spell(sp_2, hogwarts)
s_1.learn_spell(sp_3, hogwarts)
s_1.learn_spell(sp_4, hogwarts)
s_1.learn_spell(sp_5, hogwarts)
s_1.learn_spell(sp_6, hogwarts)
s_1.learn_spell(sp_7, hogwarts)

s_2.learn_spell(sp_1, hogwarts)
s_2.learn_spell(sp_2, hogwarts)
s_2.learn_spell(sp_3, hogwarts)
s_2.learn_spell(sp_4, hogwarts)
s_2.learn_spell(sp_5, hogwarts)
s_2.learn_spell(sp_6, hogwarts)
s_2.learn_spell(sp_7, hogwarts)

hogwarts.simulate_duel(s_1, s_2)