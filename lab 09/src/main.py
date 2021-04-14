from my_class import Books
from my_class import Price

def main():


    first_book = Books("Catcher in the rye","D. D. Salinger",5.8,"comedy",200)
    second_book = Books("To Kill a Mockingbird","Harper Lee",9.1,"drama",300)
    third_book = Books("The Snow Queen","G. H. Andersen",8.3,"novel",400)
    fourth_book = Books("Alice in Wonderland", "Lewis Carroll", 8.8, "novel",500)

    my_library = [first_book,second_book,third_book,fourth_book]
    try:
        r = " "
        file1 = open("pr2.txt", "w")
        file2 = open("pr1.txt", "r")
        print("Файли відкриті")
        try:
            print("---Пример записи в файл---")
            file1.write(str(my_library))

            print("---Пример чтения из файла---")
            my_library_2=[]
            for line in range(5):
                name=file2.readline()
                autor=file2.readline()
                rat=float(file2.readline())
                gen=file2.readline()
                pri=int(file2.readline())
                my_library_2.append(Books(name,autor,rat,gen,pri))
            print(my_library_2)

            print("Робота з вмістом файлу завершена")
        except Exception as error:
            print(error)
        finally:
            file1.close()
            file2.close()
            print("Файли закриті")
    except Exception as ex:
        print(ex)

    print("---Пример работы метода __str__(Вывод одного элемента)")
    print(first_book)

    print("---Пример работы метода __repr__(Вывод списка элементов)")
    print(my_library)

    print("---Пример работы метода __lt__(Сортировка по полю 'рейтинг книги')")
    my_library.sort()
    for p in my_library:
        print(p)

    print("---Пример работы метода my_genre (Поиск книг по жанру)")
    genre="novel"
    for r in range(len(my_library)):
        print(my_library[r].my_genre(genre))

    print("---Пример композиции (Цена книги в зависимости с рейтингом и налогом---)")

    my_price_book = Books("The Snow Queen","G. H. Andersen",8.3,"novel",400)
    print(my_price_book.total_price_book())


if __name__ == '__main__':
    main()

