from Task_6.Fighter_types import *
import asyncio


@asyncio.coroutine
def battle(unit1, unit2, ring_numb):
    """функция для проведения боя между двумя бойцами"""
    while unit1.health > 0 and unit2.health > 0:
        print("ring number: {0}\n".format(ring_numb), unit1.universal_hit(unit2), "\n")
        yield from asyncio.sleep(0.2)
        if unit2.health > 0:
            print("ring number: {0}\n".format(ring_numb), unit2.universal_hit(unit1), "\n")
            yield from asyncio.sleep(0.2)
    if ring_numb == "А":
        loop.stop()


"""Инициализация бойцов"""
u1 = KickBoxer('Иван', 'Иванов', 20, 70)
u2 = KickBoxer('Иван', 'Петров', 21, 80)

u3 = Boxer('Петр', 'Петров', 27, 78)
u4 = Boxer('Петр', 'Иванов', 25, 83)

u5 = Boxer('Василий', 'Петров', 22, 68)
u6 = Boxer('Василий', 'Васильев', 29, 73)


"""Бой между созданными бойцами"""
print("\n\nНачало соревнований: ")

loop = asyncio.get_event_loop()  # создание цикла событий
tasks = [
    asyncio.ensure_future(battle(u1, u2, "А")),
    asyncio.ensure_future(battle(u3, u4, "Б"))]  # создание списка событий, которые необходимо выполнить
loop.run_forever()  # асинхронное исполнение задач
tasks.append(asyncio.ensure_future(battle(u5, u6, "А")))  # начинается новый боя на ринге А
while not loop.is_running():  # выполнение всех оставшихся событий
    loop.run_forever()
loop.close()
