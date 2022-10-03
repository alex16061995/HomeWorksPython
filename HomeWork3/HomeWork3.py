
from random import randrange
def PrintTask():
    print('1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.')
    print('2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.')
    print('3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.')
    print(
        '4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.')
    print('5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.')
    print('0. Выход')


def Task1():
    n = int(input('Количество чисел в последовательности = '))
    lst = []
    sum = 0

    for i in range(n):
        lst.append(input('Число ' + str(i+1) + ' = '))
        if i % 2 != 0:
            sum = sum + int(lst[i])

    print(lst)
    print('Сумма элементов списка, стоящих на нечётной позиции = ' + str(sum))


def Task2():
    n = int(input('Количество чисел в последовательности = '))
    lst = []
    lstResult = []
    sum = 0
    if n % 2 == 0:
        endOfCycle = int(n/2)
    else:
        endOfCycle = int(n/2) + 1
    for i in range(n):
        lst.append(randrange(1, 10))

    print('Исходный список')
    print(lst)

    for i in range(endOfCycle):
        lstResult.append(lst[i] * lst[n-1-i])

    print('Новый список ')
    print(lstResult)


def Task3():
    n = int(input('Количество чисел в последовательности = '))
    lst = []
    sum = 0

    for i in range(n):
        lst.append(float(input('Число ' + str(i+1) + ' = ')))

    min = 1
    max = -1

    for i in range(1, n):
        if lst[i] % 1 == 0:
            continue
        else:
            if lst[i] % 1 < min:
                min = lst[i] % 1
            if lst[i] % 1 > max:
                max = lst[i] % 1

    print(round(max - min, 2))


def Task4():
    n = int(input('Введите число = '))
    strResult = ""
    while n / 2 != 0 and n / 2 != 1:
        strResult = str(n % 2) + strResult
        n = int(n / 2)
    
    if int(n / 2) == 0:
        if int(n % 2) == 1:
            strResult = str(int(n % 2)) + strResult
    else:
        strResult = str(int(n / 2)) + str(int(n % 2))+ strResult

    print(strResult)


def fibPlus(k):
    if k == 0:
        return 0
    elif k in [1, 2]:
        return 1
    else:
        return fibPlus(k-1) + fibPlus(k-2)

def fibMinus(k):
    if k == -1:
        return 1
    elif k == -2:
        return -1
    else:
        return fibMinus(k+2) - fibMinus(k+1)


def Task5():
    k = int(input('Введите число = '))
    lst = []
    for i in range(-k, 0):
        lst.append(fibMinus(i))

    for i in range(0, k+1):
        lst.append(fibPlus(i))
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
