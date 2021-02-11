import random
from random import randint

def main():
    task_1()
    #task_2()
    #task_3()



def task_1():
    print("Введите количество элементов в списке")
    Size = int(input())
    my_list = list()
    i = 0
    while i < Size:
        my_list.append(random.randint(-60, 60))
        i += 1
    print(my_list)
    i=0
    j=0
    my_list2=list()
    index=-1
    while i<Size:
        if my_list[i]<0 and index==-1:
            index=i
        elif my_list[i]<0 and my_list[i]>my_list[index]:
            index=i
        i+=1
    print("Найбольший отрицательный элемент: ",my_list[index])
    while j<index:
        my_list2.append(my_list[j]**2)
        j+=1
    print(my_list2)

#--------------------------------------------------------------------------------
def task_2():
    print("Введите количество строк")
    line = int(input())
    print("Введите количество столбцов")
    column= int(input())
    my_list = [[randint(0, 20) for j in range(line)] for i in range(column)]
    for i in range(0, line):
        for j in range(0, column):
            print(my_list[i][j], end = "  ")
        print("\n")

    max_i = 0
    max_j = 0
    for i in range(0, line):
        for j in range(0, column):
            if my_list[i][j] > my_list[max_i][max_j]:
                max_i = i
                max_j = j
    print("Максимальный положительный элемент: ",my_list[max_i][max_j])
    for i in range(line):
        my_list[i][1], my_list[i][max_i] = my_list[i][max_i], my_list[i][1]
    print("Новаый список: ")
    for i in range(0, line):
        for j in range(0, column):
            print(my_list[i][j], end = "  ")
        print("\n")

#--------------------------------------------------------------------------------
def task_3():
    print("Введите предложение: ")
    words = input()
    words = words.replace(',', '').replace('.', '').replace(':', '').replace('!', '').replace('?', '').replace(';', '').replace('-', '').replace(')', '')
    words = words.split()
    letter_counts = list(map(lambda x: len(x), words))
    print("Количество букв в каждом слове: ")
    print(letter_counts)
    i=0
    num=0
    size =len(letter_counts)
    while i< size:
        if letter_counts[i] >= 10:
            num+=1
        i+=1
    if num > 0:
        print("В самом длинном слове предложения больше 10-ти букв")
    else:
        print("Во всех словах предложения меньше 10-ти букв")

if __name__ == "__main__":
    main()


