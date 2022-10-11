
from random import choices, randrange


def PrintTask():
    print('1. Вычислить число π c заданной точностью d')
    print('2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.')
    print('3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.')
    print('4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.')
    print('5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов. Коэффициенты могут быть как положительными, так и отрицательными. Степени многочленов могут отличаться.')
    print('0. Выход')


def Task1():
    d = float(input('Введите точность чсила пи: '))
    summa = 1
    n= 3
    flag = False
    while 1 / n > d:
        if flag:
            summa = summa + (1/n)
            flag = False
        else:
            summa = summa - (1/n)
            flag = True
        n = n + 2
    print(summa*4)

def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def prime_factors(number):
    if is_prime(number):
        return 'Это простое число'

    factor = 2
    lst = []
    while number != 1:
        if is_prime(factor) and number % factor == 0:
            number /= factor
            lst.append(factor)
        else:
            factor += 1

    return lst

def Task2():
    num = int(input('Число = '))
    print(prime_factors(num))

def Task3():
    n = int(input('Количество чисел в последовательности = '))
    lst = []
    lst_result = []
    sum = 0

    for i in range(n):
        lst.append(int(input('Число ' + str(i+1) + ' = ')))

    for i in range (n):
        if lst.count(lst[i]) == 1:
            lst_result.append(lst[i])

    print(lst_result)

def add_plus_minus(str_data):
    if str_data == '':
        return str_data
    return str_data + f" {choices('+-', k=1)[0]} "


def add_to_file(str_data):
    with open("task4.txt", "a", encoding="utf-8") as output:
        output.write(str_data + '\n')
        
def Task4():
    k = int(input('k = '))

    ls = []
    for i in range(k):
        ls.append(randrange(0, 101))
    print('Список коэффициентов')
    print(ls)
   
    eq = ''
    while k >= -1:
        if ls[k - 1] == 0:
            k -= 1
            continue
        elif k > 1:
            eq = add_plus_minus(eq)
            eq = eq + f'{ls[k - 1]}*x^{k}'
        elif k == 1:
            eq = add_plus_minus(eq)
            eq = eq + f'{ls[k - 1]}'
        elif k == 0:
            eq = eq + ' = 0'
        k -= 1

    print(eq)
    add_to_file(eq)

def read_file(name):
    with open(name, "r", encoding="utf-8") as output:
        lst = []
        for line in output:
            lst.append(line)
        output.close()
        return lst

def Task5():
    lst_1 = read_file('file1.txt')
    lst_2 = read_file('file2.txt')
    if len(lst_1) != len(lst_2):
        print('The contents of the files do not match!')
        return
    with open("task5.txt", "w", encoding="utf-8") as output:
        for i in range(2):
            output.write(lst_1[i].replace('= 0', '+ ').replace('\n', '') + lst_2[i])

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
