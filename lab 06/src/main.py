import random
from random import randint



def task_1():
    print("-----Створення списку чисел-----")
    Size = int(input("Введіть розмір списку: "))
    circle = 1
    my_list = list()
    i = 0
    while i < Size:
        my_list.append(random.randint(1, 10))
        i += 1
    while circle:
        menu()
        answer = input()
        if answer == "1":
            print(my_list)
        elif answer == "2":
            sort_elem(my_list)
            print("Відсортований список: ", my_list)
        elif answer == "3":
            num_el=search_elem(my_list)
            print("Номер першого шуканого елементу: ", num_el)
        elif answer == "4":
            my_list.sort()
            min_elems(my_list)
        elif answer == "5":
            my_list.sort(reverse=True)
            max_elems(my_list)
        elif answer == "6":
            average_num=average(my_list)
            print("Середнє арифметичне списку: ", average_num)
        elif answer == "7":
            print("Список що не містить повторів: ", list(set(my_list)))
        elif answer == "8":
            print("Спасибо за работу!")
            circle = 0

def menu():
    """
    Меню програми з діями які можна виконати
    """
    print("------Выберите действие которое хотите сделать------")
    print("1. Вивести список на экран.")
    print("2. Швидке сортування.")
    print("3. Пошук елементу за значенням.")
    print("4. Пошук перших 𝑛 мінімальних елементів.")
    print("5. Пошук перших 𝑛 максимальних елементів.")
    print("6. Пошук середнього арифметичного.")
    print("7. Повернення списку, що не містить повторів.")
    print("8. Выход.")

def sort_elem(my_list):
    """
    Сортує масив єлементів по збільшенню

    :param my_list: Масив вхідних даних
    :type my_list: Список чисел
    :return: Повертає відсортований масив
    :rtype: Список
    """
    return my_list.sort()

def search_elem(my_list):
    """
    Виконуэться пошук індексу заданого елементу

    :param my_list: Масив вхідних даних
    :type my_list: Список чисел
    :return: Індекс елементу
    :rtype: Число
    """
    num = int(input("Введіть елемент, номер якого хочете дізнатися: "))
    return my_list.index(num)

def min_elems(my_list):
    """
    Виконуэться пошук перших n мінімальних елементів

    :param my_list: Масив вхідних даних
    :type my_list: Список чисел
    :return: Виводить на екран мінімальні елементи
    """
    min_elem = int(input("Введіть, скільки мінімальних елементів вивести: "))
    for i in range(min_elem):
        print(my_list[i])

def max_elems(my_list):
    """
    Виконуэться пошук перших n максимальних елементів

    :param my_list: Масив вхідних даних
    :type my_list: Список
    :return: Виводить на екран максимальні елементи
    """
    max_elem = int(input("Введіть, скільки максимальних елементів вивести: "))
    for v in range(max_elem):
        print(my_list[v])

def average(my_list):
    """
    Пошук середнього арифметичного елементів масиву

    :param my_list: Масив вхідних даних
    :type my_list: Список чисел
    :return: Середнє арифметичне масиву
    :rtype: Чмсло
    """
    return sum(my_list)/len(my_list)

def task_2():
    print("-----Арифметична прогресія-----")
    first_num=int(input("Введіть початкове значення: "))
    step=int(input("Введіть крок прогресії: "))
    finaly_num=int(input("Введіть номер елементу прогресії який хочете знайти: "))
    for i in range(finaly_num-1):
        first_num+=step
    print("Значеня", finaly_num, "елементу = ", first_num)
    input()

if __name__ == '__main__':
    task_1()
    task_2()
