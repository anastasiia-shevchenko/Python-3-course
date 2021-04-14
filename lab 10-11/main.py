from my_class import Person
from my_class import Student
from my_class import Employee
from my_class import SimpleIterator
from my_class import SimpleGenerator
from my_class import MenedgerFile



def main():
    print("----Iterator----")
    people = [Person("Tom", 23), Student("Bob", 20, "Harvard"), Employee("Sam", 35, "Google")]
    iter_list = SimpleIterator(people)

    for person in iter_list:
        print(person)
    print("----Generator----")
    gener_list = SimpleGenerator(people)
    print(next(gener_list))
    for person in gener_list:
        print(person)

    with MenedgerFile('employees.txt', 'w') as opened_file:
        for i in range(0, len(employees)):
            opened_file.write(str(employees[i].surname) + ' ' + str(employees[i].name) + '\n')

    employees1 = list()
    with MenedgerFile('employees.txt', 'r') as opened_file:
        for i in range(0, len(employees)):
            employees1.append(opened_file.readline()[:-1])
            print(employees1[i])

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