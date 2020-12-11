class WrongWeightException(Exception):
    """Класс исключения, который отвечает за отлавливание ошибок некорректного ввода веса бойца"""
    def __init__(self, text,  weight):
        self.text = text
        self.wrong_weight = weight

    def __str__(self):
        return self.text


class WrongDischargeException(Exception):
    """Класс исключения, который отвечает за отлавливание ошибок ввода некорректного разряда бойца"""
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return "Ошибка! Некоректное значение разряда! " + self.text


class LowDischargeException(Exception):
    """Класс исключения, который отвечает за отлавливание ошибок при присваивании разряда, которые ниже текущего"""
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return "Ошибка! Низкое значение разряда! " + self.text
