from my_class import Person
from my_class import Student
from my_class import Employee
from my_class import SimpleIterator
from my_class import SimpleGenerator
from my_class import MenedgerFile


def main():
    print("----Iterator----")
    pe1ople = [Person("Tom", 23), Student("Bob", 20, "Harvard"), Employee("Sam", 35, "Google")]
    iter_list = SimpleIterator(people)

    for person in iter_list:
        print(person)

    print("----Generator----")
    gener_list = SimpleGenerator(people)
    print(next(gener_list))
    for person in gener_list:
        print(person)

    with MenedgerFile('empl.txt', 'w') as opened_file:
        for i in range(0, len(people)):
            opened_file.write(str(people[i].name) + ' ' + str(people[i].age) + '\n')

    people_new = list()
    with MenedgerFile('empl.txt', 'r') as opened_file:
        for i in range(0, len(people_new)):
            people_new.append(opened_file.readline()[:-1])
            print(people_new[i])

    # Kevin=Student("Kevin", 20, "Harvard")
    # Kevin.display_info()
    #
    # #--------------Пример экземпляра класса
    #
    # Viktor=Person("Viktor",24)
    # print(Viktor.person_Anna)
    # # Anna
    # print(Viktor.display_info())
    # # Viktor
    #
    #
    # #------------------------------------
    # Lusi=Person("Lusi",19)
    # Vera=Person("Vera",29)
    #
    # print(Lusi.persons_list)
    # # [...Lusi,Vera]
    # print(Vera.persons_list)
    # # [...Lusi,Vera]
    # print(Person.persons_list)
    # # [...Lusi,Vera]

if __name__ == '__main__':
    main()