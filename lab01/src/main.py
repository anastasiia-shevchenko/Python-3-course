import math

a=True
while a:
    print("Введите Х (Х>0)")
    x = int(input())
    if x<=0 :
        print("Вы ввели не верное значение Х")
    else:
        a = (math.sqrt((3 * x + 2) ** 2 - 24 * x))
        b = (3 * math.sqrt(x) - (2 / math.sqrt(x)))
        Z = a / b
        print("Результат:", Z)
        a=False

