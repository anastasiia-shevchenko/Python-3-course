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

print("---Определение избыточного числа---")
a=True
while a:
    print("Введите N (N>0)")
    n = int(input())
    k=0
    if n<=0 :
        print("Вы ввели не верное значение N")
    else:
        for i in range(1,n/2):
            if n%i==0:
                k+=i
                print(k)
        a=False
if k>n:
    print("Число", n, "избыточное так как сумма = ", k, ">", n)
else:
    print("Число", n, "не избыточное так как сумма = ", k, "<=", n)
