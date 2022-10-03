from random import randint, random, randrange


def PrintTask():
    print('1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.')
    print('2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.')
    print('3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму, округлённую до трёх знаков после точки.')
    print('4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].')
    print('5. Реализуйте алгоритм перемешивания списка.')
    print('0. Выход')


def Task1():
    s = input('Значение = ')
    sum = 0

    for i in range(0, len(s)):
        if s[i].isdigit():
            sum = sum + int(s[i])
    print(sum)


def Task2():
    n = int(input('N = '))
    rez = 1
    lst = []
    for i in range(1, n+1):
        rez = rez * i
        lst.append(rez)
    print(lst)


def Task3():
    n = int(input('N = '))
    sum = 0
    lst = []
    for i in range(1, n + 1):
        lst.append((1 + 1/i) ** i)

    for i in range(len(lst)):
        sum = sum + lst[i]

    print(round(sum, 3))


def Task4():
    n = int(input('N = '))
    lst = []
    elemPosition_1 = int(input('Позиция первого элемента = '))
    elemPosition_2 = int(input('Позиция второго элемента = '))

    for i in range(-n, n+1):
        lst.append(i)

    print(lst)

    rez = lst[elemPosition_1-1] * lst[elemPosition_2-1]

    print(rez)


def Task5():
    lst = []
    for i in range(10):
        lst.append(i)

    print('Исходный список')
    print(lst)

    for i in range(10):
        temp = lst[i]
        randomPosition = lst[randrange(0, 10)]
        lst[i] = lst[randomPosition]
        lst[randomPosition] = temp

    print('Переешанный список')
    print(lst)


PrintTask()
TaskNumber = int(input('Введите номер задачи '))

while TaskNumber != 0:
    while TaskNumber < 0 or TaskNumber >= 6:
        TaskNumber = int(input('Выберете задачу 1 - 5: '))

    if TaskNumber == 1:
        Task1()

    if TaskNumber == 2:
        Task2()

    if TaskNumber == 3:
        Task3()

    if TaskNumber == 4:
        Task4()

    if TaskNumber == 5:
        Task5()

    input('Для продолжения нажмите Enter')
    PrintTask()
    TaskNumber = int(input('Введите номер задачи: '))
