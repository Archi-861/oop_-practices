# Задача №1

class Animal:

    name: str
    age: int
    type: str

    def __init__(self, name: str, age: int, type: str):
        self.name = name
        self.age = age
        self.type = type

    def make_sound(self):
        print("ARR")

    def info_animal(self):
        print(self.name, self.age, self.type)


# Задача №2

class Book:

    name: str
    author = str
    page_count = int

    def __init__(self, name: str, author: str, page_count: int):
        self.name = name
        self.author = author
        self.page = page_count

    def open_page(self, page: int):
        if page <= self.page_count:
            print('Вы открыли страницу', page)
        else:
            print('В данной книге нет такой страницы')

    def info_book(self):
        print(self.name, self.author, self.page_count)


# Задача №3

class PassengerPlane:

    manufacturer = str
    model = str
    capacity = int
    current_height = float
    current_speed = float


    def __init__(self, manufacturer: str, model: str, capacity: int, current_height: float, current_speed: float):
        self.manufacturer = manufacturer
        self.model = model
        self.capacity = capacity
        self.current_height = current_height
        self.current_speed = current_speed

    def info_plane(self):
        print(self.manufacturer, self.model, self.capacity, self.current_height, self.current_speed)


    def takeoff_plane(self):
        print('Самолет взлетел!')


    def landing_plane(self):
        print('Самолет приземлился')


    def height_change_plane(self, height: float):
        self.current_height = height


# Задача №4

class MusicAlbum:

    artist = str
    album = str
    style = str
    track_list = list

    def __init__(self, artist: str, album: str, style: str, track_list: list):
        self.artist = artist
        self.album = album
        self.style = style
        self.track_list = track_list

    def info_music_album(self):
        print(self.artist, self.album, self.style, self.track_list)

    def add_track(self, track: str):
        self.track_list.append(track)


    def del_track(self, track: str):
        if track in self.track_list:
            self.track_list.remove(track)
        else:
            print('Данного трека нет в списке треков')


    def play_track(self, track: str):
        if track in self.track_list:
            print('Сейчас играет ', track)
        else:
            print('Данного трека нет в списке треков')

