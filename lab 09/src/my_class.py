from abc import ABC, abstractmethod

class Library:
    def __init__(self, name, age):
        self.persons_list.append(name)
        self.__name = name  # instance variable Переменные экземпляра уникальны для каждого экземпляра
        self.__age = age  # устанавливаем возраст




class Books:
    """Модель книги"""

    def __init__(self, book_name,book_autor,book_rating,book_genre,book_price):
        """
        Конструктор обьекта

        :param book_name: Название книги
        :type book_name: string
        :param book_autor: Автор книги
        :type book_autor: string
        :param book_edition: Тираж книги
        :type book_edition: integer
        :param book_issuance: Год выпуска
        :type book_issuance: integer
        """
        self.book_name = book_name
        self.book_autor = book_autor
        self.book_rating = book_rating
        self.book_genre = book_genre
        self.book_price = book_price
        self.total_price = Price(self.book_price)


    def __str__(self):
        """
        Метод отображение информации

        :param: Экземпляр класса
        :return: Возвращает строку
        """
        return f"Название: {self.book_name}\nАвтор: {self.book_autor}\nРейтинг: {self.book_rating}\nЖанр: {self.book_genre}\nЦена: {self.book_price}\n\n"

    def __repr__(self):
        """
        Метод отображение информации
        :return: Экземпляр класса
        :rtype: Возвращает строку cкопировав которую, можно получить экземпляр класса
        """
        return f"Название: {self.book_name}\nАвтор: {self.book_autor}\nРейтинг: {self.book_rating}\nЖанр: {self.book_genre}Цена: {self.book_price}\n\n"

    def __lt__(self, other):
        return self.book_rating > other.book_rating

    def my_genre(self,genre):
        if self.book_genre==genre:
            return f"Название: {self.book_name}\nАвтор: {self.book_autor}\nРейтинг: {self.book_rating}\nЖанр: {self.book_genre}Цена: {self.book_price}\n\n"
        return 0

    def total_price_book(self):
        if self.book_rating<5:
            res=self.total_price.getTotal()*1.95
            return f"Цена книги: {res}"
        elif 5<self.book_rating<8:
            res = self.total_price.getTotal() * 3
            return f"Цена книги: {res}"
        else:
            res = self.total_price.getTotal() * 5.5
            return f"Цена книги: {res}"


class Price:
    def __init__(self,book_tex):
        self.book_tex = book_tex

    def getTotal(self):
        return (self.book_tex * 1.5)