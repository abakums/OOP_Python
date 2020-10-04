class Salary:
    """Класс, отвечающий за гонорар бойца"""

    def __init__(self, pay):
        """Инициализация объекта"""
        self.pay = pay

    def __str__(self):
        """Строковое представление объекта данного класса в виде значения самого гонорара"""
        return str(self.pay)

    def __add__(self, other):
        """Перегрузка оператора сложения"""
        return Salary(self.pay + other)

    def __sub__(self, other):
        """Перегрузка оператора вычитания"""
        return Salary(self.pay - other)

    def get_month_salary(self):
        """Получение месячной зарплаты исходя из размера гонорара"""
        return round(self.pay/12, 2)
