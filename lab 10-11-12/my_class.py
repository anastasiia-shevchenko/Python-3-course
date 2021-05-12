from abc import ABC, abstractmethod

class MenedgerFile(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()


class SimpleIterator:
    def __iter__(self):
        return self

    def __init__(self, list_1):
        self.list_1 = list_1
        self.counter = 0

    def __next__(self):
        if self.counter < len(self.list_1):
            self.counter += 1
            return self.list_1[self.counter-1].name
        else:
            raise StopIteration

def SimpleGenerator(list_1):
    counter = 0
    while counter < len(list_1):
        counter += 1
        yield list_1[counter - 1].name +" "+ str(list_1[counter - 1].age)

class Person:
    # persons_list = []#class variable переменные класса являются общими для всех экземпляров
    # person_Anna="Anna"
    def __init__(self, name, age):

        self.__name = name  # instance variable Переменные экземпляра уникальны для каждого экземпляра
        self.__age = age  # устанавливаем возраст

    @property
    def name(self):
        return self.__name


    @property
    def age(self):
        return self.__age


    def display_info(self):
        print("Имя:", self.__name, "\tВозраст:", self.__age)



class Employee(Person):
    # определение конструктора
    def __init__(self, name, age, company):
        Person.__init__(self, name, age)
        self.company = company

    def display_info(self):
        Person.display_info(self)
        print("Работает в компании:", self.company)


class Student(Person):
    # определение конструктора
    def __init__(self, name, age, university):
        Person.__init__(self, name, age)
        self.university = university

    def display_info(self):
        Person.display_info(self)
        print("Учится в университете", self.university)