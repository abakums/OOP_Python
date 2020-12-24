from Task_8.Fighter import *


class Facade:
    """Класс Фасада для системы из нескольких подсистем"""
    def __init__(self, _subsystem1: Salary, _subsystem2: Fighter):
        self._subsystem1 = Salary(150)
        self._subsystem2 = Fighter()

    def info(self):
        results = []
        results.append("\n\nИнформация о типе, к которому относится человек и о зарплате:")
        results.append("Месячная зарплата: {0}".format(str(self._subsystem1.get_month_salary())))
        results.append("Person: {0}".format(str(self._subsystem2.who_am_i())))
        return "\n".join(results)


def client_code(facade: Facade) -> None:
    """Клиентский код, работающий со сложными подсистемами"""
    print(facade.info(), end="")
