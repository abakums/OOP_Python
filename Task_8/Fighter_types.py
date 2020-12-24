from .Fighter import Fighter
from Task_8.decorators import hit


class Boxer(Fighter):
    """ Класс 'Боксер' (наследуется от класса 'Боец')"""

    def who_am_i(self):
        return "I'm a Boxer"

    @staticmethod
    def reduce_health_after_lead(unit):
        """Статичный метод, уменьшающий здоровье атакуемого бойца после прямого удара"""
        unit.health -= 8

    @hit("Прямой удар")
    def lead(self, unit):
        """Метод, который используется объектом данного класса во время выполнения прямого удара"""
        self.reduce_health_after_lead(unit)
        return "Прием совершен! У {0} осталось здоровья: {1}\n".format(unit, unit.health)

    @staticmethod
    def reduce_health_after_swing(unit):
        """Статичный метод, уменьшающий здоровье атакуемого бойца после бокового удара"""
        unit.health -= 10

    @hit("Боковой удар")
    def swing(self, unit):
        """Метод, который используется объектом данного класса во время выполнения бокового удара"""
        self.reduce_health_after_swing(unit)
        return "Прием совершен! У {0} осталось здоровья: {1}\n".format(unit, unit.health)


class KickBoxer(Fighter):
    """ Класс 'Кикбоксер' (наследуется от класса 'Боец')"""

    def who_am_i(self):
        return "I'm a KickBoxer"

    @staticmethod
    def reduce_health_after_punch(unit):
        """Статичный метод, уменьшающий здоровье атакуемого бойца после удара рукой"""
        unit.health -= 6

    @hit("Удар рукой")
    def punch(self, unit):
        """Метод, который используется объектом данного класса во время выполнения удара рукой"""
        self.reduce_health_after_punch(unit)
        return "Прием совершен! У {0} осталось здоровья: {1}\n".format(unit, unit.health)

    @staticmethod
    def reduce_health_after_kick(unit):
        """Статичный метод, уменьшающий здоровье атакуемого бойца после удара ногой"""
        unit.health -= 12

    @hit("Удар ногой")
    def kick(self, unit):
        """Метод, который используется объектом данного класса во время выполнения удара ногой"""
        self.reduce_health_after_kick(unit)
        return "Прием совершен! У {0} осталось здоровья: {1}\n".format(unit, unit.health)


class Wrestler(Fighter):
    """ Класс 'Борец' (наследуется от класса 'Боец')"""

    @staticmethod
    def reduce_health_after_sweep(unit):
        """Статичный метод, уменьшающий здоровье атакуемого бойца после подсечки"""
        unit.health -= 7

    @hit("Подсечку")
    def sweep(self, unit):
        """Метод, который используется объектом данного класса во время выполнения подсечки"""
        self.reduce_health_after_sweep(unit)
        return "Прием совершен! У {0} осталось здоровья: {1}\n".format(unit, unit.health)

    @staticmethod
    def reduce_health_after_deflection(unit):
        """Статичный метод, уменьшающий здоровье атакуемого бойца после броска"""
        unit.health -= 11

    @hit("Бросок")
    def deflection(self, unit):
        """Метод, который используется объектом данного класса во время выполнения броска"""
        self.reduce_health_after_deflection(unit)
        return "Прием совершен! У {0} осталось здоровья: {1}\n".format(unit, unit.health)

    @staticmethod
    def reduce_health_after_universal_hit(unit):
        """В силу того, что у борца плохая ударная техника, уменьшаемое ударами здоровье будет меньше"""
        unit.health -= 1


class CombatWrestler(KickBoxer, Wrestler):
    @staticmethod
    def reduce_health_after_sweep(unit):
        """Статичный метод, уменьшающий здоровье атакуемого бойца после подсечки"""
        unit.health -= 6

    @staticmethod
    def reduce_health_after_kick(unit):
        """Статичный метод, уменьшающий здоровье атакуемого бойца после удара ногой"""
        unit.health -= 10
