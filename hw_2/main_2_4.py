from array import array


class ArrayUtils:

    @staticmethod
    def sum(array: list[int]) -> int:
        """
        Функция по суммированию элементов массива.
        :param array: list[int]
        :return: int
        """
        summ = 0
        for i in range(0, len(array)):
            summ += array[i]
        return summ

    @staticmethod
    def multi(array: list[int]) -> int:
        """
        Функция по умножению элементов массива.
        :param array: list[int]
        :return: int
        """
        res = 1
        for i in range(0, len(array)):
            res *= array[i]
        return res

    @staticmethod
    def inverse(array: list[int]) -> list:
        """
        Функция инверсии массива.
        :param array: list[int]
        :return: int
        """
        new_array = array[::-1]
        return new_array

    @staticmethod
    def max(array: list[int]) -> int:
        """
        Функция по поиску максимального элемента массива.
        :param array: list[int]
        :return: int
        """
        max_elem = array[0]
        for i in range(1, len(array)):
            if max_elem < array[i]:
                max_elem = array[i]
        return max_elem

    @staticmethod
    def min(array: list[int]) -> int:
        """
        Функция по поиску минимального элемента массива.
        :param array: list[int]
        :return: int
        """
        min_elem = array[0]
        for i in range(1, len(array)):
            if min_elem < array[i]:
                min_elem = array[i]
        return min_elem


print('Сумма списка равна:', ArrayUtils.sum([1,2]))
print('Вычитание списка равно:', ArrayUtils.multi([1,2]))
print('Инверсия списка:', ArrayUtils.inverse([1,2]))
print('Максимальный элемент списка равен:', ArrayUtils.max([1,2]))
print('Минимальный элемент списка равен:', ArrayUtils.min([1,2]))