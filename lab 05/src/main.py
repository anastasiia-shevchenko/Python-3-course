def main():
    task_1()
    #task_2()
   # task_3()

def task_1():
    print("Введите предложение: ")
    words = input()
    sign = ",", ".", ":","!","?",";","-","'"," "
    for i in range(len(sign)):
        words = words.replace(sign[i], "")
    words = list(words)
    print("Довжина введеного рядка без урахування проблів та знаків припинання: ",len(words))

if __name__ == "__main__":
    main()