from Task_7.Salary import Salary
from Task_7.Person import Person
from Task_7.Mixins import FoodMixin, WeightMixin
from Task_7.decorators import *
from Task_7.Exceptions import *


class Fighter(Person, FoodMixin, WeightMixin):
    """ Базовый класс 'Боец' """

    __count = 0
    __summary_salary = 0  # суммарная зарплата всех спортсменов
    __discharges = ['3', '2', '1', 'КМС', 'МС', 'МСМК']  # возможные разряды спортсменов
    __base_health = 100  # базовое здоровье бойцов

    def __init__(self, name, surname, age, weight, discharge='3', patronymic='', salary=0):
        """Инициализация объекта данного класса"""
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.__age = age
        self.__salary = Salary(salary)  # композиция с классом Salary
        self.__health = 100
        self.__discharge = discharge
        try:
            if not (40 <= weight <= 300):
                self.__weight = None
                raise WrongWeightException('Некорректное значение веса!', weight)
        except WrongWeightException as m:
            print(m)
        else:
            self.__weight = weight
        Fighter.__count += 1
        Fighter.__summary_salary += salary

    def __str__(self):
        """Строковое представление объекта данного класса в виде ФИО"""
        return self.surname + " " + self.name + " " + self.patronymic

    def who_am_i(self):
        """Переопределение метода из абстрактного класса"""
        return "Hello, I am a Fighter!"

    def get_information(self):
        """Получение основной информации о бойце"""
        s = str(self)
        s += "\nВозраст: {0}\n".format(self.age)
        s += "Зарплата: {0}\n".format(self.salary)
        s += "Разряд: {0}\n".format(self.discharge)
        return s

    def eat_fish(self, count):
        """Дополнение метода из класса-миксина FoodMixin"""
        super().eat_fish(count)
        if self.__health < Fighter.__base_health - count:
            self.__health += count
            return "Ваше здоровье восполнилось на {0} единиц!".format(count)
        else:
            self.__health = Fighter.__base_health
            return "Ваше здоровье максимально!"

    @verify_weight
    def weight_on_the_scales(self, weight):
        """Дополнение метода из класса-миксина WeightMixin"""
        super().weight_on_the_scales(weight)
        self.__weight = weight
        return "Новый вес: {0}".format(weight)

    @property
    def weight(self):
        """Создание свойства-геттера для веса бойца"""
        return self.__weight

    @weight.setter
    @verify_weight
    def weight(self, weight):
        """Создание свойства-сеттера для веса бойца"""
        self.__weight = weight

    @property
    def age(self):
        """Создание свойства-геттера для возраста бойца"""
        return self.__age

    @age.setter
    @verify_age
    def age(self, age):
        """Создание свойства-сеттера для возраста бойца"""
        self.__age = age

    @property
    def discharge(self):
        """Создание свойства-геттера для разряда бойца"""
        return self.__discharge

    @discharge.setter
    def discharge(self, discharge):
        """Создание свойства-сеттера для разряда бойца"""
        try:
            if discharge not in Fighter.__discharges:
                raise WrongDischargeException("Такого разряда не существует!")
        except WrongDischargeException as m:
            print(m)
        else:
            try:
                if not Fighter.__discharges.index(discharge) > Fighter.__discharges.index(self.__discharge):
                    raise LowDischargeException("Присваиваемый разряд ниже текущего!")
            except LowDischargeException as m:
                print(m)
            else:
                self.__discharge = discharge

    @property
    def salary(self):
        """Создание свойства-геттера для зарплаты бойца"""
        return self.__salary

    @salary.setter
    def salary(self, salary):
        """Создание свойства-сеттера для зарплаты бойца"""
        self.__salary = salary

    @hit("Универсальный удар")
    def universal_hit(self, unit):
        """Метод, который используется объектом данного класса во время выполнения универсального удара"""
        self.reduce_health_after_universal_hit(unit)
        return "Прием совершен! У {0} осталось здоровья: {1}\n".format(unit, unit.health)

    @property
    def health(self):
        """Создание свойства-геттера для здоровья бойца"""
        return self.__health

    @health.setter
    def health(self, health):
        """Создание свойства-сеттера для здоровья бойца"""
        self.__health = health

    def health_recovery(self):
        """Восстановление здоровья бойца до базового значения для данного класса"""
        self.__health = Fighter.__base_health

    @staticmethod
    def reduce_health_after_universal_hit(unit):
        """Статичный метод, уменьшающий здоровье атакуемого бойца после универсального удара"""
        unit.health -= 5

    @staticmethod
    def get_summary_salary():
        """Статичный метод, получение общего гонорара, который должны выплатить всем бойцам
        (может быть полезно для продюссеров или организаторов мероприятия, в котором участвуют бойцы)"""
        return Fighter.__summary_salary

    @staticmethod
    def get_count():
        """Статичный метод, получение общего количества инициализированных(зарегистрированных бойцов)"""
        return Fighter.__count
