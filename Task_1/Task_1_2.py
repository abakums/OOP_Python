"""Функция initial() возвращает сформированный список чисел, введенных
с клавиатуры с предложением ввести количество чисел"""


def initial():
    n = int(input('Введите количество вещественных чисел, которое хотите ввести: '))
    a = []
    for i in range(n):
        a.append(float(input()))
        a[i] *= 0.13
    a.sort()
    return a


"""Функция simple_out(a) печатает на экран значения элементов переданного в 
качестве параметра списка a"""


def simple_out(a):
    for i in a:
        print(round(i, 2))


"""Функция file_out(a, file_name) создает файл с названием file_name и 
записывает в него значения элементов списка a"""


def file_out(a, file_name='Task_1_out.txt'):
    file = open(file_name, 'w', encoding='utf_8')
    for i in a:
        file.write(str(round(i, 2)) + '\n')
    file.close()


# тестирование созданных функций
m = initial()
simple_out(m)
f_name = input('Введите название файла, в который будут сохранены данные списка: ')
file_out(m, f_name)
