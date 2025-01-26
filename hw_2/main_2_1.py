import datetime

class Data:
    day = int
    month = int
    year = int

    def __init__(self, day: int, month: int, year: int):
        self.date = datetime.date(year, month, day)

    def print_date(self):
        return self.date.strftime('%d-%m-%Y')

class Time:
    hour = int
    minute = int
    second = int

    def __init__(self, hour: int, minute: int, second: int):
        self.time = datetime.time(hour, minute, second)

    def print_time(self):
        return self.time.strftime('%H:%M:%S')

class Patient:
    last_name = str
    first_name = str
    patronymic = str
    age = int
    disease = str

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int, disease: str):
        self.__last_name = last_name
        self.__first_name = first_name
        self.__patronymic = patronymic
        self.__age = age
        self.__disease = disease


    def make_appointment(self, time: Time, date: Data):
        print(f'Пациент {self.__last_name} {self.__first_name} {self.__patronymic} записан {Data.print_date(date)}г. в {Time.print_time(time)}.')


    def __str__(self):
        return f'Пациент - {self.__first_name} {self.__patronymic} {self.__last_name}, возраст - {self.__age} лет, диагноз - {self.__disease}.'


patient_1 = Patient('Джонов', 'Джон', 'Джонович', 100, 'Маразм')
time_1 = Time(10,00,00)
date_1 = Data(25,1,2025)

patient_1.make_appointment(time_1, date_1)

