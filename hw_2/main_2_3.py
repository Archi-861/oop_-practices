
class ModelWindow:
    title = str
    coord_x = int
    coord_y = int
    horizon_size = int
    vertical_size = int
    color = str
    is_visible = bool
    has_frame = bool

    def __init__(self, title: str, coord_x: int, coord_y: int, horizon_size: int, vertical_size: int, color: str, is_visible: bool, has_frame: bool):
        self.__title = title
        self.__coord_x = coord_x
        self.__coord_y = coord_y
        self.__horizon_size = horizon_size
        self.__vertical_size = vertical_size
        self.__color = color
        self.__is_visible = is_visible
        self.__has_frame = has_frame

    def __str__(self):
        return (f'Окно: {self.__title}, '
                f'координаты верхнего левого угла: координата x: {self.__coord_x}, координата y: {self.coord_y}'
                f'размер по горизонтали: {self.__horizon_size}, '
                f'размер по вертикали: {self.__vertical_size},  '
                f'цвет окна: {self.__color},'
                f'видимость: {self.__is_visible},'
                f'рамка(состояние): {self.__has_frame}')

    def move_window(self, new_coord_x: int, new_coord_y: int):
        if 1960 > new_coord_x > 0 and 1080 > new_coord_y > 0:
            self.__coord_x = new_coord_x
            self.__coord_y = new_coord_y

    def change_window_vertical_size(self, new_value: int):
        pass

    def change_window_color(self, new_color: int):
        self.__color = new_color
        print(f'Цвет окна изменен на {self.__color}')

    def window_change_frame(self, new_frame: bool):
        self.__has_frame = new_frame

    def window_change_visible(self, new_visible):
        self.__is_visible = new_visible
