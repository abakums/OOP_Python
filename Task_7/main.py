from Task_7.Fighter_types import *
from tkinter import *
from tkinter import messagebox


class GUI:
    """Класс, содержащий статические методы для вывода событий в главное окно"""
    @staticmethod
    def get_and_start():
        """Получаем двух введенных бойцов и начинаем сражение между ними"""
        un1 = units[int(unit1.get())-1]
        un2 = units[int(unit2.get())-1]

        while un1.health > 0 and un2.health > 0:
            info_str = Competition.battle(un1, un2)
            messagebox.showinfo(title="Битва", message=info_str)
        i = info_str.rfind('\n\n\n')
        s = Label(frame, text=info_str[i:].strip(), bg="grey", font=40)
        s.pack()

    @staticmethod
    def get_units(fr, un):
        """Получаем и выводим список бойцов в главное окно"""
        for i in range(len(un)):
            inf = str(un[i]) + " ({0})".format(i+1)
            s = Label(fr, text=inf, bg="grey", font=40)
            s.pack()


class Competition:
    """Класс, содержащий метод(ы) для проведения соревнований"""
    @staticmethod
    def battle(u1, u2):
        """Проведение сражения между двумя бойцами"""
        s = ""
        while u1.health > 0 and u2.health > 0:
            s += u1.universal_hit(u2) + "\n\n"
            if u2.health > 0:
                s += u2.universal_hit(u1) + "\n\n"
            return s


"""Инициализация бойцов"""
units = [KickBoxer('Иван', 'Иванов', 20, 70), KickBoxer('Иван', 'Петров', 21, 80), Boxer('Петр', 'Петров', 27, 78),
         Boxer('Петр', 'Иванов', 25, 83), Boxer('Василий', 'Петров', 22, 68), Boxer('Василий', 'Васильев', 29, 73)]

"""Бой между созданными бойцами"""

root = Tk()  # создаем главное окно
root.title("Соревнования")
root.geometry("600x350")

canvas = Canvas(root, height=600, width=350)  # создаем холст для вывода(отрисовки) объектов
canvas.pack()

frame = Frame(root, bg="red")  # создаем рамку, содержащую другие визуальные компоненты
frame.place(relx=0, rely=0, relwidth=1, relheight=1)

title = Label(frame, text="Введите id бойцов, битву которых хотите устроить(1..6): ", bg="grey", font=40)  # надпись
title.pack()
GUI.get_units(frame, units)  # выводим список бойцов в главном окне
unit1 = Entry(frame, bg="white")  # поле для ввода номера первого бойца
unit1.pack()
unit2 = Entry(frame, bg="white")  # поле для ввода номера второго бойца
unit2.pack()

btn = Button(frame, text="В бой!", bg="yellow", command=GUI.get_and_start)  # кнопка для запуска боя
btn.pack()

root.mainloop()  # запускаем постоянный цикл
