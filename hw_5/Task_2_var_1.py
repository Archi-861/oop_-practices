from abc import ABC, abstractmethod


class AFarmAnimal(ABC):

    id: int
    age: int
    race: str
    sex: str
    type: str

    def __init__(self, id: int, age: int, race: str, sex: str, type: str):

        if not isinstance(id, int):
            raise TypeError('ID должен быть целым числом')

        if not isinstance(age, int) and age <= 0:
            raise TypeError('Возраст должен быть целым положительным числом')

        if not isinstance(race, str):
            raise TypeError('Порода должна быть строкой')

        if not isinstance(sex, str):
            raise TypeError('Пол должен быть строкой')

        if not isinstance(type, str):
            raise TypeError('Тип должен быть строкой')


        self._id = id
        self._age = age
        self._race = race
        self._sex = sex
        self._type = type


    @abstractmethod
    def eat(self):
        pass



class Cow(AFarmAnimal):

    weight: int

    def __init__(self, id, age, race, sex, type, weight: int):

        super().__init__(id, age, race, sex,type)
        self.__weight = weight



    def eat(self) -> None:
        print('Корова ест')



    def get_milk(self, value: float) -> None:
        print(f'Корова {self._id} дала {value} литров молока')



class Pig(AFarmAnimal):

    weight: int

    def __init__(self, id, age, race, sex, type, weight: int):

        super().__init__(id, age, race, sex, type)
        self.__weight = weight



    def eat(self) -> None:
        print('Свинья ест')



    def multiply(self, value: int) -> None:
        print(f'Свинья {self._id} дала потомство из {value} поросят')



class Chicken(AFarmAnimal):

    productivity: int

    def __init__(self, id, age, race, sex, type, productivity: int):

        super().__init__(id, age, race, sex, type)
        self.__productivity = productivity



    def eat(self) -> None:
        print('Курица ест')



    def lay_egg(self, value: int) -> None:
        print(f'Курица {self._id} снесла {value} яиц')



class Sheep(AFarmAnimal):

    weight: int
    wool_quality: int

    def __init__(self, id, age, race, sex, type, weight: int, wool_quality: int):

        super().__init__(id, age, race, sex, type)
        self.__weight = weight
        self.__wool_quality = wool_quality



    def eat(self) -> None:
        print('Овца кушает')



    def shave(self, value: int) -> None:
        print(f'Овца {self._id} принесла {value} кг шерсти')




class AFarmEquipment(ABC):

    brand: str
    model: str
    mileage: int
    power: int
    status: str

    def __init__(self, brand: str, model: str, mileage: int, power: int, status: str):

        self._brand = brand
        self._model = model
        self._mileage = mileage
        self._power = power
        self._status = status



    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass



class Tractor(AFarmEquipment):

    wheel_size: int
    load_capacity: int

    def __init__(self, brand, model, mileage, power, status, wheel_size: int, load_capacity: int):

        super().__init__(brand, model, mileage, power, status)
        self.__wheel_size = wheel_size
        self.__load_capacity = load_capacity



    def start_engine(self) -> None:
        print(f'Трактор {self._model} завел двигатель')

    def stop_engine(self):
        print(f'Трактор {self._model} заглушил двигатель')



    def plow(self):
        print(f'Трактор {self._model} вспахивает поле')



class Harvest(AFarmEquipment):

    header_size: int
    seed_capacity: int

    def __init__(self, brand, model, mileage, power, status, header_size: int, seed_capacity: int):

        super().__init__(brand, model, mileage, power, status)
        self.__header_size = header_size
        self.__seed_capacity = seed_capacity



    def start_engine(self):
        print(f'Комбайн {self._model} завел двигатель')

    def stop_engine(self):
        print(f'Комбайн {self._model} заглушил двигатель')



    def harvest(self):
        print(f'Комбайн {self._model} собирает урожай')



cow = Cow(1, 2, 'Холмогорская', 'Жен.', 'Молочная', 800)
cow.eat()
cow.get_milk(5)

harvest = Harvest('Беларус', 'К1', 2000, 150, 'Удовлетворительное', 29, 9000)
harvest.start_engine()
harvest.stop_engine()
harvest.harvest()

tractor = Tractor('Беларус', 'Т-600', 200, 260, 'Хорошее', 35, 500)
tractor.start_engine()
tractor.stop_engine()
tractor.plow()

sheep = Sheep(520, 2, 'Романовская', 'Жен.', 'Шубы', 85, 5)
sheep.eat()
sheep.shave(10)

chicken = Chicken(601, 1, 'Леггорн', 'Жен.', 'Яичная', 3)
chicken.eat()
chicken.lay_egg(5)

pig = Pig(706, 4, 'Ландрас', 'Жен.', 'Мясная', 450)
pig.eat()
pig.multiply(10)