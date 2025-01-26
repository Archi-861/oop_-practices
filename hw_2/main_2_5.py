import math

class Vector:
    coord_x = float
    coord_y = float
    coord_z = float

    def __init__(self, coord_x: float, coord_y: float, coord_z: float):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.coord_z = coord_z

    def __str__(self):
        return (f'Координата X: {self.coord_x};'
                f'Координата Y: {self.coord_y};'
                f'Координата Z: {self.coord_z}.')

    def __add__(self, other):
        return self.coord_x + other.coord_x, self.coord_y + other.coord_y, self.coord_z + other.coord_z

    def __sub__(self, other):
        return self.coord_x - other.coord_x, self.coord_y - other.coord_y, self.coord_z - other.coord_z

    def __mul__(self, other):
        return self.coord_x * other.coord_x + self.coord_y * other.coord_y + self.coord_z * other.coord_z

    def scalar_mul(self, other):
        new_coord_x = self.coord_z * other.coord_y - self.coord_y * other.coord_z
        new_coord_y = self.coord_x * other.coord_z - self.coord_z * other.coord_x
        new_coord_z = self.coord_y * other.coord_x - self.coord_x * other.coord_y
        return new_coord_x, new_coord_y, new_coord_z

    def norma(self):
        norma = math.sqrt(self.coord_x ** 2 + self.coord_y ** 2 + self.coord_z ** 2)
        return norma

vector_1 = Vector(1.5,1.5,1.5)
vector_2 = Vector(1.5, 1,1.5)

print('Сложение двух векторов равно: ', Vector.__add__(vector_1, vector_2))
print('Вычитание двух векторов равно: ', Vector.__sub__(vector_1,vector_2))
print('Умножение двух векторов равно: ', Vector.__mul__(vector_1, vector_2))
print('Скалярное умножение двух векторов равно: ', Vector.scalar_mul(vector_1,vector_2))
print('Длина вектора равна: ', Vector.norma(vector_1))