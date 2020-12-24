class ClassName(type):
    """Данный метакласс выводит название класса-экземпляра"""
    def __str__(cls):
        return "Данный класс называется {0}".format(cls.__name__)


class MultiBases(type):
    """
    этот метод вызывается перед __init __ (),
    он создает объект и возвращает его.
    Переопределяем этот метод для управления пройесса создания объектов
    """

    def __new__(cls, clsname, bases, clsdict):
        print("Данный класс наследуется от {0} класса(ов)".format(len(bases)))
        return super().__new__(cls, clsname, bases, clsdict)


class MetaClass(ClassName, MultiBases):
    pass

