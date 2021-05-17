

def task_1():
    try:
        r=" "
        file1 = open("prim1-1.txt", "r")
        file2 = open("prim1-2.txt", "w")
        print("Файли відкриті")
        try:
            for line in file1:
                lst=line.split()
                lst[-1], lst[0] = lst[0], lst[-1]
                file2.write(r.join(lst))
                file2.write("\n")
            print("Робота з вмістом файлу завершена")
        except Exception as error:
            print(error)
        finally:
            file1.close()
            file2.close()
            print("Файли закриті")
    except Exception as ex:
        print(ex)


def task_2():
    try:
        file1 = open("prim1-1.txt", "r")
        file2 = open("prim1-3.txt", "w")
        print("Файли відкриті")
        try:
            for line in file1:
                file2.write(line)
            file2.close()

            file2 = open("prim1-3.txt", "r")
            old_data = file2.read()
            file2.close()

            file2 = open("prim1-3.txt", "r")
            for line2 in file2:
                r=list(line2)
                if r[-2]=='?' in line2:
                    new_data = old_data.replace(line2, line2[::-1].lstrip()+"\n")
                    break
            file2.close()

            file2 = open("prim1-3.txt", "w")
            file2.write(new_data)
            print("Робота з вмістом файлу завершена")

        except Exception as error:
            print(error)
        finally:
            file1.close()
            file2.close()
            print("Файли закриті")
    except Exception as ex:
        print(ex)

def main():
    print("-----Работа с файлами-----")
    task_1()
    task_2()

if __name__ == '__main__':
    main()
