from Task_5.Fighter_types import *
import threading


def battle(unit1, unit2):

    while unit1.health > 0 and unit2.health > 0:
        print(unit1.universal_hit(unit2))
        if unit2.health > 0:
            print(unit2.universal_hit(unit1), "\n\n")


"""Инициализация бойцов"""
u1 = KickBoxer('Иван', 'Иванов', 20, 330)  # проверка некорректного веса
u2 = KickBoxer('Иван', 'Петров', 21, 10)  # проверка некорректного веса

u3 = Boxer('Петр', 'Петров', 27, 78)
u4 = Boxer('Петр', 'Иванов', 25, 83)

u3.discharge = "КМ"  # проверка некорректного разряда

u3.discharge = "МС"
u3.discharge = "КМС"  # проверка исключения, когда присваиваемый разряд ниже текущего


"""Бой между созданными бойцами, проверка созданных методов класса"""
print("\n\nНачало соревнований: ")

thr1 = threading.Thread(target=battle, args=(u1, u2), name="А")
thr2 = threading.Thread(target=battle, args=(u3, u4), name="Б")

thr1.start()
thr2.start()
