from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import date


class ABankEmployee(ABC):

    id: int
    name: str
    age: int
    sex: str
    salary: float
    duties: str
    is_working: bool

    def __init__(self, id: int, name: str, age: int, sex: str, salary: float, duties: str, is_working: bool):

        self._id = id
        self._name = name
        self._age = age
        self._sex = sex
        self._salary = salary
        self._duties = duties
        self._is_working = is_working

    @abstractmethod
    def get_job(self):
        pass

    @abstractmethod
    def dismiss(self):
        pass



class Manager(ABankEmployee):

    department: str

    def __init__(self, id, name, age, sex, salary, duties, is_working, department: str):

        super().__init__(id, name, age, sex, salary, duties, is_working)
        self.__department = department



    def get_name(self):
        return self._name



    def get_job(self):
        print(f'Сотрудник {self._name} был принят на работу')



    def dismiss(self):

        self._is_working = False

        print(f'Сотрудник {self._name} уволен')



    def take_vacation(self):
        print(f'Сотрудник {self._name} решил взять отпуск')



    def __str__(self):

        status = 'Работает'
        if self._is_working is False:
            status = 'Уволен'

        return (f'Сотрудник: {self._name};\n'
                f'Личный номер: {self._id};\n'
                f'Возраст: {self._age};\n'
                f'Пол: {self._sex};\n'
                f'Зарплата: {self._salary};\n'
                f'Обязанности: {self._duties};\n'
                f'Статус: {status};\n'
                f'Отдел: {self.__department}\n')



class Cashier(ABankEmployee):

    category: str

    def __init__(self, id, name, age, sex, salary, duties, is_working, category: str):

        super().__init__(id, name, age, sex, salary, duties, is_working)
        self.__category = category



    def get_job(self):
        print(f'Сотрудник {self._name} был принят на работу')



    def dismiss(self):
        self._is_working = False

        print(f'Сотрудник {self._name} уволен')



    def make_encashment(self):
        print(f'Сотрудник {self._name} провел инкассацию')



    def __str__(self):

        status = 'Работает'
        if self._is_working is False:
            status = 'Уволен'

        return (f'Сотрудник: {self._name};\n'
                f'Личный номер: {self._id};\n'
                f'Возраст: {self._age};\n'
                f'Пол: {self._sex};\n'
                f'Зарплата: {self._salary};\n'
                f'Обязанности: {self._duties};\n'
                f'Статус: {status};\n'
                f'Категория: {self.__category}\n')



class AAccount(ABC):

    number: int
    currency: str
    balance: float
    lord: BankClient
    opening_date: int
    closing_date: int
    status: str

    def __init__(self, number: int, currency: str, balance: float, lord: BankClient, opening_date: date, status: str, closing_date: date = None):

        self._number = number
        self._currency = currency
        self._balance = balance
        self._lord = lord
        self._opening_date = opening_date
        self._closing_date = closing_date
        self._status = status


    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass



class CreditAccount(AAccount):

    limit: int
    rate: float
    free_period: int

    def __init__(self, number, currency, balance, lord, opening_date, status, limit: int, rate: float, free_period: int, closing_date= None):

        super().__init__(number, currency, balance, lord, opening_date, status, closing_date)
        self.__limit = limit
        self.__rate = rate
        self.__free_period = free_period



    def open(self):
        self._status = 'Открыт'



    def close(self):
        self._status = 'Закрыт'
        self._closing_date = date.today()



    def __str__(self):

        closing_date = self._closing_date or "-"

        return (f'Кредитный счет:\n'
                f'Номер счета: {self._number};\n'
                f'Валюта счета: {self._currency};\n'
                f'Баланс: {self._balance};\n'
                f'Владелец: {self._lord.get_name()};\n'
                f'Дата открытия: {self._opening_date};\n'
                f'Дата закрытия: {closing_date}.\n')

class CreditCard:

    number: int
    validity_period_year: int
    validity_period_month: int
    cashback_category: str
    lord: BankClient
    сredit_account: CreditAccount

    def __init__(self, number: int, validity_period_year: int, validity_period_month: int, cashback_category: str, credit_account: CreditAccount = None, lord= None):

        self.__number = number
        self.__validity_period_year = validity_period_year
        self.__validity_period_moth = validity_period_month
        self.__cashback_category = cashback_category
        self.__lord = lord
        self.__credit_account = credit_account



    def assign_credit_account(self, credit_account: CreditAccount):
        self.__credit_account = credit_account




    def __str__(self):


        lord = 'Карта не выдана'
        if self.__lord is not None:
            lord = self.__lord

        credit_account = 'Карта не активна'



        card_info = (f'Кредитная карта:\n'
                f'Номер карты: {self.__number};\n'
                f'Номер кредитного счета: {credit_account};\n'
                f'Дата окончания действия: {self.__validity_period_moth}/{self.__validity_period_year};\n'
                f'Категории cashback: {self.__cashback_category};\n'
                f'Владелец: {lord}.\n')

        return card_info



class DebitAccount(AAccount):
    pass



class BankClient:

    id: int
    name: str
    status: str
    credit_rating: float
    credit_account: list[CreditAccount]
    debit_account: list[DebitAccount]
    credit_card: list[CreditCard]


    def __init__(self, id: int, name: str, status: str, credit_rating: float, credit_account=None, debit_account=None, credit_card=None):

        self.__id = id
        self.__name = name
        self.__status = status
        self.__credit_rating = credit_rating
        self.__credit_account = credit_account or []
        self.__debit_account = debit_account or []
        self.__credit_card = credit_card or []



    def get_name(self):
        return self.__name



    def add_credit_account(self, credit_account: CreditAccount):
        self.__credit_account.append(credit_account)



    def add_credit_card(self, credit_card: CreditCard):
        self.__credit_card.append(credit_card)



    def __str__(self):

        credit_accounts_info = ''
        if self.__credit_account:
            for account in self.__credit_account:
                credit_accounts_info += (f'\nНомер: {account._number}; '
                                         f'Баланс: {account._balance} {account._currency}.\n')
        else:
            credit_accounts_info += 'Нет счетов\n'

        debit_accounts_info = ''
        if self.__debit_account:
            for account in self.__debit_account:
                debit_accounts_info += (f'\nНомер: {account._number};'
                                        f'Баланс: {account._balance} {account._currency}.')
        else:
            debit_accounts_info += 'Нет счетов\n'

        credit_card = ''
        if self.__credit_card:
            for card in self.__credit_card:
                credit_card += (f'\nНомер карты: {card._CreditCard__number}.\n')
        else:
            credit_card = 'Карт нет'

        return (f'Клиент банка\n'
                f'Идентификатор: {self.__id};\n'
                f'Имя: {self.__name};\n'
                f'Статус: {self.__status};\n'
                f'Кредитный рейтинг: {self.__credit_rating};\n'
                f'Кредитные счета: {credit_accounts_info}'
                f'Дебетовые счета: {debit_accounts_info}'
                f'Кредитные карты: {credit_card}\n')



client = BankClient(100, 'Станислав', 'Привилегия', 989)


credit_account = CreditAccount(12345678911234567891, 'Rub', 0, client, date.today(), 'Открыт', 10000, 35, 55)
credit_card_1 = CreditCard(1234567890123456, 2030, 12, 'На все 1%')
client.add_credit_account(credit_account)
client.add_credit_card(credit_card_1)

print(client)

manager = Manager(400, 'Алекс', 32, 'Муж.', 100000, 'Работать', True, 'Привилегированные клиенты')

cashier = Cashier(520, 'Ник', 45, 'Муж.', 75000, 'Считать деньги', True, 'Валютные операции')

credit_card_1.assign_credit_account(credit_account)

