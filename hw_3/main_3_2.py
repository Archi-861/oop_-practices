from __future__ import annotations

class Employee:
    name: str
    position: str
    department: str
    salary: float
    experience: int
    completed_projects: list

    def __init__(self, name: str, position: str, department: str, salary: int or float, experience: int, completed_projects=None):

        if not isinstance(name, str):
            raise ValueError('Имя должно быть строкой')

        if not isinstance(position, str):
            raise ValueError('Должность должна быть строкой')

        if not isinstance(department, str):
            raise ValueError('Название отдела должно быть строкой')

        if not isinstance(salary, int or float):
            raise ValueError('Зарплата должна быть числом')

        if salary < 0:
            raise ValueError('Зарплата не может быть отрицательной')

        if not isinstance(experience, int):
            raise ValueError('Стаж работы должен быть числом')

        if not experience >= 0:
            raise ValueError('Стаж работы не может быть отрицательным')

        self.__name = name
        self.__position = position
        self.__department = department
        self.__salary = salary
        self.__experience = experience
        self.__completed_projects = completed_projects or []


    def get_name(self):
        return self.__name

    def get_position(self):
        return self.__position

    def get_department(self):
        return self.__department

    def get_salary(self):
        return self.__salary

    def get_experience(self):
        return self.__experience

    def get_completed_projects(self):
        return self.__completed_projects

    def set_name(self, new_name: str):

        if not isinstance(new_name, str):
            raise ValueError('Имя сотрудника должно быть строкой')

        self.__name = new_name

    def set_position(self, new_position: str):

        if not isinstance(new_position, str):
            raise ValueError('Должность должна быть строкой')

        self.__position = new_position

    def set_department(self, new_department: str):

        if not isinstance(new_department, str):
            raise ValueError('Название отдела должно быть строкой')

        self.__department = new_department

    def set_salary(self, value: int or float):

        if not isinstance(value, int or float):

            raise ValueError('Зарплата должна быть числом')

        if value < 0:
            raise ValueError('Зарплата не может быть отрицательной')

        self.__salary = value

    def set_experience(self, new_experience: int):

        if not isinstance(new_experience, int):
            raise ValueError('Стаж работы должен быть числом')

        if new_experience < 0:
            raise ValueError('Стаж работы не может быть отрицательным')

        self.__experience = new_experience

    def set_completed_projects(self, value):
        self.__completed_projects = value

    def __str__(self):

        if len(self.__completed_projects) == 0:
            completed_projects = 'Проектов нет'

        else:
            completed_projects = self.__completed_projects
            completed_projects = ', '.join(completed_projects)

        return (f'Сотрудник: {self.__name};\n'
                f'Должность: {self.__position};\n'
                f'Отдел: {self.__department};\n'
                f'Зарплата: {self.__salary};\n'
                f'Стаж работы (в годах): {self.__experience};\n'
                f'Выполненные проекты: {completed_projects}.')


    def add_completed_project(self, completed_project):
        self.__completed_projects.append(completed_project)

    def remove_completed_project(self, completed_project):

        if completed_project in self.__completed_projects:
            self.__completed_projects.remove(completed_project)

        else:
            return False


    def increase_salary(self, value: int or float):

        if not isinstance(value, int or float):
            raise ValueError('Увеличение зарплаты должно быть числом')


        if value < 0:
            raise ValueError('Увеличение зарплаты не может быть отрицательным')

        self.__salary += value



class CompletedProject:

    name = str

    def __init__(self, name: str):

        if not isinstance(name, str):
            raise ValueError('Имя выполненного проекта должно быть строкой')

        self.__name = name


    def get_name(self):
        return self.__name

    def set_name(self, new_name: str):

        if not isinstance(new_name, str):
            raise ValueError('Имя проекта должно быть строкой')

        self.__name = new_name




e_1 = Employee('Alex', 'Seller', 'Sales department', 45000, 1)
c_p_1 = CompletedProject('School')
print(e_1)

e_1.add_completed_project(CompletedProject.get_name(c_p_1))
print(e_1)

e_1.increase_salary(15000)
print(e_1)