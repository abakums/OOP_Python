from Task_8.Fighter_types import *
from Task_8.Battle import *
from Task_8.Facade import *

"""Инициализация бойцов"""
units = [KickBoxer('Иван', 'Иванов', 20, 70), KickBoxer('Иван', 'Петров', 21, 80), Boxer('Петр', 'Петров', 27, 78),
         Boxer('Петр', 'Иванов', 25, 83), Boxer('Василий', 'Петров', 22, 68), Boxer('Василий', 'Васильев', 29, 73)]

"""Битва (Шаблонный паттерн)"""
b1 = Battle
b1.detail_battle(Battle, units[0], units[2])

"""Информация Person и Salary"""
s = Salary(150)
p = Fighter("Иван", "Иванов", 20, 70)
f = Facade(s, p)
client_code(f)
