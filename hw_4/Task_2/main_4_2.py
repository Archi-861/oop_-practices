from __future__ import annotations


class Library:

    name: str
    address: str
    books: list[Book]
    employee: list[Employee]



    def __init__(self, name: str, address: str, books=None, employee=None):

        if not isinstance(name, str):
            raise ValueError('Имя библиотеки должно быть строкой\n')

        if not isinstance(address, str):
            raise ValueError('Адрес библиотеки должен быть строкой\n')

        self.__name = name
        self.__address = address
        self.__books = books or []
        self.__employee = employee or []



    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_books(self):
        return self.__books

    def get_employee(self):
        return self.__employee



    def set_address(self, new_address: str):

        if not isinstance(new_address, str):
            raise TypeError('Адрес должен быть строкой')

        self.__address = new_address



    def add_book(self, book: Book):

        if not isinstance(book, Book):
            raise ValueError('Книга должна быть объектом класса Book\n')

        if book not in self.__books:
            self.__books.append(book)

        else:
            print('Данная книга уже есть в библиотеке\n')
            return False



    def remove_book(self, book: Book):

        if not isinstance(book, Book):
            raise ValueError('Книга должна быть объектом класса Book\n')

        if book in self.__books:
            self.__books.remove(book)

        else:
            print('Данной книги нет в библиотеке\n')
            return False



    def add_employee(self, employee: Employee):

        if not isinstance(employee, Employee):
            raise ValueError('Сотрудник должен быть объектом класса Employee\n')

        if employee not in self.__employee:
            self.__employee.append(employee)

        else:
            print('Данный сотрудник уже зарегистрирован в библиотеке\n')
            return False



    def remove_employee(self, employee: Employee):

        if not isinstance(employee, Employee):
            raise ValueError('Сотрудник должен быть объектом класса Employee\n')

        if employee in self.__employee:
            self.__employee.remove(employee)

        else:
            print('Данного сотрудника нет в библиотеке\n')
            return False



    def __str__(self):

        if self.__books is None or len(self.__books) == 0:
            books_info = 'Книг нет'

        else:
            books_info = ', '.join([book.get_name() for book in self.__books])


        if self.__employee is None or len(self.__employee) == 0:
            employers = 'Сотрудников нет'

        else:
            employers = ', '.join([employee.get_name() for employee in self.__employee])


        return (f'Библиотека: {self.__name};\n'
                f'Адрес: {self.__address};\n'
                f'Книги в наличии: {books_info};\n'
                f'Сотрудники: {employers}.\n')



class Book:

    id: int
    name: str
    author: str
    publication_year: int
    genre: list[Genre]



    def __init__(self, id: int, name: str, author: str, publication_year: int, genre=None):
        self.__id = id
        self.__name = name
        self.__author = author
        self.__publication_year = publication_year
        self.__genre = genre or []



        if not isinstance(id, int) and id <= 0:
            raise TypeError('ID должен быть целым положительным числом')

        if not isinstance(name, str):
            raise TypeError('Имя должно быть строкой')

        if not isinstance(author, str):
            raise TypeError('Автор должен быть строкой')

        if not isinstance(publication_year, int) and publication_year <= 0:
            raise TypeError('Год публикации должен быть целым числом')



    def get_name(self):
        return self.__name

    def get_author(self):
        return self.__author

    def get_publication_year(self):
        return self.__publication_year

    def get_id(self):
        return self.__id

    def get_genres(self):
        return self.__genre



    def set_publication_year(self, year: int):

        if not isinstance(year, int) and year <= 0:
            raise TypeError('Год должен быть целым положительным числом')

        self.__publication_year = year



    def add_genre(self, genre: Genre):

        if not isinstance(genre, Genre):
            raise TypeError('Жанр должен быть объектом класса Genre')

        if genre not in self.__genre:
            self.__genre.append(genre)

        else:
            print('Данный жанр уже добавлен к этой книге')
            return False


    def remove_genre(self, genre: Genre):

        if not isinstance(genre, Genre):
            raise TypeError('Жанр должен быть объектом класса Genre')

        if genre in self.__genre:
            self.__genre.remove(genre)

        else:
            print('Такого жанра нет у данной книги')
            return False



    def __str__(self):

        if self.__genre is None or len(self.__genre) == 0:
            genres = 'Жанр не определен'

        else:
            genres = ', '.join([genre.get_name() for genre in self.__genre])

        return (f'ID: {self.__id};\n'
                f'Название книги: {self.__name};\n'
                f'Автор: {self.__author};\n'
                f'Год публикации: {self.__publication_year};\n'
                f'Жанр: {genres};\n')



class Employee:

    id: int
    name: str
    position: str
    contact_info: list[ContactInfo]



    def __init__(self, id: int, name: str, position: str, contact_info=None):

        if not isinstance(id, int) and id <= 0:
            raise TypeError('ID должен быть целым положительным числом')

        if not isinstance(name, str):
            raise TypeError('Имя должно быть строкой')

        if not isinstance(position, str):
            raise TypeError('Должность должна быть строкой')

        self.__id = id
        self.__name = name
        self.__position = position
        self.__contact_info = contact_info or []



    def get_name(self):
        return self.__name

    def get_position(self):
        return self.__position

    def get_id(self):
        return self.__id

    def get_contact_info(self):
        return self.__contact_info



    def set_position(self, new_position: str):

        if not isinstance(new_position, str):
            raise TypeError('Должность должна быть строкой')

        self.__position = new_position



    def add_contact_info(self, contact_info: ContactInfo):

        if not isinstance(contact_info, ContactInfo):
            raise TypeError('Контактная информация должна быть объектом класса ContactInfo')

        if contact_info not in self.__contact_info:
            self.__contact_info.append(contact_info)

        else:
            print('Такая контактная информация уже добавлена сотруднику')
            return False



    def remove_contact_info(self, contact_info: ContactInfo):

        if not isinstance(contact_info, ContactInfo):
            raise TypeError('Контактная информация должна быть объектом класса ContactInfo')

        if contact_info in self.__contact_info:
            self.__contact_info.remove(contact_info)

        else:
            print('Такой информации нет у сотрудника')
            return False



    def __str__(self):

        if self.__contact_info is None or len(self.__contact_info) == 0:
            contact_info = 'Нет данных'

        else:
            contact_info = ', '.join(str(info) for info in self.__contact_info)

        return (f'ID: {self.__id};\n'
                f'Имя сотрудника: {self.__name};\n'
                f'Должность: {self.__position};\n'
                f'Контактная информация: {contact_info}.\n')



class Genre:

    name: str
    description: str



    def __init__(self, name: str, description: str):

        if not isinstance(name, str):
            raise TypeError('Имя должно быть строкой')

        if not isinstance(description, str):
            raise TypeError('Описание должно быть строкой')

        self.__name = name
        self.__description = description



    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description



    def set_name(self, new_name: str):

        if  not isinstance(new_name, str):
            raise TypeError('Имя должно быть строкой')

        self.__name = new_name

    def set_description(self, new_description: str):

        if not isinstance(new_description, str):
            raise TypeError('Описание должно быть строкой')

        self.__description = new_description



    def __str__(self):
        return (f'Название жанра: {self.__name};\n'
                f'Описание: {self.__description}.\n')



class ContactInfo:

    type: str
    value: str



    def __init__(self, type: str, value: str):

        if not isinstance(type, str):
            raise TypeError('Тип контактной информации должен быть строкой')

        if not isinstance(value, str):
            raise TypeError('Значение контактной информации должно быть строкой')

        self.__type = type
        self.__value = value



    def get_type(self):
        return self.__type

    def get_value(self):
        return self.__value



    def set_type(self, new_type: str):

        if not isinstance(new_type, str):
            raise TypeError('Тип контактной информации должен быть строкой')

        self.__type = new_type

    def set_value(self, new_value: str):

        if not isinstance(new_value, str):
            raise TypeError('Значение контактной информации должно быть строкой')

        self.__value = new_value



    def get_all_contact_info(self):
        return self.__type, self.__value



    def __str__(self):
        return (f'{self.__type};\n'
                f'Значение: {self.__value}.\n')



contact_1 = ContactInfo('Телефон', '1234')
print(contact_1)

genre_1 = Genre('Роман', 'Это роман')
genre_2 = Genre('Эпопея', 'Это эпопея')
print(genre_1)

empl_1 = Employee(1, 'Алекс', 'Директор')
print(empl_1)

empl_1.add_contact_info(contact_1)
print(empl_1)

