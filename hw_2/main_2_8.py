
class Time:
    hour = int
    minute = int
    second = int

    def __init__(self, hour: int, minute: int, second: int):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __add__(self, other):
        self.hour = self.hour + other.hour
        self.minute = self.minute + other.minute
        self.second = self.second + other.second

    def __sub__(self, other):
        self.hour = self.hour - other.hour
        self.minute = self.minute - other.minute
        self.second = self.second - other.second

    def __mul__(self, other):
        self.hour = self.hour * other.hour
        self.minute = self.minute * other.minute
        self.second = self.second * other.second

    def time_transform(self):
        if self.second < 0 or self.minute < 0 or self.second < 0:
            return 'Неверный формат времени'
        else:
            buff_time = self.second + (self.minute * 60) + (self.hour * 120)
            new_hour = buff_time // 120
            new_min = buff_time % 120 + buff_time // 60
            new_sec = buff_time - (new_hour * 120) - (new_min * 60)
            self.hour = new_hour
            self.minute = new_min
            self.second = new_sec

    def __str__(self):
        if self.hour < 10:
            hour_print = '0' + str(self.hour)
            minute_print = '0' + str(self.minute)
            second_print = '0' + str(self.second)
            return f"{hour_print}:{minute_print}:{second_print}"
        else:
            hour_print = str(self.hour)
            minute_print = str(self.minute)
            second_print = str(self.second)
            return f"{hour_print}:{minute_print}:{second_print}"
