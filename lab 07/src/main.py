import random
from random import randint
import datetime
import random
import time

Registered = []
def time_funk(func):
    """
    Декоратор для відстежування часу початку та завершення виконання програми
    (використовуйте модуль datetime);

    :param func: Функція, яку обгортує декоратор
    :return: Повертає функцію-"обгортку"
    """
    def wrapper(arg1,arg2,arg3):
        """
        Функція-"обгортка"
        :param arg: Аргумент, який приймає основна(декорована) функція
        """
        start_time = datetime.datetime.now()
        func(arg1,arg2,arg3)
        end_time = datetime.datetime.now()
        finally_time = end_time - start_time
        return finally_time

    return wrapper

def decorator_reg(func):
    """

    :param func:
    :type func:
    :return:
    :rtype:
    """
    def wrapper(*arguments):
        function = func(*arguments)
        i = 0
        for i in range(len(Registered)):

            if func.__name__ == Registered[i]:
                return function
            i = i + 1
        Registered.append(func.__name__)
        return function
    return wrapper

def my_decorator(func):
    """
    Декоратор для декількох запусків функції у разі її неуспішного виконання

    :param func: Функція, яку обгортує декоратор
    :return: Повертає функцію-"обгортку"
    """
    def wrapper():
        """
        Функція-"обгортка"

        """
        s = False
        while not s:
            s = func()
    return wrapper

@decorator_reg
def my_func():

    probability_num=random.randint(1, 100)
    if probability_num>80: # Вероятность правильного срабативыния функции 80%
        f=False
    else:
        f = True

    if not f:
        print("Функція виконана неправильно")
    else:
        print("Функція виконана правильно")
    return f

@decorator_reg
def arithmetic_progression(first_num,step,finaly_num):
    """
    Функція визначає значення n-го елементу аривметичної прогресії

    :param first_num: Початкове значення прогресії
    :param step: Крок прогресії
    :param finaly_num: Номер шуканого елементу
    """
    print("-----Арифметична прогресія-----")

    for i in range(finaly_num - 1):
        first_num += step
    print("Значеня", finaly_num, "елементу = ", first_num)


def main():

    first_num = int(input("Введіть початкове значення: "))
    step = int(input("Введіть крок прогресії: "))
    finaly_num = int(input("Введіть номер елементу прогресії який хочете знайти: "))

    decorated = time_funk(arithmetic_progression)
    t = decorated(first_num,step,finaly_num)
    print(f"Час виконання: {t}")
    my_func_decorated = my_decorator(my_func)
    my_func_decorated()
    print(f"Registered: {Registered}")



if __name__ == '__main__':
    main()
