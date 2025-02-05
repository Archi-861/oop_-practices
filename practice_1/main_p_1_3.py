from __future__ import annotations


class Potion:

    name: str
    ingredients: list[Ingredients]
    difficulty: int
    effect: str
    status: bool

    def __init__(self, name: str, difficulty: int, effect: str, status: bool, ingredients=None):
        if not isinstance(name, str):
            raise ValueError('Название зелья должно быть строкой')

        if not 0 < difficulty < 11:
            raise ValueError('Сложность приготовления должна быть числом от 1 до 10')

        if not isinstance(difficulty, int):
            raise ValueError('Сложность приготовления должна быть целым числом')

        if not isinstance(effect, str):
            raise ValueError('Эффект зелья должен быть строкой')

        if not isinstance(status, bool):
            raise ValueError('Состояние должно быть булевым значением True/False')

        self.__name = name
        self.__difficulty = difficulty
        self.__effect = effect
        self.__status = status
        self.__ingredients = ingredients or []


    def add_ingredient(self, ingredient: Ingredients):

        if not isinstance(ingredient, Ingredients):
            raise ValueError('Ингредиент должен быть объектом класса Ингредиенты')

        self.__ingredients.append(ingredient)

    def remove_ingredient(self, ingredient: Ingredients):

        if not isinstance(ingredient, Ingredients):
            raise ValueError('Ингредиент должен быть объектом класса Ингредиенты')

        else:
            self.__ingredients.remove(ingredient)


    def change_difficulty(self, value: int):

        if 0 < value < 11:
            raise ValueError('Сложность приготовления должна быть числом от 1 до 10')

        if not isinstance(value, int):
            raise ValueError('Сложность приготовления должна быть целым числом')

        self.__difficulty = value


    def change_effect(self, new_effect: str):

        if not isinstance(new_effect, str):
            raise ValueError('Эффект должен быть строкой')

        self.__effect = new_effect


    def check_status(self):

        status = 'Приготовлено'

        if self.__status is False:
            status = 'Не приготовлено'

        print(status)


    def check_ingredients(self):

        ingredients = self.__ingredients
        ingredients = ', '.join(ingredients)

        if len(self.__ingredients) == 0:
            ingredients = 'Ингредиентов нет'

        print(ingredients)

    def __str__(self):

        ingredients = self.__ingredients
        ingredients = ', '.join(ingredients)

        if len(self.__ingredients) == 0:
            ingredients = 'Ингредиентов нет'

        status = 'Приготовлено'

        if self.__status is False:
            status = 'Не приготовлено'

        return (f'Зелье: {self.__name};\n'
                f'Ингредиенты: {ingredients};\n'
                f'Эффект: {self.__effect};\n'
                f'Сложность: {self.__difficulty};\n'
                f'Статус приготовления: {status}.\n')


class Ingredients:

    name: str

    def __init__(self, name: str):

        if not isinstance(name, str):
            raise ValueError('Ингредиент должен быть строкой')

        self.__name = name


    def get_name(self):
        return self.__name


in_1 = Ingredients('Философский камень')
p_1 = Potion('Эликсир жизни', 10, 'Бессмертие', True)
print(p_1)