from __future__ import annotations


class Library:

    name: str
    address: str
    books: list[Book]
    users: list[User]



    def __init__(self, name: str, address: str, books=None, users=None):

        if not isinstance(name, str):
            raise ValueError('Имя библиотеки должно быть строкой\n')

        if not isinstance(address, str):
            raise ValueError('Адрес библиотеки должен быть строкой\n')

        self.__name = name
        self.__address = address
        self.__books = books or []
        self.__users = users or []



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



    def register_user(self, user: User):

        if not isinstance(user, User):
            raise ValueError('Пользователь должен быть объектом класса User\n')

        if user not in self.__users:
            self.__users.append(user)

        else:
            print('Данный пользователь уже зарегистрирован в библиотеке\n')
            return False


    def issue_book(self, book: Book, user: User):

        if not isinstance(book, Book):
            raise ValueError('Книга должна быть объектом класса Book\n')

        if not isinstance(user, User):
            raise ValueError('Пользователь должен быть объектом класса User\n')

        if book in self.__books and book.is_available is True:
            user.add_book(book)
            book.change_is_available()
            book.assign_user(user)

        else:
            print('Такой книги нет в библиотеке!\n')
            return False



    def return_book(self, book: Book, user: User):

        if not isinstance(book, Book):
            raise ValueError('Книга должна быть объектом класса Book\n')

        if not isinstance(user, User):
            raise ValueError('Пользователь должен быть объектом класса User\n')

        if book in user.get_books():
            user.remove_book(book)
            book.change_is_available()
            book.assign_user(user)

        else:
            print('Эту книгу данный пользователь не брал!\n')
            return False



    def get_books_status(self) -> str:

        if len(self.__books) == 0:
            books_info = 'Книг нет'

        else:
            books_info = ', '.join([book.get_name() for book in self.__books])

        return books_info


    def get_users_status(self) -> str:

        if len(self.__users) == 0:
            users = 'Пользователей нет'

        else:
            users = ', '.join([user.get_name() for user in self.__users])

        return users



    def __str__(self):

        if len(self.__books) == 0:
            books_info = 'Книг нет'

        else:
            books_info = ', '.join([book.get_name() for book in self.__books])


        if len(self.__users) == 0:
            users = 'Пользователей нет'

        else:
            users = ', '.join([user.get_name() for user in self.__users])


        return (f'Библиотека: {self.__name};\n'
                f'Адрес: {self.__address};\n'
                f'Книги в наличии: {books_info};\n'
                f'Пользователи: {users}.\n')


class Book:

    name: str
    author: str
    publication_year: int
    genre: str
    is_available: bool
    current_user: User or None



    def __init__(self, name:str, author: str, publication_year: int, genre: str, is_available: bool, current_user=None):
        self.__name = name
        self.__author = author
        self.__publication_year = publication_year
        self.__genre = genre
        self.__is_available = is_available
        self.__current_user = current_user or None



    def get_name(self):
        return self.__name



    def get_current_user(self):
        return self.__current_user



    def change_is_available(self):

        if self.__is_available is True:
            self.__is_available = False

        if self.__is_available is False:
            self.__is_available = True

            if self.__current_user is None:
                print('Книга не может быть выдана без указания пользователя')
                return False



    def assign_user(self, user: User):

        if not isinstance(user, User):
            raise TypeError('Пользователь должен быть объектом класса User\n')

        self.__current_user = user
        self.__is_available = False



    def change_genre(self, new_genre: str):

        if not isinstance(new_genre, str):
            raise TypeError('Жанр должен быть строкой\n')

        self.__genre = new_genre



    def __str__(self):

        status = 'В наличии'

        if self.__current_user is None:
            user_info = 'Пользователя нет'

        else:
            user_info = self.__current_user.get_name()


        if self.__is_available is False:
            status = 'Выдана'



        return (f'Название книги: {self.__name};\n'
                f'Автор: {self.__author};\n'
                f'Год публикации: {self.__publication_year};\n'
                f'Жанр: {self.__genre};\n'
                f'Статус: {status};\n'
                f'Текущий пользователь: {user_info}\n')




class User:

    name: str
    readers_ticket: int
    books: list[Book]



    def __init__(self, name: str, readers_ticket: int, books=None):


        self.__name = name
        self.__readers_ticket = readers_ticket
        self.__books = books or []



    def get_name(self):
        return self.__name

    def get_books(self):
        return self.__books



    def add_book(self, book: Book):

        if not isinstance(book, Book):
            raise TypeError('Книга должна быть объектом класса Book\n')

        if book in self.__books:
            print('Данная книга уже есть у пользователя!\n')
            return False

        self.__books.append(book)



    def remove_book(self, book: Book):

        if not isinstance(book, Book):
            raise TypeError('Книга должна быть объектом класса Book\n')

        if book not in self.__books:
            print('Такой книги нет у пользователя!\n')
            return False

        self.__books.remove(book)



    def check_books(self):
        if len(self.__books) == 0:
            books_info = 'Книг нет'

        else:
            for book in self.__books:
                books_info = ', '.join([book.get_name()])

        print(f'Список взятых книг у пользователя {self.__name}: {books_info}.\n')


    def __str__(self):

        if len(self.__books) == 0:
            books_info = 'Книг нет'

        else:
            for book in self.__books:
                books_info = ', '.join([book.get_name()])

        return (f'Имя пользователя: {self.__name};\n'
                f'Номер читательского билета: {self.__readers_ticket};\n'
                f'Список взятых книг: {books_info}.\n')


l_1 = Library('Пушкинская', 'г. Волгоград, ул. Пушкина')

u_1 = User("Alex", 123)
u_2 = User('Nick', 124)
print(u_1)

b_1 = Book('Война и мир', 'Л.В. Толстой', 1863, 'Роман-эпопея', False)
b_2 = Book('Мастер и Маргарита', 'М.А. Булгаков', 1966, 'Роман', False)

u_1.add_book(b_1)
print(u_1)

u_1.add_book(b_1)

u_1.remove_book(b_2)

u_1.check_books()

print(b_1)
b_1.change_is_available()
print(b_1)

b_1.assign_user(u_1)
print(b_1)

print(l_1)

l_1.add_book(b_1)
l_1.add_book(b_2)
print(l_1)

l_1.remove_book(b_2)
print(l_1)

l_1.register_user(u_1)
l_1.register_user(u_2)
print(l_1)