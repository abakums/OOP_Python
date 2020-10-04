from Task_3.Salary import Salary
from Task_3.Fighter_types import *

"""Инициализация бойцов и вывод информации об одном из них"""
u1 = Boxer('Иван', 'Иванов', 20, 70)
u2 = KickBoxer('Петр', 'Петров', 21, 80)
print("ФИ: ", u1)
print("Возраст: ", u1.age)
print("Разряд: ", u1.discharge)
print("Зарплата:", u1.salary)
print("Количество бойцов: ", Fighter.get_count())

"""Инициализация различных зарплат для разрядов, проверка работоспособности
перегрузки оператора сложения для объектов класса Salary"""
kms_salary = Salary(10000)
ms_salary = kms_salary + 5000
u1.discharge = 'КМС'
u1.salary = kms_salary
print("Новый разряд: ", u1.discharge)
print("Новая зарплата: ", u1.salary, "\n")
u1.discharge = 'МС'
u1.salary = ms_salary
print("Новый разряд: ", u1.discharge)
print("Новая зарплата: ", u1.salary, "\n")

"""Бой между созданными бойцами, проверка созданных методов класса"""
print("Начало боя: ")
print("Здоровье первого бойца: ", u1.health)
print("Здоровье второго бойца: ", u2.health)
while u1.health > 0 and u2.health > 0:
    print(u1.lead(u2))
    print(u2.kick(u1))

"""Проверка переопределенных методов Task_3"""
print(u1.get_information())
print(u1.who_am_i())
print("Вес: ", u1.weight)
print(u1.weight_on_the_scales(100))
print("Вес: ", u1.weight)
print(u1.eat_fish(10))
u1.health = 50
print("Здоровье: ", u1.health)
print(u1.eat_fish(20))
print("Здоровье: ", u1.health)

