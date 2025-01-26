import math

class GeometryUtils:

    @staticmethod
    def square_circle(radius: float) -> float:
        return math.pi * radius ** 2

    @staticmethod
    def perimetr_circle(radius: float) -> float:
        return 2 * math.pi * radius

    @staticmethod
    def square_rectangle(side_a: float, side_b: float) -> float:
        return side_a * side_b

    @staticmethod
    def perimetr_rectangle(side_a: float, side_b: float) -> float:
        return 2 * (side_a + side_b)

    @staticmethod
    def square_triangle(side_a: float, side_b: float, side_c: float) -> float:
        pol_perimetr = (GeometryUtils.perimetr_triangle(side_a, side_b, side_c)) / 2
        return math.sqrt(pol_perimetr * (pol_perimetr - side_a) * (pol_perimetr - side_b) * (pol_perimetr - side_c))

    @staticmethod
    def perimetr_triangle(side_a: float, side_b: float, side_c: float) -> float:
        return side_a + side_b + side_c

