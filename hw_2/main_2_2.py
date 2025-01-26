
class Tourist:
    name = str

    def __init__(self, name: str):
        self.__name = name

    def get_name(self):
        return self.__name

class TouristSpot:
    name = str
    country = str
    type = str

    def __init__(self, name: str, country: str, type: str):
        self.__name = name
        self.__country = country
        self.__type = type

    def visit_place(self, tourist: Tourist):
        print(f'Турист {tourist.get_name()} посетил {self.__name}')

    def __str__(self):
        return f'Туристическая достопримечательность под названием {self.__name} располагается в {self.__country} и является {self.__type} достопримечательностью'


tourist_1 = Tourist('Джон')
place_1 = TouristSpot('Мамаев Курган', 'Россия', 'историческая')

place_1.visit_place(tourist_1)