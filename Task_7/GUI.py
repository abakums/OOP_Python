from tkinter import *
from tkinter import messagebox


class GUI:
    @staticmethod
    def get_and_start():
        un1 = units[int(unit1.get()) - 1]
        un2 = units[int(unit2.get()) - 1]

        while un1.health > 0 and un2.health > 0:
            info_str = Competition.battle(un1, un2)
            messagebox.showinfo(title="Битва", message=info_str)
        i = info_str.rfind('\n\n\n')
        s = Label(frame, text=info_str[i:].strip(), bg="grey", font=40)
        s.pack()

    @staticmethod
    def get_units(fr, un):
        for i in range(len(un)):
            inf = str(un[i]) + " ({0})".format(i + 1)
            s = Label(fr, text=inf, bg="grey", font=40)
            s.pack()