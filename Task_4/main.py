from Task_4.Fighter_types import *
from Task_4.Salary import Salary

"""Проверка работоспособности метаклассов"""

print(Salary, end="\n\n")

"""Инициализация бойцов"""
u1 = Boxer('Иван', 'Иванов', 20, 70)
u2 = KickBoxer('Петр', 'Петров', 21, 80)

"""Проверка декораторов-условий для присваивания корректного веса и возраста бойца"""
u1.weight = 310
u2.weight_on_the_scales(30)
print(u1.weight)
print(u2.weight)

u1.age = 100
print(u1.age)

"""Бой между созданными бойцами, проверка созданных методов класса"""
print("Начало боя: ")
print("Здоровье первого бойца: ", u1.health)
print("Здоровье второго бойца: ", u2.health)
while u1.health > 0 and u2.health > 0:
    print(u1.universal_hit(u2))
    if u2.health > 0:
        print(u2.universal_hit(u1))
