import random
from random import randint

def main():
    #task_1()
    #task_2()
    task_3()

def task_1():
    print("Введіть речення : ")
    words = input()
    sign = ",", ".", ":","!","?",";","-","'"," "
    for i in range(len(sign)):
        words = words.replace(sign[i], "")
    print("Клькість оригінальних символів (без урахування пробілів та знаків припинання): ",len(set(words)))
    input()

def task_2():
    print()
    nun_range=201
    print("-----Сгенеровано масив з кількістю елементів: ", nun_range-1, "-----")
    Znak_num=0
    fib1 = fib2 = 1
    a=1
    array=set()
    arr_Fibonachies=set()
    for n in range(1,nun_range):
        array.add(n)
    print(array)

    while fib2 < nun_range:
        arr_Fibonachies.add(fib2)
        fib1, fib2 = fib2, fib1 + fib2

    print("Числами Фібоначі є числа: ",array.intersection(arr_Fibonachies))
    for num in array:
        s_num=list(str(num))
        if s_num[0]=="1" or s_num[0]=="2":
            Znak_num+=1
    print("Кількість чисел перша значуща цифра яких дорівнює «1» або «2» = ", Znak_num)
    print()
    input()

def task_3():

    quantity = int(input("Введіть кількість множин: "))
    size = int(input("Введіть розмір множин: "))
    Array=dict()
    for num in range(quantity):
        Array[num]={random.randint(0, 50) for x in range(size)}
        print(num,":", Array[num])
    Array_keys=list(Array.keys())
    Array_Help=Array[0].copy()
    for key in Array_keys:
        if key%3==0:
            Array_Help.intersection_update(Array[key])
    print("Елементи що є в множинах які кратні трьом: ",Array_Help)
    print("Елементи що є в множинах які кратні трьом та не входять в множину 1: ", Array_Help.difference(Array[1]))


if __name__ == "__main__":
    main()