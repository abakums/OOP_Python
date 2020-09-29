from Task_2.Salary import Salary


class Fighter:
    """ Базовый класс 'Боец' """

    __count = 0
    __summary_salary = 0  # суммарная зарплата всех спортсменов
    __discharges = ['3', '2', '1', 'КМС', 'МС', 'МСМК']  # возможные разряды спортсменов
    __base_health = 100  # базовое здоровье бойцов

    def __init__(self, name, surname, age, discharge='3', patronymic='', salary=0):
        """Инициализация объекта данного класса"""
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.__age = age
        self.__salary = Salary(salary)  # композиция с классом Salary
        self.__health = 100
        self.__discharge = discharge
        Fighter.__count += 1
        Fighter.__summary_salary += salary

    def __str__(self):
        """Строковое представление объекта данного класса в виде ФИО"""
        return self.surname + " " + self.name + " " + self.patronymic

    @property
    def age(self):
        """Создание свойства-геттера для возраста бойца"""
        return self.__age

    @age.setter
    def age(self, age):
        """Создание свойства-сеттера для возраста бойца"""
        if age in range(8, 61):
            self.__age = age
        else:
            print("Некорректный возраст!")

    @property
    def discharge(self):
        """Создание свойства-геттера для разряда бойца"""
        return self.__discharge

    @discharge.setter
    def discharge(self, discharge):
        """Создание свойства-сеттера для разряда бойца"""
        if discharge in Fighter.__discharges:
            if Fighter.__discharges.index(discharge) > Fighter.__discharges.index(self.__discharge):
                self.__discharge = discharge
            else:
                print("Присваиваемый разряд ниже текущего!")
        else:
            print("Некорректный разряд")

    @property
    def salary(self):
        """Создание свойства-геттера для зарплаты бойца"""
        return self.__salary

    @salary.setter
    def salary(self, salary):
        """Создание свойства-сеттера для зарплаты бойца"""
        self.__salary = salary

    def universal_hit(self, unit):
        """Метод, который используется объектом данного класса во время выполнения универсального удара"""
        self.reduce_health_after_universal_hit(unit)
        return self.after_hit(unit)

    def after_hit(self, unit):
        """Метод, возвращающий информацию об атаке бойца и остатке здоровья его соперника"""
        s = "{0} нанес удар бойцу {1} и его остаток здоровья: {2}\n" \
            .format(self, unit, unit.health)
        if unit.__health <= 0:
            s += "В этом бою проиграл {0}| у бойца {1} остаток здоровья: {2}\n\n" \
                .format(unit, self, self.health)
        return s

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
