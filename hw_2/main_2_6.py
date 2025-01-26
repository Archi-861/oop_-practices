
class Fraction:
    numerator = int
    denominator = int

    def __init__(self, numerator: int, denominator: int):
        if self.denominator == 0:
            raise ValueError('Знаменатель не может быть равен нулю!')
        self.numerator = numerator
        self.denominator = denominator

    @staticmethod
    def fraction_zero_check(check_denominator: int) -> bool:
        if check_denominator == 0:
            return False
        else:
            return True

    def __str__(self):
        if self.denominator == self.numerator:
            res = f'{self.numerator}'
        else:
            res = f'{self.numerator}/{self.denominator}'
        return res

    def __add__(self, other):
        if Fraction.fraction_zero_check(self.denominator) == True and Fraction.fraction_zero_check(other.denominator) == True:
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        else:
            print('Знаменатель равен нулю!')

    def __sub__(self, other):
        if Fraction.fraction_zero_check(self.denominator) == True and Fraction.fraction_zero_check(other.denominator) == True:
            new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        else:
            print('Знаменатель равен нулю!')

    def __mul__(self, other):
        if Fraction.fraction_zero_check(self.denominator) == True and Fraction.fraction_zero_check(other.denominator) == True:
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        else:
            print('Знаменатель равен нулю!')


fraction_1 = Fraction(1,2)
fraction_2 = Fraction(1,3)
fraction_3 = Fraction(1,1)
fraction_4 = Fraction(5,0)

print(fraction_1)
